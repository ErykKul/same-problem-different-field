#!/usr/bin/env python3
"""Reproducible name-free audit of the mechanism skeletons (the anti-cheat property).

The central anti-cheat claim is that a skeleton's MECHANISM text describes the computation
WITHOUT naming the canonical method, so a cross-field match is genuine abstraction rather than
name recognition. This script makes the name-free headline reproducible from the shipped
artifact, using EXPLICIT, pinned forbidden-name lists rather than an undocumented one, and
reports the number under each so the reader can see how list-sensitive it is.

Three nested, pinned lists:
  DISTILLER  the exact method families the distiller was INSTRUCTED to strip
             (see src/distill_faceted.py: "Kalman filter, SVM, PageRank, EM algorithm,
             Gaussian process, HMM"), with morphological variants. This is the list the
             paper's headline rate is measured against.
  EXTENDED   DISTILLER + the canonical proper-noun names of the other benchmark cores
             (Metropolis, LASSO, Viterbi, Bradley-Terry, preferential attachment,
             Lotka-Volterra, Hawkes, kriging, naive Bayes, Huckel). A stricter skeptic's list.
  BROAD      EXTENDED + generic technique/paradigm labels (PCA, SVD, Fourier, MCMC, wavelet)
             that are not method names but bound the rate from below.

Audits the MECHANISM field only (the free-text computational description the distiller is told
to keep name-free); the DOMAIN facet is allowed to name the field/application and is excluded.

Usage:  python src/name_free_audit.py [skeleton_dir ...]
        (default: data/skeletons_faceted_haiku, the paper's primary distiller)
"""
import re
import sys
from pathlib import Path

DISTILLER = [
    r"kalman", r"gaussian process", r"\bsvm\b", r"support[- ]vector machine",
    r"em algorithm", r"expectation[- ]maximi[sz]ation", r"\bhmm\b", r"hidden markov",
    r"\bpagerank\b", r"page[- ]rank",
]
EXTENDED = DISTILLER + [
    r"\bviterbi\b", r"\blasso\b", r"kriging", r"bradley[- ]?terry", r"lotka[- ]?volterra",
    r"preferential attachment", r"metropolis", r"hawkes", r"h[uü]ckel", r"naive bayes",
]
BROAD = EXTENDED + [
    r"\bpca\b", r"principal component", r"\bsvd\b", r"singular value decomposition",
    r"\bfourier\b", r"\bmcmc\b", r"wavelet", r"replicator",
]
LISTS = [("DISTILLER", DISTILLER), ("EXTENDED ", EXTENDED), ("BROAD    ", BROAD)]

FACET_LABELS = ("DOMAIN:", "STRUCTURE:", "DATA_OBJECT:", "INFERENCE:", "PROBLEM_FORM:",
                "DISTRIBUTION:", "COMPLEXITY:", "DATA_AVAILABILITY:", "CODE_AVAILABILITY:",
                "PREREGISTRATION:", "EVIDENCE_BASIS:")


def mechanism(text):
    """Extract the MECHANISM field (from 'MECHANISM:' up to the next facet label)."""
    m = re.search(r"MECHANISM:(.*?)(?=\n(?:%s)|\Z)" % "|".join(re.escape(f) for f in FACET_LABELS),
                  text, re.S)
    return (m.group(1) if m else text)


def audit(dirpath):
    mechs = {f.stem: mechanism(f.read_text(encoding="utf-8"))
             for f in sorted(Path(dirpath).glob("*.md"))}
    n = len(mechs)
    out = {}
    for name, terms in LISTS:
        rx = re.compile("|".join(terms), re.I)
        leaks = [(stem, rx.search(mech).group(0)) for stem, mech in mechs.items() if rx.search(mech)]
        out[name] = leaks
    return n, out


def main():
    dirs = sys.argv[1:] or ["data/skeletons_faceted_haiku"]
    for d in dirs:
        n, out = audit(d)
        print(f"\n=== {d}  ({n} skeletons) ===")
        for name, leaks in out.items():
            print(f"{name}: {n - len(leaks)}/{n} name-free = {100*(n-len(leaks))/n:.1f}%  "
                  f"({len(leaks)} name a method)")
        distiller_leaks = out["DISTILLER"]
        print(f"  DISTILLER-list mentions ({len(distiller_leaks)}; permitted where the math needs the name):")
        for stem, tok in distiller_leaks:
            print(f"    {stem}: {tok!r}")


if __name__ == "__main__":
    main()
