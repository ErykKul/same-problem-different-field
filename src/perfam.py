#!/usr/bin/env python3
"""Per-family cross-domain P@1 (skeleton+TF-IDF) on the curated benchmark (the '17 of 18 families exceed P@1 0.5' result). Run from the package root: python src/perfam.py"""
import sys
from pathlib import Path
import numpy as np
sys.path.insert(0,"."); sys.path.insert(0,"src")
import embed as E, reproduce as R
DATA="data"
lab,fld=R.load_labels(),R.load_field()
absr=E.load_rep(DATA,"abstract")
ids,field,fam=R.corpus("curated",absr,lab,fld)
N=len(ids); idx={i:k for k,i in enumerate(ids)}
S=E.cosine_matrix(R.vectors([R.faceted_text("skeletons_faceted_haiku",i,mech_only=True) for i in ids],"tfidf"))
np.fill_diagonal(S,-1)
fams={}
for i in ids:
    if fam[i]: fams.setdefault(fam[i],[]).append(i)
nfam=0; npass=0
for f,mem in sorted(fams.items()):
    hits=0; tot=0
    for i in mem:
        si=idx[i]
        # nearest cross-field neighbor
        order=[k for k in np.argsort(-S[si]) if field[ids[k]]!=field[i]]
        if not order: continue
        tot+=1; hits+= 1 if fam[ids[order[0]]]==f else 0
    p1=hits/tot if tot else 0
    nfam+=1; npass+= 1 if p1>0.5 else 0
    print(f"  {f:28} n={len(mem)} P@1={p1:.2f}")
print(f"FAMILIES: {npass} of {nfam} exceed cross-domain P@1 0.5")
