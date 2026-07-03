#!/usr/bin/env python3
"""Stage 2 (faceted): distill each paper into a STRUCTURED multi-FACET computational fingerprint.

One LLM call per paper (the only expensive step; cached). Emits 8 labeled facets:
  MECHANISM     - free-text domain-neutral skeleton (== the old flat skeleton; the baseline rep)
  DOMAIN        - topical field (the ONLY facet allowed to name the field; the recall control)
  STRUCTURE     - computational pattern, scaffolded by the Berkeley 13 motifs (the precision spine)
  DATA_OBJECT   - the primary data structure operated on
  INFERENCE     - how unknowns / uncertainty are handled
  PROBLEM_FORM  - the abstract goal type
  DISTRIBUTION  - measured outcome distribution + the estimator's ASSUMED distribution (operator 2)
  COMPLEXITY    - complexity class / guarantee, if stated

Non-math NOISE papers (qualitative, position, survey-without-method, descriptive-only) are handled
explicitly: the mechanism facets come back "none", so they can never read as a method-twin. That is
the point of mixing them in (does the fingerprint correctly STAY SILENT on papers with no method?).

Each facet is embedded SEPARATELY downstream; operators are similarity/disagreement queries over a
chosen facet subset; precision/recall is tuned by (1) THIS prompt (vector quality) and (2) the facet
subset (operating point). Design: docs/FACETED_FINGERPRINT_DESIGN.md.

Backends (auto): ollama (local, no rate limit, default qwen2.5:14b-instruct) or anthropic (if key set).
Determinism: temperature 0. The prompt below IS part of the method; keep it fixed across the corpus.

Usage:
  python src/distill_faceted.py                       # all md, ollama, cached
  python src/distill_faceted.py --backend anthropic --model claude-opus-4-8 --ids clf-clin-001
"""
from __future__ import annotations
import argparse, os, re, sys
from pathlib import Path

FACETS = ["MECHANISM", "DOMAIN", "STRUCTURE", "DATA_OBJECT", "INFERENCE",
          "PROBLEM_FORM", "DISTRIBUTION", "COMPLEXITY",
          "DATA_AVAILABILITY", "CODE_AVAILABILITY", "PREREGISTRATION", "EVIDENCE_BASIS"]

# ---- THE faceted distillation prompt (fixed; part of the method) ------------
DISTILL_PROMPT = """You are reducing a research paper to a STRUCTURED COMPUTATIONAL FINGERPRINT:
a small set of independent FACETS, each on its own line with the EXACT label shown. Two papers
from different fields that use the SAME underlying computation must agree on the mechanism facets
even when their topics differ.

FIRST decide: does this paper actually COMPUTE something (a mathematical or algorithmic method,
model, estimator, simulation, or proof)? If it is qualitative, a position/opinion piece, a survey
with no new method, or a purely descriptive or empirical report with no method of its own, then it
has NO computational core: write "none" for STRUCTURE, DATA_OBJECT, INFERENCE, DISTRIBUTION and
COMPLEXITY, and keep MECHANISM to a single sentence.

Output EXACTLY these labeled lines and nothing else (no preamble, no markdown, no blank lines):

MECHANISM: <a COMPLETE, detailed 6 to 12 sentence skeleton; this is the primary RETRIEVAL signal, so do
NOT abbreviate or defer detail to the facets below. What is computed and the algorithmic steps in order, in GENERIC
mathematical language. Strip ALL domain, application and dataset words (no "patient", "stock",
"gene", "galaxy", "city", "voter"; replace with "an entity", "a quantity", "an observation"). Do
NOT name famous methods (no "Kalman filter", "SVM", "PageRank", "EM algorithm", "Gaussian process",
"HMM") unless the mathematics cannot be stated without the name. If there is no computational core,
write one sentence describing what the paper does instead.>
DOMAIN: <the mathematical subject area or topical field, 3 to 8 words. This is the ONLY facet where
you may name the field or application.>
STRUCTURE: <the computational PATTERN, domain-neutral. If it matches one of these, name that one:
dense linear algebra; sparse linear algebra; spectral or transform; N-body or all-pairs; structured
grid; unstructured mesh; map-reduce or embarrassingly-parallel; combinational logic; graph traversal;
dynamic programming; backtracking or branch-and-bound; graphical models; finite-state machine. If it
is a different pattern, write "other: <a few words>". Write "none" if there is no computation.>
DATA_OBJECT: <the primary structure operated on: dense matrix or tensor; sparse matrix; grid or
lattice; mesh; graph or network; point set; sequence or time-series; tree or hierarchy; set or
table; continuous function or field. Write "none" if there is no computation.>
INFERENCE: <how unknowns or uncertainty are handled: deterministic or closed-form; frequentist
point estimate; Bayesian posterior; variational; sampling or Monte-Carlo; bootstrap or resampling;
optimization only. Write "none" if not applicable.>
PROBLEM_FORM: <the abstract goal, domain-neutral: estimation; prediction or classification;
optimization; decision or test; search; counting; simulation or generation; proof or
characterization; control; ranking or retrieval.>
DISTRIBUTION: <if the method models an outcome variable, name BOTH the outcome's measured
distribution (count; continuous; proportion or bounded; ordinal; binary; survival or time-to-event;
heavy-tailed) AND the distribution the estimator ASSUMES. Write "none" if not applicable.>
COMPLEXITY: <complexity class or guarantee, if the paper states one: closed-form; polynomial
iterative; combinatorial or NP-hard; consistency; finite-sample bound; convergence rate; regret
bound. Write "not stated" if absent.>
DATA_AVAILABILITY: <does the paper release or rely on a dataset with a PERSISTENT identifier? EXACTLY one
of: dataset-with-DOI-or-handle; dataset-in-repository; public-benchmark-used; data-on-request; proprietary; none>
CODE_AVAILABILITY: <is the code/software available? EXACTLY one of: public-repository; on-request; none>
PREREGISTRATION: <EXACTLY one of: registered-report; preregistered; analysis-plan-stated; none>
EVIDENCE_BASIS: <the basis of the paper's claims, EXACTLY one of: empirical-with-released-data;
empirical-with-private-data; simulation-study; mathematical-proof; reanalysis-of-existing-data; review-or-position>

IMPORTANT: STRUCTURE, DATA_OBJECT, INFERENCE, PROBLEM_FORM and the four availability/evidence facets must
each be EXACTLY ONE value (the single best match), never a list. PREFER a listed term over a synonym, so
that two papers doing the same thing get the SAME label (consistency matters more than nuance here; put
nuance in MECHANISM). Write each controlled-vocab value as a SINGLE lowercase term copied from its list,
with NO trailing punctuation and no extra words; never leave a facet blank (use the listed none / not stated
value when nothing applies).

PAPER TEXT:
"""

MAX_CHARS = 24000

# Keep-domain ablation arm: identical prompt, but retain the paper's domain words (isolates the
# domain-stripping effect from the LLM re-description itself). Selected by --keep-domain.
KEEP_DOMAIN_PROMPT = re.sub(
    r'Strip ALL domain.*?an observation"\)\.',
    "Keep the paper's own domain, application and dataset words as written; do NOT genericize them.",
    DISTILL_PROMPT, flags=re.S)

# point at a remote GPU box with: OLLAMA_HOST=http://<your-gpu-host>:11434
OLLAMA = os.environ.get("OLLAMA_HOST", "http://localhost:11434").rstrip("/")
if not OLLAMA.startswith("http"):
    OLLAMA = "http://" + OLLAMA


def _body(md_path: Path) -> str:
    text = md_path.read_text(encoding="utf-8")
    text = re.sub(r"^---\n.*?\n---\n", "", text, flags=re.S)
    return text[:MAX_CHARS]


def distill_ollama(text: str, model: str, prompt: str = DISTILL_PROMPT) -> str:
    import requests
    r = requests.post(f"{OLLAMA}/api/generate", timeout=600,
                      json={"model": model, "prompt": prompt + text,
                            "stream": False, "options": {"temperature": 0, "num_ctx": 16384}})
    r.raise_for_status()
    return r.json()["response"].strip()


def distill_anthropic(text: str, model: str, prompt: str = DISTILL_PROMPT) -> str:
    import requests
    r = requests.post("https://api.anthropic.com/v1/messages", timeout=600,
                      headers={"x-api-key": os.environ["ANTHROPIC_API_KEY"],
                               "anthropic-version": "2023-06-01",
                               "content-type": "application/json"},
                      json={"model": model, "max_tokens": 1100, "temperature": 0,
                            "messages": [{"role": "user", "content": prompt + text}]})
    r.raise_for_status()
    return "".join(b.get("text", "") for b in r.json()["content"]).strip()


def parse_facets(raw: str) -> dict[str, str]:
    """Split the labeled block into {facet: text}. Tolerant of minor label drift."""
    out = {f: "" for f in FACETS}
    cur = None
    for line in raw.splitlines():
        m = re.match(r"\s*\*{0,2}\s*([A-Z][A-Z_]+)\s*\*{0,2}\s*:\s*(.*)", line)  # tolerate **bold** labels
        if m and m.group(1) in FACETS:
            cur = m.group(1); out[cur] = re.sub(r"\*\*", "", m.group(2)).strip()
        elif cur:
            out[cur] += " " + re.sub(r"\*\*", "", line).strip()
    return {k: v.strip() for k, v in out.items()}


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--data", default="data")
    ap.add_argument("--backend", choices=["ollama", "anthropic"],
                    default="anthropic" if os.environ.get("ANTHROPIC_API_KEY") else "ollama")
    ap.add_argument("--model", default=None)
    ap.add_argument("--ids", nargs="*")
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--outdir", default=None, help="output dir (default data/skeletons_faceted; set per-distiller for benchmarks)")
    ap.add_argument("--keep-domain", action="store_true", help="ablation arm: keep domain words instead of stripping them")
    a = ap.parse_args()
    model = a.model or ("claude-opus-4-8" if a.backend == "anthropic" else "qwen2.5:14b-instruct")
    distill = distill_anthropic if a.backend == "anthropic" else distill_ollama
    prompt = KEEP_DOMAIN_PROMPT if a.keep_domain else DISTILL_PROMPT

    md_dir = Path(a.data) / "md"
    sk_dir = Path(a.outdir) if a.outdir else Path(a.data) / "skeletons_faceted"
    sk_dir.mkdir(parents=True, exist_ok=True)
    ids = a.ids or sorted(p.stem for p in md_dir.glob("*.md"))
    ok = skip = fail = nomethod = 0
    for rid in ids:
        out = sk_dir / f"{rid}.md"
        if out.exists() and not a.force:
            skip += 1; continue
        md = md_dir / f"{rid}.md"
        if not md.exists():
            print(f"  MISS {rid} (no md)"); fail += 1; continue
        try:
            raw = distill(_body(md), model, prompt)
            raw = re.sub(r"<think>.*?</think>\s*", "", raw, flags=re.S).strip()  # drop thinking-model traces
            fac = parse_facets(raw)
            if not fac["MECHANISM"]:
                print(f"  WARN {rid}: no MECHANISM parsed; storing raw")
            out.write_text(raw + "\n", encoding="utf-8")
            tag = "no-method" if fac["STRUCTURE"].lower().startswith("none") else "method"
            nomethod += tag == "no-method"
            print(f"  ok   {rid:34} {len(raw):>5} chars  [{tag}]"); ok += 1
        except Exception as e:  # noqa: BLE001
            print(f"  FAIL {rid:34} {type(e).__name__}: {e}"); fail += 1
    print(f"[distill_faceted:{a.backend}/{model}] ok={ok} skip={skip} fail={fail} "
          f"no-method={nomethod} -> {sk_dir}")


if __name__ == "__main__":
    main()
