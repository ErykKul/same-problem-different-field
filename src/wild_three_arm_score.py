#!/usr/bin/env python3
"""Score the three-arm wild import-candidacy study from the blind annotations + the arm key.

Reports, per arm (system-top / random / single-facet-collision): the precision = fraction of pairs a
MAJORITY of the three blind annotators judged a genuine cross-domain import candidate, a paired
bootstrap 95% CI, the per-annotator yes-counts, and the overall Fleiss kappa (3 raters).

Inputs (scratchpad): wild_3arm_annotations.json = {annotators:[{annotator,judgments:[{id,genuine}]}]}
(the blind-annotation workflow result), and wild_3arm_key.json = {id:{arm,a,b}} (from wild_three_arm.py).
"""
import json
import os
import numpy as np

np.random.seed(0)
# Ship the blind-annotation result + arm key in the package so the scoring reproduces offline; fall back
# to the scratchpad when regenerating live. (Generating the annotations needs an LLM; scoring does not.)
PKG = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "datasets", "validity")
SCRATCH = os.environ.get("SCRATCH_DIR", ".")


def _load(name):
    p = os.path.join(PKG, name)
    return json.load(open(p if os.path.exists(p) else os.path.join(SCRATCH, name)))


ann = _load("wild_3arm_annotations.json")["annotators"]
key = _load("wild_3arm_key.json")
arm = {int(i): key[i]["arm"] for i in key}

votes = {}  # id -> list of bool, one per annotator
for a in ann:
    for j in a["judgments"]:
        votes.setdefault(int(j["id"]), []).append(bool(j["genuine"]))
ids = sorted(votes)
nrat = len(ann)
maj = {i: sum(votes[i]) >= (nrat // 2 + 1) for i in ids}


def prec_ci(arm_name, B=5000):
    x = np.array([1.0 if maj[i] else 0.0 for i in ids if arm[i] == arm_name])
    if len(x) == 0:
        return float("nan"), 0, 0, 0
    boot = np.array([np.random.choice(x, len(x), replace=True).mean() for _ in range(B)])
    return x.mean(), np.percentile(boot, 2.5), np.percentile(boot, 97.5), len(x)


print(f"three-arm wild import-candidacy precision ({nrat} blind annotators, majority vote)")
print(f"  {'arm':12}{'precision':>10}{'95% CI':>18}{'n':>5}   per-annotator yes")
for a in ["top", "random", "collision"]:
    p, lo, hi, n = prec_ci(a)
    pa = [sum(1 for j in ad["judgments"] if arm[int(j["id"])] == a and j["genuine"]) for ad in ann]
    print(f"  {a:12}{p:>10.3f}   [{lo:.3f}, {hi:.3f}]{n:>5}   {pa}")

# Fleiss kappa (binary, nrat raters)
N = len(ids)
M = np.zeros((N, 2))
for idx, i in enumerate(ids):
    y = sum(votes[i]); M[idx] = [y, nrat - y]
Pi = ((M ** 2).sum(1) - nrat) / (nrat * (nrat - 1))
pj = M.sum(0) / (N * nrat)
Pe = (pj ** 2).sum()
kappa = (Pi.mean() - Pe) / (1 - Pe) if (1 - Pe) > 0 else float("nan")
print(f"  Fleiss kappa ({nrat} raters): {kappa:.3f}")
