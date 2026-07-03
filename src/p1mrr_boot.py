#!/usr/bin/env python3
"""Paired bootstrap (over queries) of the abstract->skeleton P@1/MRR swap on the curated benchmark. Run from the package root: python src/p1mrr_boot.py"""
import sys
import numpy as np
sys.path.insert(0,"."); sys.path.insert(0,"src")
import embed as E, reproduce as R
np.random.seed(0)
DATA="data"
lab,fld=R.load_labels(),R.load_field()
absr=E.load_rep(DATA,"abstract")
ids,field,fam=R.corpus("curated",absr,lab,fld)
N=len(ids)
reps={"abstract":[absr[i] for i in ids],
      "skeleton":[R.faceted_text("skeletons_faceted_haiku",i,mech_only=True) for i in ids]}
def perq(texts):
    S=E.cosine_matrix(R.vectors(texts,"tfidf")); np.fill_diagonal(S,-2)
    q_idx=[]; p1=[]; rr=[]
    for q in range(N):
        if not fam[ids[q]]: continue
        cand=[k for k in np.argsort(-S[q]) if field[ids[k]]!=field[ids[q]]]
        if not any(fam[ids[k]]==fam[ids[q]] for k in cand): continue
        q_idx.append(q)
        p1.append(1.0 if fam[ids[cand[0]]]==fam[ids[q]] else 0.0)
        rank=next(r for r,k in enumerate(cand) if fam[ids[k]]==fam[ids[q]])+1
        rr.append(1.0/rank)
    return np.array(q_idx),np.array(p1),np.array(rr)
qa,p1a,rra=perq(reps["abstract"]); qs,p1s,rrs=perq(reps["skeleton"])
# align on common queries (both must have a twin under each rep -> same set: queries with a twin)
common=sorted(set(qa)&set(qs))
ia={q:k for k,q in enumerate(qa)}; iss={q:k for k,q in enumerate(qs)}
P1a=np.array([p1a[ia[q]] for q in common]); P1s=np.array([p1s[iss[q]] for q in common])
RRa=np.array([rra[ia[q]] for q in common]); RRs=np.array([rrs[iss[q]] for q in common])
Q=len(common)
print(f"queries with a twin: {Q}")
print(f"abstract P@1={P1a.mean():.3f} MRR={RRa.mean():.3f} | skeleton P@1={P1s.mean():.3f} MRR={RRs.mean():.3f}")
B=2000; dP=np.empty(B); dM=np.empty(B)
for b in range(B):
    s=np.random.randint(0,Q,Q)
    dP[b]=P1s[s].mean()-P1a[s].mean(); dM[b]=RRs[s].mean()-RRa[s].mean()
print(f"skeleton - abstract  MRR +{(RRs-RRa).mean():.3f} [{np.percentile(dM,2.5):+.3f},{np.percentile(dM,97.5):+.3f}]")
print(f"skeleton - abstract  P@1 +{(P1s-P1a).mean():.3f} [{np.percentile(dP,2.5):+.3f},{np.percentile(dP,97.5):+.3f}]")
