#!/usr/bin/env python3
"""SPECTER2 (allenai/specter2_base + proximity adapter) run LOCALLY on the full curated 109,
so the standard scientific-document embedder is evaluated on the same corpus as every other
baseline (no Semantic Scholar API, no 65-paper coverage gap). Embedding = [CLS] of the last
hidden state, per the SPECTER2 model card. Run from the package root:  python src/specter2_local.py"""
import sys
import numpy as np
import torch
sys.path.insert(0, ".")
sys.path.insert(0, "src")
import embed as E          # noqa: E402
import reproduce as R      # noqa: E402
from sklearn.metrics import average_precision_score  # noqa: E402
from transformers import AutoTokenizer               # noqa: E402
from adapters import AutoAdapterModel                # noqa: E402

DATA = "data"
lab, fld = R.load_labels(), R.load_field()
absr = E.load_rep(DATA, "abstract")
ids, field, fam = R.corpus("curated", absr, lab, fld)
N = len(ids)
A, B = np.triu_indices(N, 1)
cross = np.array([field[ids[a]] for a in A]) != np.array([field[ids[b]] for b in B])
fa = np.array([fam[ids[a]] for a in A], dtype=object)
fb = np.array([fam[ids[b]] for b in B], dtype=object)
pos = ((fa != "") & (fa == fb))[cross]
A, B = A[cross], B[cross]

tok = AutoTokenizer.from_pretrained("allenai/specter2_base")
model = AutoAdapterModel.from_pretrained("allenai/specter2_base")
_adapter = model.load_adapter("allenai/specter2", source="hf", set_active=True)
model.set_active_adapters(_adapter)
model.eval()
print(f"SPECTER2 active adapter: {model.active_adapters}", file=sys.stderr)


def embed(texts):
    out = []
    for i in range(0, len(texts), 16):
        batch = texts[i:i + 16]
        inp = tok(batch, padding=True, truncation=True, max_length=512, return_tensors="pt")
        with torch.no_grad():
            out.append(model(**inp).last_hidden_state[:, 0, :].numpy())
    return np.vstack(out)


def ap(texts):
    V = embed(texts)
    return average_precision_score(pos, E.cosine_matrix(V)[A, B])


reps = {
    "abstract":    [absr[i] for i in ids],
    "skeleton":    [R.faceted_text("skeletons_faceted_haiku", i, mech_only=True) for i in ids],
    "fingerprint": [R.faceted_text("skeletons_faceted_haiku", i) for i in ids],
}
print(f"SPECTER2 (local model + proximity adapter) on curated {N}, {len(pos)} cross-field pairs, "
      f"{int(pos.sum())} twins")
print("reference: abstract+TF-IDF 0.253, fingerprint+TF-IDF 0.565")
for r, t in reps.items():
    print(f"  SPECTER2  {r:12} AP {ap(t):.3f}", flush=True)

# paired cluster bootstrap (over papers, B=2000) of fingerprint+TF-IDF vs SPECTER2 (abstract)
Ss2 = E.cosine_matrix(embed(reps["abstract"]))
Sfp = E.cosine_matrix(R.vectors(reps["fingerprint"], "tfidf"))
farr = np.array([field[i] for i in ids])
famarr = np.array([fam[i] for i in ids], dtype=object)
np.random.seed(0)
TRIU = np.triu_indices(N, 1)
Bn = 2000
bf = np.empty(Bn)
bs = np.empty(Bn)
for b in range(Bn):
    bi = np.random.randint(0, N, N)
    ii, jj = bi[TRIU[0]], bi[TRIU[1]]
    cr = farr[ii] != farr[jj]
    ic, jc = ii[cr], jj[cr]
    p = ((famarr[ic] != "") & (famarr[ic] == famarr[jc])).astype(int)
    if p.sum() == 0:
        bf[b] = bs[b] = np.nan
        continue
    bf[b] = average_precision_score(p, Sfp[ic, jc])
    bs[b] = average_precision_score(p, Ss2[ic, jc])
d = bf - bs
d = d[~np.isnan(d)]
pt = average_precision_score(pos, Sfp[A, B]) - average_precision_score(pos, Ss2[A, B])
pval = 2 * min((d <= 0).mean(), (d >= 0).mean())
print(f"fingerprint+TF-IDF vs SPECTER2 (abstract): +{pt:.3f} "
      f"[{np.percentile(d, 2.5):+.3f}, {np.percentile(d, 97.5):+.3f}]  p={pval:.4f}")
