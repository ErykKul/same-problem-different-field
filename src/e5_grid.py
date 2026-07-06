#!/usr/bin/env python3
"""E5-large-v2 baseline (query prefix, its best retrieval config) on the curated benchmark: abstract / skeleton / fingerprint AP under E5. Run from the package root with the ML venv: python src/e5_grid.py"""
import sys, numpy as np
sys.path.insert(0,"."); sys.path.insert(0,"src")
import embed as E, reproduce as R
from sklearn.metrics import average_precision_score
DATA="data"; MODEL="st:intfloat/e5-large-v2"
lab,fld=R.load_labels(),R.load_field()
absr=E.load_rep(DATA,"abstract")
ids,field,fam=R.corpus("curated",absr,lab,fld)
N=len(ids); A,B=np.triu_indices(N,1)
cross=np.array([field[ids[a]] for a in A])!=np.array([field[ids[b]] for b in B])
fa=np.array([fam[ids[a]] for a in A],dtype=object); fb=np.array([fam[ids[b]] for b in B],dtype=object)
pos=((fa!="")&(fa==fb))[cross]; A,B=A[cross],B[cross]
def ap(texts):  # e5 retrieval convention: "query: " prefix on both sides (symmetric)
    V=E.embed_texts(texts, MODEL)  # embed.py adds the E5 query prefix
    return average_precision_score(pos, E.cosine_matrix(V)[A,B])
reps={"abstract":[absr[i] for i in ids],
      "skeleton":[R.faceted_text("skeletons_faceted_haiku",i,mech_only=True) for i in ids],
      "fingerprint":[R.faceted_text("skeletons_faceted_haiku",i) for i in ids]}
print(f"E5-large-v2 on curated {N} (query-prefix). reference: fingerprint+TFIDF 0.557, abstract+TFIDF 0.222")
for r,t in reps.items(): print(f"  E5-large-v2  {r:12} AP {ap(t):.3f}",flush=True)
