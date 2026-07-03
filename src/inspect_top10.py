#!/usr/bin/env python3
"""Look at what the fingerprint actually retrieves: top-10 cross-field neighbors per import seed, each
tagged labeled-twin / other-curated / WILD-unlabeled, with title + abstract. Unlabeled is NOT wrong:
judge the wild neighbors on the merits, do not assume a non-twin label means a non-match.

Run from the package root with the venv:  python src/inspect_top10.py
"""
import re
import sys
from pathlib import Path
import numpy as np
sys.path.insert(0, "."); sys.path.insert(0, "src")
import embed as E      # noqa: E402
import reproduce as R  # noqa: E402

DATA = "data"
lab, fld = R.load_labels(), R.load_field()
absr = E.load_rep(DATA, "abstract")
ids = sorted(set(absr) & set(p.stem for p in Path(f"{DATA}/skeletons_faceted_haiku").glob("*.md")))
field = {i: (fld.get(i) or lab.get(i, {}).get("field", "") or "?") for i in ids}
family = {i: (lab.get(i, {}).get("family", "") if lab.get(i, {}).get("role", "member") == "member" else "") for i in ids}
idx = {i: k for k, i in enumerate(ids)}
FP = E.cosine_matrix(R.vectors([R.faceted_text("skeletons_faceted_haiku", i) for i in ids], "tfidf"))


def title(i):
    t = re.sub(r"^---\n.*?\n---\n", "", Path(f"{DATA}/md/{i}.md").read_text(encoding="utf-8"), flags=re.S)
    m = re.search(r"^#\s+(.+)", t, flags=re.M)
    return (m.group(1) if m else i).strip()[:88]


SEEDS = {"vanco (clinical NPAG dosing)": "em-pharma-noname-001",
         "A (ideal points / low-rank)": "pca-polmeth-001",
         "B (kriging / GP)": "gp-geo-noname-001",
         "C (sequence alignment / DP)": "dp-bio-001"}
for name, seed in SEEDS.items():
    si = idx[seed]
    order = [k for k in np.argsort(-FP[si]) if ids[k] != seed and field[ids[k]] != field[seed]]
    print(f"\n===== {name}: seed {seed}  family={family[seed]!r}  field={field[seed]!r} =====")
    print(f"      {title(seed)}")
    ntwin = sum(1 for k in order[:10] if family[ids[k]] and family[ids[k]] == family[seed])
    print(f"      top-10 cross-field: {ntwin} labeled same-core twins, {10-ntwin} other (judge on merits)")
    for r, k in enumerate(order[:10]):
        j = ids[k]
        fam = family[j]
        tag = "[TWIN same-core]" if fam and fam == family[seed] else (f"[curated:{fam}]" if fam else "[WILD unlabeled]")
        ab = " ".join(absr.get(j, "").split())[:155]
        print(f"  #{r+1:2} cos {FP[si, k]:.3f} {tag:20} {j}  ({field[j]})")
        print(f"        {title(j)}")
        print(f"        {ab}")
