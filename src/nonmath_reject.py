#!/usr/bin/env python3
"""Non-math rejection (paper 1, Section 5.3): the operator stays silent where there is no computation.

Of the cross-field pairs that touch a deliberately non-mathematical paper (the 64 papers sampled from the
six qualitative arXiv NOISE categories cs.CY, cs.HC, cs.DL, physics.hist-ph,
econ.GN, cs.SI), what fraction does the operator score as a cross-field twin?

Twin call = the deployed retrieve-then-filter operator at its natural operating point: rank all
cross-field pairs by whole-fingerprint TF-IDF cosine, take the top 210 (= the number of twins the
benchmark plants), and keep the ones whose four CORE computational facets all agree. Non-computational
papers carry empty / degenerate STRUCTURE, so they almost never survive both stages.

Reproduces (Section 5.3): 27,968 cross-field non-math x computational pairs; 32 score as twins -> 0.001.

Offline once the faceted skeletons + manifest are present.  Run:  python src/nonmath_reject.py
"""
import glob
import os
import sys

sys.path.insert(0, ".")
sys.path.insert(0, "src")
import reproduce as R  # noqa: E402
import embed as E      # noqa: E402

SKDIR = "data/skeletons_faceted_haiku"
CORE = ["STRUCTURE", "DATA_OBJECT", "INFERENCE", "PROBLEM_FORM"]
NOISE_ID = ("mc-cs-CY-", "mc-cs-HC-", "mc-cs-DL-", "mc-physics-hist-ph-", "mc-econ-GN-", "mc-cs-SI-")
N_TWINS = 210  # the benchmark's planted cross-field twin count = the operator's operating point


def parse_facets(path):
    d = {}
    for line in open(path, encoding="utf-8"):
        if ":" in line:
            k, v = line.split(":", 1)
            d[k.strip()] = v.strip().lower()
    return d


ids = sorted(os.path.basename(f)[:-3] for f in glob.glob(f"{SKDIR}/*.md"))
fac = {i: parse_facets(f"{SKDIR}/{i}.md") for i in ids}
lab, mfield = R.load_labels(), R.load_field()
field = {i: (mfield.get(i) or lab.get(i, {}).get("field", "") or "?") for i in ids}
nonmath = {i for i in ids if i.startswith(NOISE_ID)}

n = len(ids)
FP = E.cosine_matrix(R.vectors([R.faceted_text("skeletons_faceted_haiku", i) for i in ids], "tfidf"))

pairs = [(x, y) for x in range(n) for y in range(x + 1, n) if field[ids[x]] != field[ids[y]]]
top = set(sorted(pairs, key=lambda p: -FP[p[0], p[1]])[:N_TWINS])


def agree4(a, b):
    return all(fac[ids[a]].get(c) and fac[ids[a]].get(c) == fac[ids[b]].get(c) for c in CORE)


def is_nm(k):
    return ids[k] in nonmath


# the claim is that a NON-computational paper is not matched to a COMPUTATIONAL one, so exactly one side
# is non-math (a non-math x non-math pair is trivially alike -- both compute nothing -- so it is excluded)
mn = [p for p in pairs if is_nm(p[0]) != is_nm(p[1])]
mn_twins = [p for p in mn if p in top and agree4(*p)]
nn = [p for p in pairs if is_nm(p[0]) and is_nm(p[1])]  # reported only for transparency
nn_twins = [p for p in nn if p in top and agree4(*p)]

print(f"non-math papers (6 NOISE arXiv categories):          {len(nonmath)}")
print(f"total cross-field pairs:                             {len(pairs):,}")
print(f"cross-field non-math x computational pairs:          {len(mn):,}")
print(f"...scored as a cross-field twin:                     {len(mn_twins)}   (fraction {len(mn_twins)/len(mn):.4f})")
print(f"[reference] cross-field non-math x non-math pairs:   {len(nn):,}  (scored as twins: {len(nn_twins)})")
