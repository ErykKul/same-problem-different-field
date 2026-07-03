#!/usr/bin/env python3
"""Sample a cross-domain discovery set from arXiv (Mode B), frozen into a CSV.

Pulls method-bearing papers across distinct fields within a date window. The
chosen categories are all "a mathematical method applied to a problem" fields
(statistics, control, ML, quantitative bio/finance, computational physics, ...),
so the sample is dense in exactly the papers whose computational skeleton we want
to cluster.

Reproducible: same window + categories + cap -> same frozen list. We freeze the
ids into the CSV (the versioned input) rather than re-querying at build time, so
the published corpus does not drift with the live arXiv index.

    python src/sample_arxiv.py --from 20260301 --to 20260331 --per-cat 35
"""
from __future__ import annotations
import argparse, csv, sys, time
import xml.etree.ElementTree as ET
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import requests  # noqa: E402
from arxiv_lib import API, ATOM, ARX, UA, _norm_id  # noqa: E402

# Ten distinct domains, each a field where papers solve a problem with explicit math.
DEFAULT_CATS = [
    "stat.ME",            # statistics / methodology
    "eess.SY",            # systems & control
    "cs.LG",              # machine learning
    "q-bio.QM",           # quantitative biology
    "q-fin.ST",           # quantitative finance
    "physics.soc-ph",     # computational social science
    "cond-mat.stat-mech", # statistical physics
    "astro-ph.IM",        # astro instrumentation & methods
    "q-bio.NC",           # computational neuroscience
    "math.OC",            # optimization & control
]

# NON-MATH / qualitative NOISE: papers that mostly do not "apply a math method to a problem".
# Mixed into the corpus so we test whether the fingerprint correctly STAYS SILENT (mechanism facets
# = "none") on papers with no computational core, and so precision/recall are measured against a
# realistic, messy background rather than an all-quantitative one. arXiv skews STEM, so these are
# qualitative-STEM (HCI studies, policy, position/history papers); deeper humanities/social-science
# noise would need a non-arXiv source and is out of scope for this open release.
NOISE_CATS = [
    "cs.CY",          # computers & society (policy/ethics, often qualitative)
    "cs.HC",          # human-computer interaction (qualitative user studies)
    "cs.DL",          # digital libraries
    "physics.hist-ph",# history & philosophy of physics (non-mathematical)
    "econ.GN",        # general economics (often non-formal)
    "cs.SI",          # social & information networks (mixed)
]


def sample_cat(cat: str, d_from: str, d_to: str, n: int) -> list[dict]:
    q = f"cat:{cat} AND submittedDate:[{d_from}0000 TO {d_to}2359]"
    params = {"search_query": q, "start": 0, "max_results": n,
              "sortBy": "submittedDate", "sortOrder": "ascending"}
    r = requests.get(API, params=params, headers=UA, timeout=40)
    r.raise_for_status()
    root = ET.fromstring(r.text)
    out = []
    for e in root.findall(f"{ATOM}entry"):
        prim = e.find(f"{ARX}primary_category")
        out.append({"id": _norm_id(e.findtext(f"{ATOM}id") or ""),
                    "primary": prim.get("term") if prim is not None else cat})
    return out


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--from", dest="d_from", default="20260301")
    ap.add_argument("--to", dest="d_to", default="20260331")
    ap.add_argument("--per-cat", type=int, default=35)
    ap.add_argument("--noise", type=int, default=0, help="papers per NON-MATH noise category")
    ap.add_argument("--prefix", default="mb", help="id prefix (use a fresh one to avoid collisions)")
    ap.add_argument("--cats", nargs="*", default=DEFAULT_CATS)
    ap.add_argument("--out", default="datasets/mode_b_discovery.csv")
    a = ap.parse_args()

    jobs = [(c, a.per_cat, "") for c in a.cats]
    if a.noise:
        jobs += [(c, a.noise, "noise") for c in NOISE_CATS]
    seen: set[str] = set()
    rows: list[tuple[str, str, str, str]] = []
    for cat, n, note in jobs:
        k = 0
        for p in sample_cat(cat, a.d_from, a.d_to, n):
            if p["id"] in seen:
                continue
            seen.add(p["id"]); k += 1
            rid = f"{a.prefix}-{cat.replace('.', '-')}-{k:03d}"
            rows.append((rid, f"https://arxiv.org/abs/{p['id']}", cat, note))
        print(f"  {cat:22} {k:3} papers {note}", file=sys.stderr)
        time.sleep(1)  # be polite to the arXiv API

    out = Path(a.out)
    with out.open("w", newline="", encoding="utf-8") as fh:
        fh.write("# Mode B discovery set: frozen arXiv sample (UNLABELED).\n")
        fh.write(f"# regenerate: python src/sample_arxiv.py --from {a.d_from} --to {a.d_to} "
                 f"--per-cat {a.per_cat}\n")
        fh.write(f"# window {a.d_from}..{a.d_to}; cats: {','.join(a.cats)}\n")
        w = csv.writer(fh)
        w.writerow(["id", "url", "field", "license", "note"])
        for rid, url, cat, note in rows:
            w.writerow([rid, url, cat, "arXiv", note])
    print(f"[done] {len(rows)} papers -> {out}", file=sys.stderr)


if __name__ == "__main__":
    main()
