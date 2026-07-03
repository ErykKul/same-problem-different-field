#!/usr/bin/env python3
"""Held-out-family generalization test (addresses the construct-validity / "you only show retrieval
given a twin exists, on families you picked" objection). The headline method (fingerprint + TF-IDF)
is zero-shot; its only corpus-dependent component is the TF-IDF vocabulary/IDF. This leaves each of
the 18 families out in turn, fits the vectorizer on the OTHER 17 families only, transforms all papers
with it, and evaluates P@1 / MRR on the held-out family's queries. If held-out matches the full-fit
reference, the representation does not overfit to the selected family set. Run from the package root."""
import sys
import numpy as np
sys.path.insert(0, ".")
sys.path.insert(0, "src")
import reproduce as R  # noqa: E402
import embed as E      # noqa: E402
from sklearn.feature_extraction.text import TfidfVectorizer  # noqa: E402
from sklearn.metrics.pairwise import cosine_similarity        # noqa: E402

DATA = "data"
lab, fld = R.load_labels(), R.load_field()
absr = E.load_rep(DATA, "abstract")
ids, field, fam = R.corpus("curated", absr, lab, fld)
N = len(ids)
fp = [R.faceted_text("skeletons_faceted_haiku", i) for i in ids]
famv = [fam[i] for i in ids]
fieldv = [field[i] for i in ids]
families = sorted(set(f for f in famv if f))


def eval_queries(S, qmask):
    np.fill_diagonal(S, -2.0)
    p1, rr = [], []
    for q in range(N):
        if not qmask[q] or not famv[q]:
            continue
        cand = [k for k in np.argsort(-S[q]) if fieldv[k] != fieldv[q]]
        if not any(famv[k] == famv[q] for k in cand):
            continue
        p1.append(1.0 if famv[cand[0]] == famv[q] else 0.0)
        rank = next(r for r, k in enumerate(cand) if famv[k] == famv[q]) + 1
        rr.append(1.0 / rank)
    return p1, rr


Sfull = cosine_similarity(TfidfVectorizer().fit_transform(fp))
p1f, rrf = eval_queries(Sfull, [True] * N)
print(f"FULL  fingerprint+TF-IDF (vocabulary fit on all 18 families): "
      f"P@1={np.mean(p1f):.3f} MRR={np.mean(rrf):.3f}  ({len(p1f)} queries)")

p1h, rrh = [], []
for f in families:
    train = [fp[k] for k in range(N) if famv[k] != f]
    S = cosine_similarity(TfidfVectorizer().fit(train).transform(fp))
    p1, rr = eval_queries(S, [famv[k] == f for k in range(N)])
    p1h += p1
    rrh += rr
print(f"HELD-OUT  (leave-one-family-out; the vocabulary never sees the test family): "
      f"P@1={np.mean(p1h):.3f} MRR={np.mean(rrh):.3f}  ({len(p1h)} held-out queries)")
print(f"  delta vs full: P@1 {np.mean(p1h)-np.mean(p1f):+.3f}, MRR {np.mean(rrh)-np.mean(rrf):+.3f}")
