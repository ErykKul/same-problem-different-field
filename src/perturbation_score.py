#!/usr/bin/env python3
"""Score the interventional perturbation test (structure vs surface).

Two controlled perturbations per paper: RE-SKIN (change the field, keep the computation) and MATH-EDIT
(keep the field, change the computation). A representation that keys on the COMPUTATION should stay
invariant under re-skin and move under math-edit; a topical representation (the abstract) should do the
opposite. We report the 2x2 of cosine self-similarity to the original, for the fingerprint (the distilled
skeleton) and for the abstract baseline, under each perturbation, plus a paired bootstrap CI on the
interaction (fingerprint gap minus abstract gap), the single number that the structure-vs-surface claim
rides on. Reads the perturbation workflow result (rewrites + skeletons) and the original abstracts.
"""
import json
import os
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

np.random.seed(0)
# Ship the rewrite+skeleton result in the package so the scoring reproduces offline; fall back to the
# scratchpad when regenerating live. (Generating the rewrites/skeletons needs an LLM; scoring does not.)
PKG = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "datasets", "validity")
SCRATCH = os.environ.get("SCRATCH_DIR", ".")
DATA = "data/md"
_pp = os.path.join(PKG, "perturbation.json")
R = json.load(open(_pp if os.path.exists(_pp) else os.path.join(SCRATCH, "perturbation.json")))
rw = {r["id"]: r for r in R["rewrites"] if r}
sk = {s["id"]: s for s in R["skeletons"] if s}
ids = [i for i in sk if i in rw]


def cos_pairs(triples):
    flat = []
    for o, r, m in triples:
        flat += [o, r, m]
    V = TfidfVectorizer().fit_transform(flat).toarray()

    def c(i, j):
        a, b = V[i], V[j]
        return float(a @ b / (np.linalg.norm(a) * np.linalg.norm(b) + 1e-12))
    rr = np.array([c(3 * k, 3 * k + 1) for k in range(len(triples))])
    mm = np.array([c(3 * k, 3 * k + 2) for k in range(len(triples))])
    return rr, mm


fp_r, fp_m = cos_pairs([(sk[i]["s_orig"], sk[i]["s_reskin"], sk[i]["s_math"]) for i in ids])
ab_r, ab_m = cos_pairs([(open(f"{DATA}/{i}.md", encoding="utf-8").read(), rw[i]["reskin"], rw[i]["math"]) for i in ids])

print(f"interventional perturbation test ({len(ids)} papers): cosine self-similarity to the ORIGINAL")
print(f"  re-skin = change field, keep computation   |   math-edit = keep field, change computation")
print(f"  {'':26}{'RE-SKIN':>9}{'MATH-EDIT':>11}")
print(f"  {'FINGERPRINT (skeleton)':26}{fp_r.mean():>9.3f}{fp_m.mean():>11.3f}   (want high | low: keys on computation)")
print(f"  {'ABSTRACT (baseline)':26}{ab_r.mean():>9.3f}{ab_m.mean():>11.3f}   (want low | high: keys on field)")
inter = (fp_r - fp_m) - (ab_r - ab_m)
boot = np.array([np.random.choice(inter, len(inter), replace=True).mean() for _ in range(5000)])
print(f"  interaction (fingerprint gap - abstract gap): {inter.mean():.3f}  95% CI "
      f"[{np.percentile(boot, 2.5):.3f}, {np.percentile(boot, 97.5):.3f}]  (>0 => double dissociation)")
print(f"  per-paper fingerprint gap > abstract gap: {(inter > 0).sum()}/{len(ids)}")
