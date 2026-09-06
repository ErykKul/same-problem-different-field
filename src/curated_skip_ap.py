#!/usr/bin/env python3
"""Curated-benchmark AP as reported (all 109 papers, all 5,812 cross-field pairs) and with only the ten pairs
between the five no-method distractors (STRUCTURE "none") dropped from the ranking, all papers kept. The wild
run's candidate skip would remove those pairs; the benchmark keeps every pair by design, and the paper reports
the unskipped, conservative figures. Run from the package root with the ML venv."""
import os, sys, csv, itertools
from sklearn.metrics import average_precision_score
sys.path.insert(0, "."); sys.path.insert(0, "src")
import embed as E, reproduce as R  # noqa: E402
from distill_faceted import parse_facets  # noqa: E402
NONE = {"", "none", "none.", "not stated", "not stated.", "not applicable", "n/a", "na", "no computation"}
rows = [r for r in csv.DictReader(l for l in open("datasets/mode_a_seed_families.csv") if not l.startswith("#"))]
ids = [r["id"] for r in rows]; field = {r["id"]: r["field"] for r in rows}; role = {r["id"]: r["role"] for r in rows}
fam = {r["id"]: r["family"] for r in rows if r["role"] == "member"}
nomethod = {i for i in ids if role[i] == "distractor" and (parse_facets(open(f"data/skeletons_faceted_haiku/{i}.md", encoding="utf-8").read()).get("STRUCTURE", "") or "").lower().strip() in NONE}
absr = E.load_rep("data", "abstract"); idx = {i: k for k, i in enumerate(ids)}
allpairs = [(a, b) for a, b in itertools.combinations(ids, 2) if field[a] != field[b]]
kept = [(a, b) for a, b in allpairs if not (a in nomethod and b in nomethod)]
twin = lambda a, b: a in fam and b in fam and fam[a] == fam[b]
print(f"no-method distractors: {sorted(nomethod)}")
print(f"cross-field pairs: {len(allpairs)} (as reported) | {len(kept)} with the {len(allpairs) - len(kept)} no-method/no-method pairs dropped; twins {sum(twin(*p) for p in kept)} in both")
for rep, texts in [("abstract+TF-IDF", [absr[i] for i in ids]), ("skeleton+TF-IDF", [R.faceted_text("skeletons_faceted_haiku", i, mech_only=True) for i in ids]), ("whole fingerprint+TF-IDF", [R.faceted_text("skeletons_faceted_haiku", i) for i in ids])]:
    S = E.cosine_matrix(R.vectors(texts, "tfidf"))
    ap = lambda P: average_precision_score([int(twin(*p)) for p in P], [S[idx[a], idx[b]] for a, b in P])
    print(f"  {rep:26} AP as reported {ap(allpairs):.3f} | no-method pairs dropped {ap(kept):.3f}")
