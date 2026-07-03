#!/usr/bin/env python3
"""Facet-operator on the CURATED benchmark (complete labels -> valid precision/recall, not the wild
lower bound). Reports: facet-only AP, the faceted-full retriever AP (sanity = headline), and the
precision/recall frontier as more of the four core facets are required to agree (the tunable operator,
Table tab:frontier in the paper). Needs the ML extras (sentence-transformers) for the per-facet
agreement step. Run from the package root with the ML venv: python src/facet_ops.py"""
import sys
import numpy as np
sys.path.insert(0, "."); sys.path.insert(0, "src")
import embed as E      # noqa: E402
import reproduce as R  # noqa: E402
from distill_faceted import parse_facets  # noqa: E402
from sklearn.metrics import average_precision_score  # noqa: E402

DATA = "data"
ST = "st:sentence-transformers/all-MiniLM-L6-v2"
CORE = ["STRUCTURE", "DATA_OBJECT", "INFERENCE", "PROBLEM_FORM"]
NONE = {"none", "not stated", ""}

lab, fld = R.load_labels(), R.load_field()
absr = E.load_rep(DATA, "abstract")
ids, field, fam = R.corpus("curated", absr, lab, fld)
N = len(ids)
fac = {i: parse_facets(open(f"{DATA}/skeletons_faceted_haiku/{i}.md", encoding="utf-8").read()) for i in ids}
A, B = np.triu_indices(N, 1)
cross = np.array([field[ids[a]] for a in A]) != np.array([field[ids[b]] for b in B])
fa = np.array([fam[ids[a]] for a in A], dtype=object)
fb = np.array([fam[ids[b]] for b in B], dtype=object)
pos = ((fa != "") & (fa == fb))[cross]
A, B = A[cross], B[cross]
P = int(pos.sum())
Rretr = E.cosine_matrix(R.vectors([R.faceted_text("skeletons_faceted_haiku", i) for i in ids], "tfidf"))
mech = Rretr[A, B]
order = np.argsort(-mech)
fonly = [" ".join(f"{f}: {fac[i].get(f, '')}" for f in fac[i] if f != "MECHANISM") for i in ids]
facet_ap = average_precision_score(pos, E.cosine_matrix(R.vectors(fonly, "tfidf"))[A, B])
print(f"curated {N} papers, {len(A)} cross-field pairs, {P} twins (complete labels)")
print(f"facet-only AP (TF-IDF):     {facet_ap:.3f}")
print(f"faceted-full retriever AP:  {average_precision_score(pos, mech):.3f}  (= headline)")
Sfac, isnone = {}, {}
for f in CORE:
    Sfac[f] = E.cosine_matrix(E.embed_texts([fac[i].get(f, "") or "none" for i in ids], ST))
    isnone[f] = np.array([(fac[i].get(f, "") or "").lower().strip() in NONE for i in ids])
AG = {f: (Sfac[f][A, B] >= 0.85) & ~(isnone[f][A] | isnone[f][B]) for f in CORE}
cand = np.zeros(len(A), bool)
cand[order[:min(1000, len(A))]] = True
agc = np.sum([AG[f] for f in CORE], axis=0)
print("\nfacet-frontier (k-of-4 core facets agree, on the top-1000 retrieved; complete-label P/R):")
print(f"  {'k>=':>4} {'precision':>10} {'recall':>8} {'kept':>6}")
for k in range(0, 5):
    keep = cand & (agc >= k)
    kk = int(keep.sum())
    print(f"  {k:>4} {pos[keep].sum()/max(kk,1):>10.3f} {pos[keep].sum()/P:>8.3f} {kk:>6}")
