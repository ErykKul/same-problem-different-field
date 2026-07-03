#!/usr/bin/env python3
"""The CANONICAL v1 distiller: the simple 8-facet prompt (MECHANISM skeleton + 7 controlled facets),
the configuration that wins on facet_select (combined AP 0.309). Reconstructed 2026-06 (the original
distill_haiku.py was lost in iteration; this matches the haiku-v1 skeleton format exactly and is the
prompt the reproducibility run + the paper appendix use). NO curated vocabulary / glossary (that
over-coarsens, see distill_vocab.py + paper Part C); the open "other:" escape is kept on purpose.

Backends via env / flags:
  --backend ollama   (OLLAMA_HOST env, default http://localhost:11434; --model qwen2.5:14b-instruct)
  --backend anthropic (ANTHROPIC_API_KEY env; --model claude-opus-4-8 / claude-haiku-4-5)

  python src/distill_v1.py --backend ollama --model qwen2.5:14b-instruct --outdir data/skeletons_v1_qwen25
"""
from __future__ import annotations
import argparse, os, re, csv, io
from pathlib import Path
import requests
from distill_faceted import parse_facets  # tolerant label parser, reused

FACETS = ["MECHANISM", "DOMAIN", "STRUCTURE", "DATA_OBJECT", "INFERENCE",
          "PROBLEM_FORM", "DISTRIBUTION", "COMPLEXITY"]

DISTILL_PROMPT = """You are reducing a research paper to a STRUCTURED COMPUTATIONAL FINGERPRINT: a small
set of FACETS, each on its own line with the EXACT label shown. Two papers from different fields that
use the SAME underlying computation must agree on these facets even when their topics differ.

FIRST decide: does this paper COMPUTE something (a mathematical or algorithmic method, model,
estimator, simulation, or proof)? If it is qualitative, a position/opinion piece, a survey with no new
method, or a purely descriptive report with no method of its own, it has NO computational core: write
"none" for STRUCTURE, DATA_OBJECT, INFERENCE, DISTRIBUTION and COMPLEXITY, and keep MECHANISM to one
sentence.

The controlled facets (STRUCTURE, DATA_OBJECT, INFERENCE, PROBLEM_FORM) must each be EXACTLY ONE short
value; if nothing fits, write "other: <short term>". Put any nuance in MECHANISM, not in the facets.
Do not name a method/algorithm/software in any facet value.

Output EXACTLY these labeled lines and nothing else (no preamble, no markdown, no blank lines):

MECHANISM: <a domain-neutral skeleton of WHAT is computed and the key algorithmic steps in order, 6 to
12 sentences, in GENERIC mathematical language. Strip ALL domain / application / dataset words (no
"patient", "gene", "stock", "galaxy", "city", "voter"; use "an entity", "a quantity", "an
observation"). Do NOT name famous methods (no "Kalman filter", "SVM", "PageRank", "EM algorithm",
"Gaussian process", "HMM") unless the mathematics cannot be stated without the name.>
DOMAIN: <the subject area or topical field, 3 to 8 words; the ONLY facet that may name the field.>
STRUCTURE: <the dominant computational pattern, one short term, e.g. dense linear algebra, sparse
linear algebra, spectral or transform, N-body or all-pairs, structured grid, unstructured mesh, graph
traversal, dynamic programming, graphical models, kernel method, neural network, numerical
optimization, MCMC sampling, map-reduce, finite-state machine, or "other: <term>".>
DATA_OBJECT: <the primary structure operated on, one of: dense matrix or tensor, sparse matrix, grid
or lattice, mesh, graph or network, point set, sequence or time-series, tree or hierarchy, set or
table, continuous function or field, none.>
INFERENCE: <one of: deterministic or closed-form, frequentist point estimate, maximum likelihood,
bayesian posterior, variational, sampling or Monte-Carlo, bootstrap or resampling, deterministic
optimization, none.>
PROBLEM_FORM: <one of: estimation, prediction or classification, optimization, decision or test,
search, counting, simulation or generation, proof or characterization, control, ranking or retrieval,
reconstruction or denoising, none.>
DISTRIBUTION: <format "<measured>; <assumed>", one coarse token per side. measured: continuous,
count, proportion or bounded, binary, ordinal, survival, heavy-tailed, none. assumed: gaussian,
logistic, poisson, binomial, multinomial, gaussian mixture, exponential, nonparametric, none.>
COMPLEXITY: <one of: closed-form, polynomial iterative, combinatorial or NP-hard, consistency,
finite-sample bound, convergence rate, regret bound, not stated.>

PAPER TEXT:
"""

MAX_CHARS = 24000
OLLAMA = os.environ.get("OLLAMA_HOST", "http://localhost:11434").rstrip("/")
if not OLLAMA.startswith("http"):
    OLLAMA = "http://" + OLLAMA


def _body(p: Path) -> str:
    t = re.sub(r"^---\n.*?\n---\n", "", p.read_text(encoding="utf-8"), flags=re.S)
    return t[:MAX_CHARS]


def distill_ollama(text, model):
    r = requests.post(f"{OLLAMA}/api/generate", timeout=600,
                      json={"model": model, "prompt": DISTILL_PROMPT + text, "stream": False,
                            "options": {"temperature": 0, "num_ctx": 16384}})
    r.raise_for_status()
    return r.json()["response"].strip()


def distill_anthropic(text, model):
    r = requests.post("https://api.anthropic.com/v1/messages", timeout=600,
                      headers={"x-api-key": os.environ["ANTHROPIC_API_KEY"],
                               "anthropic-version": "2023-06-01", "content-type": "application/json"},
                      json={"model": model, "max_tokens": 1100, "temperature": 0,
                            "messages": [{"role": "user", "content": DISTILL_PROMPT + text}]})
    r.raise_for_status()
    return "".join(b.get("text", "") for b in r.json()["content"]).strip()


def seed_ids():
    out = set()
    for c in ["datasets/mode_a_seed_families.csv"]:
        if not os.path.exists(c):
            continue
        for r in csv.DictReader(io.StringIO("\n".join(l for l in open(c).read().splitlines()
                                                       if not l.lstrip().startswith("#")))):
            rid = (r.get("id") or "").strip()
            if rid and (r.get("url") or "").strip() and (r.get("role") or "member").strip() == "member":
                out.add(rid)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", default="data")
    ap.add_argument("--backend", choices=["ollama", "anthropic"], default="ollama")
    ap.add_argument("--model", default="qwen2.5:14b-instruct")
    ap.add_argument("--outdir", required=True)
    ap.add_argument("--ids", nargs="*")
    ap.add_argument("--seeds", action="store_true")
    ap.add_argument("--force", action="store_true")
    a = ap.parse_args()
    distill = distill_anthropic if a.backend == "anthropic" else distill_ollama
    md = Path(a.data) / "md"
    out = Path(a.outdir)
    out.mkdir(parents=True, exist_ok=True)
    ids = a.ids or sorted(p.stem for p in md.glob("*.md"))
    if a.seeds:
        s = seed_ids()
        ids = [i for i in ids if i in s]
    ok = skip = fail = 0
    for rid in ids:
        o = out / f"{rid}.md"
        if o.exists() and not a.force:
            skip += 1
            continue
        mp = md / f"{rid}.md"
        if not mp.exists():
            fail += 1
            continue
        try:
            raw = re.sub(r"<think>.*?</think>\s*", "", distill(_body(mp), a.model), flags=re.S).strip()
            o.write_text(raw + "\n", encoding="utf-8")
            ok += 1
            if ok % 25 == 0:
                print(f"  ...{ok} done", flush=True)
        except Exception as e:  # noqa: BLE001
            print(f"  FAIL {rid}: {type(e).__name__}: {e}", flush=True)
            fail += 1
    print(f"[distill_v1:{a.backend}/{a.model}] ok={ok} skip={skip} fail={fail} -> {out}", flush=True)


if __name__ == "__main__":
    main()
