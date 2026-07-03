#!/usr/bin/env python3
"""Three-distiller robustness comparison (Haiku / Opus / qwen3-14b) on the curated papers carrying all three faceted fingerprints: faceted-full TF-IDF AP per distiller. Run from the package root: python src/distiller_subset.py"""
import sys
import numpy as np
from pathlib import Path
sys.path.insert(0,"."); sys.path.insert(0,"src")
import embed as E, reproduce as R
from sklearn.metrics import average_precision_score
DATA="data"
lab,fld=R.load_labels(),R.load_field()
absr=E.load_rep(DATA,"abstract")
ids0,field,fam=R.corpus("curated",absr,lab,fld)
dirs={"Haiku":"skeletons_faceted_haiku","Opus":"skeletons_v1_opus","Qwen3-14b":"skeletons_faceted_qwen_v3"}
def has(d,i): return Path(f"{DATA}/{d}/{i}.md").exists()
ids=[i for i in ids0 if all(has(d,i) for d in dirs.values())]
N=len(ids); A,B=np.triu_indices(N,1)
fla=np.array([field[ids[a]] for a in A]); flb=np.array([field[ids[b]] for b in B])
cr=fla!=flb
fma=np.array([fam[ids[a]] for a in A],dtype=object); fmb=np.array([fam[ids[b]] for b in B],dtype=object)
pos=((fma!="")&(fma==fmb))[cr].astype(int); A,B=A[cr],B[cr]
print(f"3-distiller-complete subset: {N} papers, {len(A)} cross-field pairs, {int(pos.sum())} twins")
for name,d in dirs.items():
    texts=[R.faceted_text(d,i) for i in ids]
    S=E.cosine_matrix(R.vectors(texts,"tfidf"))
    print(f"  faceted-full [{name:9}] AP {average_precision_score(pos,S[A,B]):.3f}")
