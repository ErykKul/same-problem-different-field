#!/usr/bin/env python3
"""Skip rule report: the operator skips, as retrieval candidates, every paper whose skeleton carries
STRUCTURE "none" (no computational pattern was distilled). Reports how many of the 501 are skipped, how
many of the 64 deliberately non-mathematical papers the rule catches, how many pass, and whether any
passing non-mathematical paper reaches the judged top lists (datasets/validity/wild_3arm_key.json).
Run from the package root."""
import glob, json, os, sys
sys.path.insert(0, "."); sys.path.insert(0, "src")
from distill_faceted import parse_facets  # noqa: E402
NONE = {"", "none", "none.", "not stated", "not stated.", "not applicable", "n/a", "na", "no computation"}
NONMATH_PREFIX = ("mc-cs-CY-", "mc-cs-HC-", "mc-cs-DL-", "mc-physics-hist-ph-", "mc-econ-GN-", "mc-cs-SI-")
SK = "data/skeletons_faceted_haiku"
ids = sorted(os.path.basename(f)[:-3] for f in glob.glob(f"{SK}/*.md"))
fac = {i: parse_facets(open(f"{SK}/{i}.md", encoding="utf-8").read()) for i in ids}
skipped = {i for i in ids if (fac[i].get("STRUCTURE", "") or "").lower().strip() in NONE}
nonmath = {i for i in ids if i.startswith(NONMATH_PREFIX)}
labels = {}
for l in open("datasets/mode_a_seed_families.csv"):
    if l.startswith("#") or l.startswith("id,") or not l.strip(): continue
    p = l.split(","); labels[p[0]] = p[4]
members = {i for i in ids if labels.get(i) == "member"}; distractors = {i for i in ids if labels.get(i) == "distractor"}
print(f"corpus {len(ids)}; skipped by STRUCTURE=none: {len(skipped)} "
      f"(benchmark members {len(skipped & members)}, distractors {len(skipped & distractors)}, "
      f"deliberately non-mathematical {len(skipped & nonmath)}, other wild {len(skipped - members - distractors - nonmath)})")
print(f"deliberately non-mathematical papers: {len(nonmath)}; caught by the rule {len(nonmath & skipped)}; passing {len(nonmath - skipped)}")
for i in sorted(skipped & members): print(f"  benchmark member skipped (distiller wrote STRUCTURE none): {i}")
keyf = "datasets/validity/wild_3arm_key.json"
if os.path.exists(keyf):
    key = json.load(open(keyf))["pairs"]
    hits = [(v["arms"], v["a"], v["b"]) for v in key.values() if v["nonmath_pair"]]
    print(f"passing non-mathematical papers appearing in judged top lists: {len(hits)} pairs" + ("" if not hits else ":"))
    for arms, a, b in hits: print(f"  {arms}: {a} <-> {b}")
