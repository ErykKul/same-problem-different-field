#!/usr/bin/env python3
"""Domain-stripping ablation on the full 109-paper benchmark (qwen3 distiller): abstract vs keep-domain vs stripped MECHANISM under TF-IDF, MiniLM, and SPECTER, with bootstrap CIs on the domain-stripping gain (which widens under topical embedders). Run from the package root with the ML venv: python src/abl_109.py"""
import sys, numpy as np
from pathlib import Path
sys.path.insert(0,"."); sys.path.insert(0,"src")
import embed as E, reproduce as R
from distill_faceted import parse_facets
from sklearn.metrics import average_precision_score
np.random.seed(0); DATA="data"
lab,fld=R.load_labels(),R.load_field()
absr=E.load_rep(DATA,"abstract")
ids,field,fam=R.corpus("curated",absr,lab,fld)
ids=[i for i in ids if Path(f"{DATA}/skeletons_keepdomain_qwen/{i}.md").exists()
                    and Path(f"{DATA}/skeletons_faceted_qwen_v3/{i}.md").exists()]
N=len(ids); A,B=np.triu_indices(N,1)
cross=np.array([field[ids[a]] for a in A])!=np.array([field[ids[b]] for b in B])
fa=np.array([fam[ids[a]] for a in A],dtype=object); fb=np.array([fam[ids[b]] for b in B],dtype=object)
pos=((fa!="")&(fa==fb))[cross].astype(int); A,B=A[cross],B[cross]
def mech(d,i): return parse_facets(open(f"{DATA}/{d}/{i}.md",encoding="utf-8").read()).get("MECHANISM","") or "none"
arms={"abstract":[absr[i] for i in ids],
      "keep-domain":[mech("skeletons_keepdomain_qwen",i) for i in ids],
      "stripped":[mech("skeletons_faceted_qwen_v3",i) for i in ids]}
embs=[("TF-IDF","tfidf","cos"),("MiniLM","st:sentence-transformers/all-MiniLM-L6-v2","cos"),("SPECTER","st:allenai/specter","cos")]
def simmat(texts,kind,metric):
    V=R.vectors(texts,kind)
    if metric=="euclid":
        sq=(V*V).sum(1); return -np.sqrt(np.maximum(sq[:,None]+sq[None,:]-2*V@V.T,0))
    return E.cosine_matrix(V)
print(f"ablation on {N} papers, {len(A)} cross-field pairs, {int(pos.sum())} twins (qwen3 distiller)")
print(f"{'embedder':10} {'abstract':>9} {'keep-dom':>9} {'stripped':>9}  {'strip-keep (95% CI)':>22}")
for ename,kind,metric in embs:
    S={k:simmat(v,kind,metric).astype(np.float64) for k,v in arms.items()}
    pt={k:average_precision_score(pos,S[k][A,B]) for k in arms}
    Bn=2000; TRIU=np.triu_indices(N,1); boot={k:np.empty(Bn) for k in ("keep-domain","stripped")}
    for b in range(Bn):
        bi=np.random.randint(0,N,N); ii,jj=bi[TRIU[0]],bi[TRIU[1]]
        cr=np.array([field[ids[x]] for x in ii])!=np.array([field[ids[x]] for x in jj]); ic,jc=ii[cr],jj[cr]
        p=((np.array([fam[ids[x]] for x in ic],dtype=object)!="")&(np.array([fam[ids[x]] for x in ic],dtype=object)==np.array([fam[ids[x]] for x in jc],dtype=object))).astype(int)
        if p.sum()==0:
            for k in boot: boot[k][b]=np.nan
            continue
        for k in boot: boot[k][b]=average_precision_score(p,S[k][ic,jc])
    d=boot["stripped"]-boot["keep-domain"]; d=d[~np.isnan(d)]
    lo,hi=np.percentile(d,2.5),np.percentile(d,97.5)
    print(f"{ename:10} {pt['abstract']:9.3f} {pt['keep-domain']:9.3f} {pt['stripped']:9.3f}  +{pt['stripped']-pt['keep-domain']:.3f} [{lo:+.3f},{hi:+.3f}]")
