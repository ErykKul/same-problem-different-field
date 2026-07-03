#!/usr/bin/env python3
"""Fingerprint AP with the DOMAIN facet ablated, showing the headline is not topical leakage from the recall-floor field label. Run from the package root: python src/nodomain.py"""
import sys, numpy as np
sys.path.insert(0,"."); sys.path.insert(0,"src")
import embed as E, reproduce as R
from distill_faceted import parse_facets
from sklearn.metrics import average_precision_score
DATA="data"
lab,fld=R.load_labels(),R.load_field()
absr=E.load_rep(DATA,"abstract")
ids,field,fam=R.corpus("curated",absr,lab,fld)
N=len(ids); A,B=np.triu_indices(N,1)
cross=np.array([field[ids[a]] for a in A])!=np.array([field[ids[b]] for b in B])
fa=np.array([fam[ids[a]] for a in A],dtype=object); fb=np.array([fam[ids[b]] for b in B],dtype=object)
pos=((fa!="")&(fa==fb))[cross]; A,B=A[cross],B[cross]
def ap(texts): return average_precision_score(pos, E.cosine_matrix(R.vectors(texts,"tfidf"))[A,B])
def rebuild(i, drop=()):
    f=parse_facets(open(f"{DATA}/skeletons_faceted_haiku/{i}.md",encoding="utf-8").read())
    return " ".join(f"{k}: {v}" for k,v in f.items() if k not in drop)
print(f"canonical faceted_text (ref):     {ap([R.faceted_text('skeletons_faceted_haiku',i) for i in ids]):.3f}")
print(f"fingerprint, parse+rejoin (DOMAIN in):  {ap([rebuild(i) for i in ids]):.3f}")
print(f"fingerprint MINUS DOMAIN:               {ap([rebuild(i, drop=('DOMAIN',)) for i in ids]):.3f}")
print(f"DOMAIN facet ALONE:                     {ap([parse_facets(open(f'{DATA}/skeletons_faceted_haiku/{i}.md',encoding='utf-8').read()).get('DOMAIN','') or 'none' for i in ids]):.3f}")
