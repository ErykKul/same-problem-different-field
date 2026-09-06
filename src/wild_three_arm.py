#!/usr/bin/env python3
"""Wild three-arm import-candidacy study: build the blind pairs (construct validity, Section 6.2).

The corpus is the 501-paper extended corpus. The operator skips, as candidates, every paper whose skeleton
carries STRUCTURE "none" (no computational pattern was distilled; 80 of 501). All remaining cross-field
pairs are ranked once by the whole-fingerprint TF-IDF cosine. Three views of that one ranking are judged:
  seeded    : the top K pairs as ranked; the benchmark's planted twins may appear (detection view).
  unseeded  : the top K after excluding pairs whose two papers are both benchmark papers, i.e. the pairs
              whose labels we already know (discovery view). A benchmark paper with a wild paper stays.
  random    : K pairs drawn at random from the both-wild pairs below rank 300 (chance control).
A stricter sub-view, bothwild (neither paper from the benchmark), was also judged and is kept in the key.
Pairs are anonymized (field labels + abstracts truncated to 550 chars), deduplicated across views, shuffled,
and judged blind by three LLM annotators reading datasets/validity/wild_3arm_prompt.md. Scoring is offline
(wild_three_arm_score.py). Deterministic (seed 0). Run from the package root with the ML venv.
"""
import os, sys, json, random
from pathlib import Path
import numpy as np
sys.path.insert(0, "."); sys.path.insert(0, "src")
import embed as E      # noqa: E402
import reproduce as R  # noqa: E402
from distill_faceted import parse_facets  # noqa: E402

random.seed(0); np.random.seed(0)
DATA = "data"; K = 30
OUTDIR = os.environ.get("OUTDIR", "datasets/validity")
NONE = {"", "none", "none.", "not stated", "not stated.", "not applicable", "n/a", "na", "no computation"}
NONMATH_PREFIX = ("mc-cs-CY-", "mc-cs-HC-", "mc-cs-DL-", "mc-physics-hist-ph-", "mc-econ-GN-", "mc-cs-SI-")

lab, mfield = R.load_labels(), R.load_field()
absr = E.load_rep(DATA, "abstract")
ref = set(p.stem for p in Path(f"{DATA}/skeletons_faceted_haiku").glob("*.md"))
ids_all = sorted(set(absr) & ref)
fac = {i: parse_facets(open(f"{DATA}/skeletons_faceted_haiku/{i}.md", encoding="utf-8").read()) for i in ids_all}
skipped = {i for i in ids_all if (fac[i].get("STRUCTURE", "") or "").lower().strip() in NONE}
ids = [i for i in ids_all if i not in skipped]
field = {i: (mfield.get(i) or lab.get(i, {}).get("field", "") or "?") for i in ids}
benchmark = {i for i in ids if lab.get(i, {}).get("family")}
member_fam = {i: lab[i]["family"] for i in ids if lab.get(i, {}).get("family") and lab[i].get("role") == "member"}
N = len(ids)
print(f"corpus {len(ids_all)} | skipped (STRUCTURE none) {len(skipped)} | pool {N} | benchmark papers in pool {len(benchmark)}")

S = E.cosine_matrix(R.vectors([R.faceted_text("skeletons_faceted_haiku", i) for i in ids], "tfidf"))
iu, ju = np.triu_indices(N, 1)
fa = np.array([field[ids[a]] for a in iu]); fb = np.array([field[ids[b]] for b in ju])
cross = fa != fb
ic, jc = iu[cross], ju[cross]
sc = S[ic, jc]
order = np.argsort(-sc)
pair = lambda k: (ids[ic[k]], ids[jc[k]])
is_twin = lambda a, b: a in member_fam and b in member_fam and member_fam[a] == member_fam[b]
twins_present = int(sum(is_twin(*pair(k)) for k in order))
recall1000 = sum(is_twin(*pair(k)) for k in order[:1000]) / 210
print(f"cross-field pairs {len(order)} | planted twins present {twins_present}/210 | recall@1000 {recall1000:.3f}")

seeded = list(order[:K])
unseeded_order = [k for k in order if not (pair(k)[0] in benchmark and pair(k)[1] in benchmark)]
unseeded = unseeded_order[:K]
bothwild_order = order[np.array([not (pair(k)[0] in benchmark or pair(k)[1] in benchmark) for k in order])]
bothwild = list(bothwild_order[:K])
rnd = list(np.random.choice(bothwild_order[300:], K, replace=False))

arms = {}
for name, lst in [("seeded", seeded), ("unseeded", unseeded), ("bothwild", bothwild), ("random", rnd)]:
    for k in lst:
        arms.setdefault(int(k), []).append(name)
rank_all = {int(k): r for r, k in enumerate(order, 1)}
rank_unseeded = {int(k): r for r, k in enumerate(unseeded_order, 1)}
uniq = sorted(arms)            # deterministic order before shuffling
random.shuffle(uniq)
pairs_out, key_out = [], {}
for n, k in enumerate(uniq):
    a, b = pair(k)
    pairs_out.append({"id": n, "field_a": field[a], "field_b": field[b],
                      "abstract_a": " ".join(absr[a].split())[:550], "abstract_b": " ".join(absr[b].split())[:550]})
    key_out[str(n)] = {"a": a, "b": b, "arms": arms[k], "rank": rank_all[k],
                       "rank_unseeded": rank_unseeded.get(k), "cosine": round(float(sc[k]), 4),
                       "planted_twin": is_twin(a, b), "benchmark_a": a in benchmark, "benchmark_b": b in benchmark,
                       "nonmath_pair": a.startswith(NONMATH_PREFIX) or b.startswith(NONMATH_PREFIX)}
meta = {"corpus": len(ids_all), "skipped_structure_none": len(skipped), "pool": N, "cross_field_pairs": int(len(order)),
        "planted_twins_present": twins_present, "planted_twins_total": 210, "recall_at_1000": round(float(recall1000), 4),
        "K": K, "nonmath_passing_skip": sum(1 for i in ids if i.startswith(NONMATH_PREFIX))}
os.makedirs(OUTDIR, exist_ok=True)
keyfile = f"{OUTDIR}/wild_3arm_key.json"
if os.path.exists(keyfile) and os.environ.get("CHECK", "1") == "1":
    old = json.load(open(keyfile))["pairs"]
    olds = {frozenset((v["a"], v["b"])) for v in old.values()}
    news = {frozenset((v["a"], v["b"])) for v in key_out.values()}
    assert olds == news, f"regenerated pairs differ from the judged set: {len(olds ^ news)} differences"
    print("regenerated pairs == judged pairs (shipped key)")
    sys.exit(0)
json.dump(pairs_out, open(f"{OUTDIR}/wild_3arm_pairs.json", "w"), indent=1)
json.dump({"meta": meta, "pairs": key_out}, open(keyfile, "w"), indent=1)
print(f"wrote {len(pairs_out)} anonymized pairs + key to {OUTDIR} (seeded {len(seeded)}, unseeded {len(unseeded)}, bothwild {len(bothwild)}, random {len(rnd)})")
