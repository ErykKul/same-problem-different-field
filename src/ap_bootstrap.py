#!/usr/bin/env python3
"""Paired bootstrap CIs for the curated-benchmark AP, resampling the curated papers with
replacement (cluster bootstrap), fixed representation. Run from the package root with the ML venv (loads the SOTA embedders) or the plain venv for the TF-IDF rows.
For each resample: rebuild cross-field pairs among the resampled papers, recompute pooled AP
per method on the SAME resample (paired). Reports each method's AP [2.5,97.5] and the
fingerprint-vs-baseline AP difference + 95% CI + two-sided p."""
import sys
import numpy as np
sys.path.insert(0, ".")
sys.path.insert(0, "src")
import embed as E          # noqa: E402
import reproduce as R      # noqa: E402
from sklearn.metrics import average_precision_score  # noqa: E402

np.random.seed(0)
DATA = "data"

lab, mfield = R.load_labels(), R.load_field()
absr = E.load_rep(DATA, "abstract")
ids, fld, fam = R.corpus("curated", absr, lab, mfield)
N = len(ids)
field = np.array([fld[i] for i in ids])
family = np.array([fam[i] for i in ids], dtype=object)
abst = [absr[i] for i in ids]
print(f"curated: {N} papers")

methods = [
    ("abstract + TF-IDF",   "tfidf", "cos", abst),
    ("SPECTER",             "st:allenai/specter", "cos", abst),
    ("SciNCL",              "st:malteos/scincl", "cos", abst),
    ("SemCSE",              "semcse", "euclid", abst),
    ("Qwen3-Embedding",     "qwen3", "cos", abst),
    ("E5-large-v2",         "st:intfloat/e5-large-v2", "cos", abst),
    ("skeleton + TF-IDF",   "tfidf", "cos", [R.faceted_text("skeletons_faceted_haiku", i, mech_only=True) for i in ids]),
    ("fingerprint + TF-IDF", "tfidf", "cos", [R.faceted_text("skeletons_faceted_haiku", i) for i in ids]),
]
names = [m[0] for m in methods]


def full_sim(kind, metric, texts):
    V = R.vectors(texts, kind)
    if metric == "euclid":
        sq = (V * V).sum(1)
        return -np.sqrt(np.maximum(sq[:, None] + sq[None, :] - 2 * V @ V.T, 0.0))
    return E.cosine_matrix(V)


S = {name: full_sim(kind, metric, texts).astype(np.float64) for name, kind, metric, texts in methods}

iu, ju = np.triu_indices(N, 1)
cr0 = field[iu] != field[ju]
pos0 = ((family[iu] != "") & (family[iu] == family[ju]))[cr0].astype(int)
point = {n: average_precision_score(pos0, S[n][iu[cr0], ju[cr0]]) for n in names}
print(f"\npoint AP (check vs reproduce.py): {len(pos0)} cross-field pairs, {pos0.sum()} twins")
for n in names:
    print(f"  {n:22} {point[n]:.3f}")

Bn = 2000
TRIU = np.triu_indices(N, 1)
boot = {n: np.empty(Bn) for n in names}
for b in range(Bn):
    bi = np.random.randint(0, N, N)
    ii, jj = bi[TRIU[0]], bi[TRIU[1]]
    cr = field[ii] != field[jj]
    ic, jc = ii[cr], jj[cr]
    pos = ((family[ic] != "") & (family[ic] == family[jc])).astype(int)
    if pos.sum() == 0:
        for n in names:
            boot[n][b] = np.nan
        continue
    for n in names:
        boot[n][b] = average_precision_score(pos, S[n][ic, jc])


def ci(x):
    x = x[~np.isnan(x)]
    return np.percentile(x, 2.5), np.percentile(x, 97.5)


print(f"\nper-method AP [95% CI] (paper bootstrap over papers, B={Bn}):")
for n in names:
    lo, hi = ci(boot[n])
    print(f"  {n:22} {point[n]:.3f}  [{lo:.3f}, {hi:.3f}]")

print("\nfingerprint+TF-IDF vs each (paired AP difference [95% CI], two-sided p):")
fp = boot["fingerprint + TF-IDF"]
for n in names:
    if n == "fingerprint + TF-IDF":
        continue
    d = (fp - boot[n])
    d = d[~np.isnan(d)]
    lo, hi = np.percentile(d, 2.5), np.percentile(d, 97.5)
    p = 2 * min((d <= 0).mean(), (d >= 0).mean())
    print(f"  vs {n:22} +{point['fingerprint + TF-IDF'] - point[n]:.3f}  [{lo:+.3f}, {hi:+.3f}]  p={p:.4f}")
