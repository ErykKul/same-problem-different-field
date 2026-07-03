#!/usr/bin/env python3
"""The full representation x embedder AP grid (abstract/skeleton/fingerprint x TF-IDF/MiniLM/SPECTER/SciNCL/SemCSE/Qwen3-Emb) on the curated benchmark = paper Table tab:grid; E5-large-v2 column via e5_grid.py. Run from the package root with the ML venv: python src/full_grid.py"""
import sys
from pathlib import Path
import numpy as np
sys.path.insert(0,"."); sys.path.insert(0,"src")
import embed as E, reproduce as R
from sklearn.metrics import average_precision_score
DATA="data"
lab,fld=R.load_labels(),R.load_field()
absr=E.load_rep(DATA,"abstract")
ids,field,fam=R.corpus("curated",absr,lab,fld)
N=len(ids)
A,B=np.triu_indices(N,1)
fa=np.array([field[ids[a]] for a in A]); fb=np.array([field[ids[b]] for b in B])
cr=fa!=fb
fma=np.array([fam[ids[a]] for a in A],dtype=object); fmb=np.array([fam[ids[b]] for b in B],dtype=object)
pos=((fma!="")&(fma==fmb))[cr].astype(int)
A,B=A[cr],B[cr]
print(f"{N} papers, {len(A)} cross-field pairs, {pos.sum()} twins")
reps={"abstract":[absr[i] for i in ids],
      "skeleton":[R.faceted_text("skeletons_faceted_haiku",i,mech_only=True) for i in ids],
      "fingerprint":[R.faceted_text("skeletons_faceted_haiku",i) for i in ids]}
embs=[("TF-IDF","tfidf","cos"),("MiniLM","st:sentence-transformers/all-MiniLM-L6-v2","cos"),
      ("SPECTER","st:allenai/specter","cos"),("SciNCL","st:malteos/scincl","cos"),
      ("SemCSE","semcse","euclid"),("Qwen3-Emb","qwen3","cos")]
def ap(texts,kind,metric):
    V=R.vectors(texts,kind)
    if metric=="euclid":
        sq=(V*V).sum(1); S=-np.sqrt(np.maximum(sq[:,None]+sq[None,:]-2*V@V.T,0))
    else: S=E.cosine_matrix(V)
    return average_precision_score(pos,S[A,B])
print(f"\n{'rep':12}"+"".join(f"{e[0]:>11}" for e in embs))
for rname,rtexts in reps.items():
    row=[]
    for ename,kind,metric in embs:
        try: row.append(f"{ap(rtexts,kind,metric):.3f}")
        except Exception as ex: row.append(f"ERR")
    print(f"{rname:12}"+"".join(f"{v:>11}" for v in row))
