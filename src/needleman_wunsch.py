#!/usr/bin/env python3
"""Executed import (paper 1), WILD-surfaced pair (detection-rate top-50, pair id 44, non-curated):
computational linguistics imports the bioinformatics sequence-alignment solver. The system ranked two
topically-unrelated papers as a top cross-field pair by fingerprint distance: a bioinformatics GPU
sequence-alignment paper and a computational-linguistics paper that measures phonetic word similarity
"using the Needleman-Wunsch algorithm". Their abstracts share no field vocabulary, yet both solve the
same computation, and the linguistics paper has literally adopted the biology aligner.

Shared computational problem: global dynamic-programming sequence alignment (Needleman-Wunsch). The
linguistics bespoke tool, plain string edit distance (Levenshtein), is the UNIT-COST SPECIAL CASE of
the biology aligner; importing the aligner generalizes it with substitution scores and gap penalties.
This script runs ONE Needleman-Wunsch solver on a protein pair (biology) AND a phonetic word pair
(linguistics), and verifies that linguistics' edit distance is exactly the unit-cost aligner.

Offline, pure standard library, deterministic.
"""


def needleman_wunsch(a, b, match=1, mismatch=-1, gap=-1):
    """Standard global alignment DP. Returns (score, aligned_a, aligned_b)."""
    n, m = len(a), len(b)
    H = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        H[i][0] = i * gap
    for j in range(1, m + 1):
        H[0][j] = j * gap
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            s = match if a[i - 1] == b[j - 1] else mismatch
            H[i][j] = max(H[i - 1][j - 1] + s, H[i - 1][j] + gap, H[i][j - 1] + gap)
    # traceback
    i, j, ra, rb = n, m, [], []
    while i > 0 or j > 0:
        s = match if (i > 0 and j > 0 and a[i - 1] == b[j - 1]) else mismatch
        if i > 0 and j > 0 and H[i][j] == H[i - 1][j - 1] + s:
            ra.append(a[i - 1]); rb.append(b[j - 1]); i -= 1; j -= 1
        elif i > 0 and H[i][j] == H[i - 1][j] + gap:
            ra.append(a[i - 1]); rb.append("-"); i -= 1
        else:
            ra.append("-"); rb.append(b[j - 1]); j -= 1
    return H[n][m], "".join(reversed(ra)), "".join(reversed(rb))


def edit_distance(a, b):
    """Levenshtein edit distance: the linguistics bespoke tool."""
    n, m = len(a), len(b)
    D = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        D[i][0] = i
    for j in range(m + 1):
        D[0][j] = j
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            c = 0 if a[i - 1] == b[j - 1] else 1
            D[i][j] = min(D[i - 1][j - 1] + c, D[i - 1][j] + 1, D[i][j - 1] + 1)
    return D[n][m]


# 1) biology: align two protein sequences with one aligner (the textbook Needleman-Wunsch example)
sc, pa, pb = needleman_wunsch("HEAGAWGHEE", "PAWHEAE")
print("BIOLOGY  (protein alignment, the bespoke field's home turf):")
print(f"  {pa}\n  {pb}   score {sc}\n")

# 2) linguistics: align phonetic transcriptions of cognates with the SAME aligner
print("LINGUISTICS (phonetic word alignment, imported aligner):")
for w1, w2, gloss in [("naIt", "naxt", "night ~ Nacht"),
                      ("fadr", "pater", "father ~ pater"),
                      ("hund", "haUnd", "Hund ~ hound")]:
    sc, a1, a2 = needleman_wunsch(w1, w2)
    print(f"  {gloss:18}  {a1} / {a2}   score {sc}")

# 3) the import's special case: linguistics' edit distance == the unit-cost aligner, exactly
print("\nEDIT DISTANCE = UNIT-COST NEEDLEMAN-WUNSCH (the bespoke tool is the special case):")
ok = True
for w1, w2 in [("naIt", "naxt"), ("fadr", "pater"), ("hund", "haUnd"), ("kanton", "canton")]:
    nw_cost = -needleman_wunsch(w1, w2, match=0, mismatch=-1, gap=-1)[0]
    ed = edit_distance(w1, w2)
    ok &= (nw_cost == ed)
    print(f"  {w1:8} vs {w2:8}  edit-distance {ed}  ==  unit-cost-NW {nw_cost}  {'OK' if nw_cost==ed else 'MISMATCH'}")
print(f"\none alignment solver serves both fields; edit distance is its unit-cost special case "
      f"(verified exact: {ok}).\nimporting the biology aligner gives linguistics substitution scores "
      f"and gap penalties for free.")
