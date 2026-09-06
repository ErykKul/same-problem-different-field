#!/usr/bin/env python3
"""Score the wild three-arm import-candidacy study offline from the shipped files under datasets/validity/:
wild_3arm_key.json (pairs, arms, ranks, planted-twin flags, corpus meta) and wild_3arm_annotations.json
(three blind LLM judges; prompt in wild_3arm_prompt.md). Reports, per view, the judged precision at
k = 5, 10, 20, 30 (majority of three), per-judge yes counts, a bootstrap CI at k = 30, the seeded view split
into planted twins and unlabeled pairs, Fleiss kappa over all judged pairs, and the ranked confirmed pairs of
the unseeded view. The unseeded view has no recall or AP: the positives among 80k pairs are unknown, so
"precision" there is only what the judges confirmed among the k surfaced pairs. Pairs that contain a paper
from the deliberately non-mathematical set count as not genuine regardless of votes (reported separately).
"""
import json, sys
import numpy as np
V = "datasets/validity"
key = json.load(open(f"{V}/wild_3arm_key.json")); meta, pairs = key["meta"], key["pairs"]
ann = json.load(open(f"{V}/wild_3arm_annotations.json"))["annotators"]
names = [a["annotator"] for a in ann]
votes = {int(j["id"]): [] for j in ann[0]["judgments"]}
for a in ann:
    for j in a["judgments"]: votes[int(j["id"])].append(bool(j["genuine"]))
ids = sorted(int(i) for i in pairs); n_j = len(ann)
maj = {i: sum(votes[i]) > n_j / 2 for i in ids}
def arm(name): return sorted([i for i in ids if name in pairs[str(i)]["arms"]], key=lambda i: pairs[str(i)]["rank"])
def ci(x, B=5000, seed=0):
    rng = np.random.default_rng(seed); x = np.array(x, float); m = [rng.choice(x, len(x)).mean() for _ in range(B)]
    return np.percentile(m, 2.5), np.percentile(m, 97.5)
def line(label, sub):
    if not sub: return
    x = [1.0 if maj[i] else 0.0 for i in sub]; lo, hi = ci(x)
    adj = [1.0 if (maj[i] and not pairs[str(i)]["nonmath_pair"]) else 0.0 for i in sub]
    pj = "/".join(str(sum(votes[i][r] for i in sub)) for r in range(n_j))
    print(f"  {label:36}{len(sub):>4}{np.mean(x):>8.3f}  [{lo:.2f}, {hi:.2f}]  {pj:>10}   nonmath-adjusted {np.mean(adj):.3f} ({sum(pairs[str(i)]['nonmath_pair'] for i in sub)} such pairs)")
def at_k(sub, ks=(5, 10, 20, 30)):
    return "  ".join(f"P@{k}={np.mean([maj[i] for i in sub[:k]]):.2f}" for k in ks if len(sub) >= k)
print(f"wild three-arm study: {n_j} blind judges ({', '.join(names)}), {len(ids)} distinct pairs")
print(f"corpus {meta['corpus']}, skipped STRUCTURE=none {meta['skipped_structure_none']}, pool {meta['pool']}, cross-field pairs {meta['cross_field_pairs']}")
print(f"DETECTION (seeded view): planted twins present {meta['planted_twins_present']}/{meta['planted_twins_total']}, recall of known twins in top 1000 = {meta['recall_at_1000']:.3f}")
print(f"  {'view / subset':36}{'n':>4}{'judged':>8}  {'95% CI':14} {'yes per judge':>10}")
s = arm("seeded"); line("seeded top 30 (planted pairs included)", s)
line("  planted twins", [i for i in s if pairs[str(i)]["planted_twin"]]); line("  unlabeled", [i for i in s if not pairs[str(i)]["planted_twin"]])
u = arm("unseeded"); line("unseeded top 30 (planted pairs excluded)", u)
line("  benchmark paper with wild paper", [i for i in u if pairs[str(i)]["benchmark_a"] != pairs[str(i)]["benchmark_b"]])
line("  wild with wild", [i for i in u if not (pairs[str(i)]["benchmark_a"] or pairs[str(i)]["benchmark_b"])])
line("both-wild top 30 (stricter sub-view)", arm("bothwild")); line("random 30 (chance control)", arm("random"))
print(f"\nDISCOVERY (unseeded view), judged precision at k: {at_k(u)}   | random: {at_k(arm('random'))}")
M = np.array([[sum(votes[i]), n_j - sum(votes[i])] for i in ids]); P_i = ((M ** 2).sum(1) - n_j) / (n_j * (n_j - 1))
p = M.sum(0) / M.sum(); kappa = (P_i.mean() - (p ** 2).sum()) / (1 - (p ** 2).sum())
print(f"Fleiss kappa over all {len(ids)} pairs: {kappa:.3f}")
print("\nunseeded view: confirmed pairs by rank (rank in the planted-excluded ranking; votes of 3):")
for i in u:
    if maj[i]:
        q = pairs[str(i)]; print(f"  #{q['rank_unseeded']:>2} {sum(votes[i])}/3 cos {q['cosine']:.3f}  {q['a']}  <->  {q['b']}")
print("\nseeded view: planted twins in the top 30 NOT confirmed:")
for i in s:
    if pairs[str(i)]["planted_twin"] and not maj[i]: print(f"  {sum(votes[i])}/3  {pairs[str(i)]['a']} <-> {pairs[str(i)]['b']}")
