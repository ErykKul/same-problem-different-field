#!/usr/bin/env python3
"""Curated-benchmark AP with and without the operator's candidate skip (STRUCTURE "none" papers removed).
The paper reports the unskipped, conservative figures; this prints both. Run from the package root with the ML venv."""
import os, sys, csv, itertools
from sklearn.metrics import average_precision_score
sys.path.insert(0, "."); sys.path.insert(0, "src")
import embed as E, reproduce as R  # noqa: E402
from distill_faceted import parse_facets  # noqa: E402
NONE = {"", "none", "none.", "not stated", "not stated.", "not applicable", "n/a", "na", "no computation"}
rows = [r for r in csv.DictReader(l for l in open("datasets/mode_a_seed_families.csv") if not l.startswith("#"))]
ids_all = [r["id"] for r in rows]; field = {r["id"]: r["field"] for r in rows}; role = {r["id"]: r["role"] for r in rows}
fam = {r["id"]: r["family"] for r in rows if r["role"] == "member"}
skip = {i for i in ids_all if (parse_facets(open(f"data/skeletons_faceted_haiku/{i}.md", encoding="utf-8").read()).get("STRUCTURE", "") or "").lower().strip() in NONE}
absr = E.load_rep("data", "abstract")
def ap(ids, texts):
    S = E.cosine_matrix(R.vectors(texts, "tfidf")); idx = {i: k for k, i in enumerate(ids)}
    pairs = [(a, b) for a, b in itertools.combinations(ids, 2) if field[a] != field[b]]
    y = [int(a in fam and b in fam and fam[a] == fam[b]) for a, b in pairs]
    return average_precision_score(y, [S[idx[a], idx[b]] for a, b in pairs]), len(pairs), sum(y)
print(f"skip removes {len(skip)} curated papers: {sorted(skip)} (roles: {[role[i] for i in sorted(skip)]})")
for label, ids in [("all 109 papers (as reported)", ids_all), ("candidate skip applied", [i for i in ids_all if i not in skip])]:
    a_fp, n, t = ap(ids, [R.faceted_text("skeletons_faceted_haiku", i) for i in ids]); a_sk, _, _ = ap(ids, [R.faceted_text("skeletons_faceted_haiku", i, mech_only=True) for i in ids]); a_ab, _, _ = ap(ids, [absr[i] for i in ids])
    print(f"{label:32} papers {len(ids)}, cross-field pairs {n}, twins {t}: AP abstract+TF-IDF {a_ab:.3f} | skeleton+TF-IDF {a_sk:.3f} | whole fingerprint+TF-IDF {a_fp:.3f}")
