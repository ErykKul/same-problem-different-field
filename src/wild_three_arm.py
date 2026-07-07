#!/usr/bin/env python3
"""Three-arm wild import-candidacy precision (the construct-validity / non-circularity test).

Builds three pools of cross-field pairs from the 501-paper wild corpus, for a BLIND LLM annotation:
  ARM 1  system top-k  : the whole-fingerprint distance's top-K cross-field pairs.
  ARM 2  random        : K random cross-field pairs (the chance / base-rate control).
  ARM 3  collision     : K hard negatives -- cross-field pairs that agree on EXACTLY ONE core facet
                         (STRUCTURE / DATA_OBJECT / INFERENCE / PROBLEM_FORM) but are NOT in the top,
                         i.e. what a shallow one-facet structural matcher would surface and the full
                         operator down-ranks.
The claim the arms license: the system's top wild pairs are genuine cross-domain import candidates at a
precision far above BOTH a random control (rules out chance) AND a single-facet control (rules out the
"any one shared facet looks like a twin" confound), which is discriminative validity on the uncurated
pool, not re-finding planted twins.

Reproducible: deterministic sampling (seed 0). Writes the anonymized pairs (annotator input, arm-blind)
and the arm key. The blind annotation (3 LLM annotators) and the precision/bootstrap-CI computation are
separate steps (wild_three_arm_score.py). Run from the package root with the ML venv.
"""
import os, sys, json, random
from pathlib import Path
import numpy as np
sys.path.insert(0, "."); sys.path.insert(0, "src")
import embed as E      # noqa: E402
import reproduce as R  # noqa: E402
from distill_faceted import parse_facets  # noqa: E402

random.seed(0); np.random.seed(0)
DATA = "data"
CORE = ["STRUCTURE", "DATA_OBJECT", "INFERENCE", "PROBLEM_FORM"]
NONE = {"", "none", "none.", "not stated", "not stated.", "not applicable", "n/a", "na", "no computation"}
S_DIR = os.environ.get("SCRATCH_DIR", "reproduce_out")
OUT, KEYOUT = f"{S_DIR}/wild_3arm_pairs.json", f"{S_DIR}/wild_3arm_key.json"
K = 30

lab, mfield = R.load_labels(), R.load_field()
absr = E.load_rep(DATA, "abstract")
ref = set(p.stem for p in Path(f"{DATA}/skeletons_faceted_haiku").glob("*.md"))
ids = sorted(set(absr) & ref)
field = {i: (mfield.get(i) or lab.get(i, {}).get("field", "") or "?") for i in ids}
fac = {i: parse_facets(open(f"{DATA}/skeletons_faceted_haiku/{i}.md", encoding="utf-8").read()) for i in ids}
N = len(ids)
print(f"wild corpus: {N} papers")

texts = [R.faceted_text("skeletons_faceted_haiku", i) for i in ids]
S = E.cosine_matrix(R.vectors(texts, "tfidf"))
iu, ju = np.triu_indices(N, 1)
fa = np.array([field[ids[a]] for a in iu]); fb = np.array([field[ids[b]] for b in ju])
cross = fa != fb
ic, jc = iu[cross], ju[cross]
sc = S[ic, jc]
order = np.argsort(-sc)

top = order[:K]
rnd = np.random.choice(order[300:], K, replace=False)


def n_core_agree(a, b):
    n = 0
    for f in CORE:
        va = (fac[a].get(f, "") or "").lower().strip()
        vb = (fac[b].get(f, "") or "").lower().strip()
        if va not in NONE and va == vb:
            n += 1
    return n


# single-facet collisions: the HIGHEST-similarity cross-field pairs (below the top) that agree on
# EXACTLY ONE core facet -- the confusable hard negatives a shallow one-facet matcher would surface.
cand = [k for k in order[K:] if n_core_agree(ids[ic[k]], ids[jc[k]]) == 1]
coll = cand[:K]
print(f"top sim {sc[top[0]]:.3f}..{sc[top[-1]]:.3f} | random sim ~{sc[rnd].mean():.3f} | "
      f"collision sim ~{sc[coll].mean():.3f} ({len(cand)} single-facet candidates)")


def info(k):
    a, b = ids[ic[k]], ids[jc[k]]
    return {"a": a, "b": b, "fa": field[a], "fb": field[b],
            "abs_a": " ".join(absr[a].split())[:550], "abs_b": " ".join(absr[b].split())[:550]}


arms = ([("top", info(k)) for k in top] + [("random", info(k)) for k in rnd] + [("collision", info(k)) for k in coll])
random.shuffle(arms)
json.dump([{"id": n, "field_a": p["fa"], "field_b": p["fb"], "abstract_a": p["abs_a"], "abstract_b": p["abs_b"]}
           for n, (t, p) in enumerate(arms)], open(OUT, "w"), indent=1)
json.dump({str(n): {"arm": t, "a": p["a"], "b": p["b"]} for n, (t, p) in enumerate(arms)}, open(KEYOUT, "w"), indent=1)
print(f"top {len(top)} | random {len(rnd)} | collision {len(coll)} -> {len(arms)} anonymized pairs")
print(f"wrote {OUT} + {KEYOUT}")
