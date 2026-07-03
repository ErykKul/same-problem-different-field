#!/usr/bin/env python3
"""Reproduce the SYSTEM-SURFACING half of the executed imports: the fingerprint links the bespoke-field
paper to the standard-solver paper across fields, where a topical abstract embedder does not. The
execution half is in causal_mc.py (A), kriging_gp.py (B), needleman_wunsch.py (C, wild pair 44).

Run from the package root with the venv:  python src/import_surfacing.py
"""
import sys
from pathlib import Path
import numpy as np
sys.path.insert(0, "."); sys.path.insert(0, "src")
import embed as E      # noqa: E402
import reproduce as R  # noqa: E402

DATA = "data"
lab, mfield = R.load_labels(), R.load_field()
absr = E.load_rep(DATA, "abstract")
ids = sorted(set(absr) & set(p.stem for p in Path(f"{DATA}/skeletons_faceted_haiku").glob("*.md")))
field = {i: (mfield.get(i) or lab.get(i, {}).get("field", "") or "?") for i in ids}
idx = {i: k for k, i in enumerate(ids)}
FP = E.cosine_matrix(R.vectors([R.faceted_text("skeletons_faceted_haiku", i) for i in ids], "tfidf"))
AB = E.cosine_matrix(R.vectors([absr[i] for i in ids], "tfidf"))


def cross_order(seed):
    si = idx[seed]
    return si, [k for k in np.argsort(-FP[si]) if ids[k] != seed and field[ids[k]] != field[seed]]


def rank_of(seed, target):
    _, order = cross_order(seed)
    return next(r for r, k in enumerate(order) if ids[k] == target) + 1


# --- A: political-methodology ideal points -> recommender-systems matrix factorization (strong) ---
si, order = cross_order("pca-polmeth-001")
print("[A causal-panel <- matrix completion]  seed pca-polmeth-001 (political_methodology)")
print("  top cross-field fingerprint neighbors:    fp-cos  abs-cos  field")
for k in order[:5]:
    tag = "  <== import partner (recsys matrix factorization)" if ids[k] == "pca-recsys-001" else ""
    print(f"    {ids[k]:22} {FP[si, k]:.3f}   {AB[si, k]:.3f}   {field[ids[k]]}{tag}")
print(f"  -> partner pca-recsys-001 ranks #{rank_of('pca-polmeth-001','pca-recsys-001')} of {len(order)} "
      f"cross-field; abstract cosine {AB[si, idx['pca-recsys-001']]:.3f} (topical embedder misses it).")

# --- B: the Gaussian-process / kriging core, surfaced as a cross-field CLUSTER ---
gp = [i for i in ids if i.startswith("gp-")]
si, order = cross_order("gp-ml-001")
print("\n[B kriging <- Gaussian process]  the GP core is surfaced as a cross-field cluster.")
print("  machine-learning GP (gp-ml-001) top cross-field neighbors:   fp-cos  field")
for k in order[:4]:
    tag = "  (GP)" if ids[k] in gp else ""
    print(f"    {ids[k]:22} {FP[si, k]:.3f}   {field[ids[k]]}{tag}")
print(f"  geostatistics kriging joins the same core: gp-geo-001 (named) ranks gp-ml at "
      f"#{rank_of('gp-geo-001','gp-ml-001')}, gp-geo-noname-001 (name-free) at "
      f"#{rank_of('gp-geo-noname-001','gp-ml-001')}")
print("  (the deliberately name-free kriging paper is the hardest to place, consistent with the audit).")
