import sys, numpy as np
sys.path.insert(0,"."); sys.path.insert(0,"src")
import embed as E, reproduce as R
from sklearn.metrics import average_precision_score
DATA="data"
lab,fld=R.load_labels(),R.load_field()
absr=E.load_rep(DATA,"abstract")
ids,field,fam=R.corpus("curated",absr,lab,fld)
EXCL={"inverse_ising_potts","hawkes_self_exciting","optimal_transport"}
def ap(idset):
    n=len(idset); A,B=np.triu_indices(n,1)
    fl=np.array([field[idset[a]] for a in A])!=np.array([field[idset[b]] for b in B])
    fa=np.array([fam[idset[a]] for a in A],dtype=object); fb=np.array([fam[idset[b]] for b in B],dtype=object)
    pos=((fa!="")&(fa==fb))[fl]; A2,B2=A[fl],B[fl]
    S=E.cosine_matrix(R.vectors([R.faceted_text("skeletons_faceted_haiku",i) for i in idset],"tfidf"))
    return average_precision_score(pos,S[A2,B2]),int(pos.sum()),n
af,tf,nf=ap(ids)
ids2=[i for i in ids if fam[i] not in EXCL]
ae,te,ne=ap(ids2)
print(f"full:            {nf} papers, {tf} twins, fingerprint+TF-IDF AP {af:.3f}")
print(f"excl 3 n=2 fams: {ne} papers, {te} twins, fingerprint+TF-IDF AP {ae:.3f}")
