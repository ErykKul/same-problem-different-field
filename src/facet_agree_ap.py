#!/usr/bin/env python3
"""Curated facet-agreement AP (raw count + log-LR-weighted): the 'facet classification alone is the weakest signal' number in the paper. Run from the package root with the ML venv: python src/facet_agree_ap.py"""
import sys, numpy as np
sys.path.insert(0,"."); sys.path.insert(0,"src")
import embed as E, reproduce as R
from distill_faceted import parse_facets
from sklearn.metrics import average_precision_score
DATA="data"; ST="st:sentence-transformers/all-MiniLM-L6-v2"
CORE=["STRUCTURE","DATA_OBJECT","INFERENCE","PROBLEM_FORM"]
ALLF=["DOMAIN","STRUCTURE","DATA_OBJECT","INFERENCE","PROBLEM_FORM","DISTRIBUTION","COMPLEXITY"]
NONE={"none","not stated",""}
lab,fld=R.load_labels(),R.load_field()
absr=E.load_rep(DATA,"abstract")
ids,field,fam=R.corpus("curated",absr,lab,fld)
N=len(ids)
fac={i:parse_facets(open(f"{DATA}/skeletons_faceted_haiku/{i}.md",encoding="utf-8").read()) for i in ids}
A,B=np.triu_indices(N,1)
cross=np.array([field[ids[a]] for a in A])!=np.array([field[ids[b]] for b in B])
fa=np.array([fam[ids[a]] for a in A],dtype=object); fb=np.array([fam[ids[b]] for b in B],dtype=object)
pos=((fa!="")&(fa==fb))[cross]; A,B=A[cross],B[cross]
fonly=[" ".join(f"{f}: {fac[i].get(f,'')}" for f in fac[i] if f!="MECHANISM") for i in ids]
ap_tfidf=average_precision_score(pos, E.cosine_matrix(R.vectors(fonly,"tfidf"))[A,B])
def agmat(faclist):
    AG=np.zeros(len(A)); cols=[]
    for f in faclist:
        S=E.cosine_matrix(E.embed_texts([fac[i].get(f,"") or "none" for i in ids],ST))
        isnone=np.array([(fac[i].get(f,"") or "").lower().strip() in NONE for i in ids])
        ag=((S[A,B]>=0.85)&~(isnone[A]|isnone[B])).astype(float); cols.append((f,ag)); AG=AG+ag
    return AG,cols
def loglr(cols):
    sc=np.zeros(len(A))
    for f,ag in cols:
        p1=ag[pos==1].mean()+1e-3; p0=ag[pos==0].mean()+1e-3
        sc=sc+np.log(p1/p0)*ag
    return sc
AGc,colc=agmat(CORE); AGa,cola=agmat(ALLF)
print(f"curated {N}, {len(A)} cross-field pairs, {int(pos.sum())} twins")
print(f"(a) facet-only TF-IDF AP:             {ap_tfidf:.3f}   <- facet block as plain TF-IDF (0.449)")
print(f"(b) raw agreement-count AP (4 core):  {average_precision_score(pos,AGc):.3f}")
print(f"(b) raw agreement-count AP (7 all):   {average_precision_score(pos,AGa):.3f}")
print(f"(c) log-LR-weighted AP (4 core):      {average_precision_score(pos,loglr(colc)):.3f}")
print(f"(c) log-LR-weighted AP (7 all):       {average_precision_score(pos,loglr(cola)):.3f}")
print(f"reference: skeleton+TFIDF 0.513, fingerprint+TFIDF 0.557 (so 'weakest' must be < 0.513)")
