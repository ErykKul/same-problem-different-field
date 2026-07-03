#!/usr/bin/env python3
"""Re-centered eval (the original design): a TUNABLE, FACET-SELECTABLE distance + CLUSTERING.

The operator is NOT a fixed point. (1) per-facet distance: cosine for the free-text MECHANISM (the
high-recall retriever); an AGREEMENT-COUNT / Hamming "k of K facets agree" for the controlled-vocab
discrete facets (agree = cosine >= a match threshold, so near-synonyms count). (2) SELECT which facets
to require. (3) tune the cutoff / k -> the precision/recall FRONTIER (tight = fewer but better matches;
loose = more matches, more false positives, fewer missed). (4) CLUSTER the corpus by the chosen distance.
The retrieve-then-filter (facet_roc.py) is ONE point on this frontier. Engine for the end product: a
browser over an institutional papers + datasets library where the user tunes facets/threshold and sees clusters.

  python src/facet_select.py --skdir data/skeletons_faceted_haiku
"""
from __future__ import annotations
import os, sys, csv, io, json, argparse, itertools, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np  # noqa: E402
import embed as E  # noqa: E402
from distill_faceted import FACETS, parse_facets  # noqa: E402

ST = "st:sentence-transformers/all-MiniLM-L6-v2"
NONE = {"", "none", "none.", "not stated", "not stated.", "not applicable", "n/a", "na", "no computation"}
LABEL_CSVS = ["datasets/mode_a_seed_families.csv", "datasets/extended_private.csv"]
CORE = ["STRUCTURE", "DATA_OBJECT", "INFERENCE", "PROBLEM_FORM"]  # the discrete facets to select over


def load_labels():
    out = {}
    for c in LABEL_CSVS:
        if not os.path.exists(c):
            continue
        lines = [ln for ln in open(c, encoding="utf-8").read().splitlines() if not ln.lstrip().startswith("#")]
        for r in csv.DictReader(io.StringIO("\n".join(lines))):
            rid = (r.get("id") or "").strip()
            if rid and (r.get("url") or "").strip():
                out[rid] = {"family": (r.get("family") or "").strip(),
                            "field": (r.get("field") or "").strip(),
                            "role": (r.get("role") or "member").strip()}
    return out


def load_field():
    field = {}
    if os.path.exists("data/manifest.jsonl"):
        for ln in open("data/manifest.jsonl", encoding="utf-8"):
            ln = ln.strip()
            if not ln:
                continue
            try:
                r = json.loads(ln)
            except json.JSONDecodeError:
                continue
            field[r["id"]] = (r.get("field") or "").strip()
    return field


def pr(keep, pos, P):
    if keep.sum() == 0:
        return float("nan"), 0.0, 0
    return float(pos[keep].mean()), float(pos[keep].sum() / P), int(keep.sum())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--skdir", default="data/skeletons_faceted")
    ap.add_argument("--match", type=float, default=0.85, help="per-facet agreement cosine threshold")
    ap.add_argument("--retriever", default="faceted-tfidf", choices=["faceted-tfidf", "mech-minilm"],
                    help="retrieval distance: full faceted block + TF-IDF (best) or MECHANISM + MiniLM")
    ap.add_argument("--alpha", type=float, default=0.4,
                    help="combined-distance mix (default scorer): alpha*skeleton + (1-alpha)*weighted facets")
    ap.add_argument("--seed", default="", help="seed paper id: print its cross-domain neighbours under the combined distance")
    a = ap.parse_args()
    print(f"[facet-select on {a.skdir} | per-facet agreement cos>={a.match}]")

    ids = sorted(f[:-3] for f in os.listdir(a.skdir) if f.endswith(".md"))
    fac = {i: parse_facets(open(f"{a.skdir}/{i}.md", encoding="utf-8").read()) for i in ids}
    labels, mfield = load_labels(), load_field()
    fld = {i: (mfield.get(i) or labels.get(i, {}).get("field", "") or "?") for i in ids}
    fam = {i: labels.get(i, {}).get("family", "") for i in ids}
    role = {i: labels.get(i, {}).get("role", "") for i in ids}
    is_seed = {i: bool(i in labels and role[i] == "member" and fam[i]) for i in ids}
    N = len(ids); idx = {i: k for k, i in enumerate(ids)}

    S, isnone = {}, {}
    for f in FACETS:
        S[f] = E.cosine_matrix(E.embed_texts([fac[i].get(f, "") or "none" for i in ids], ST))
        isnone[f] = np.array([(fac[i].get(f, "") or "").lower().strip() in NONE for i in ids])

    # RETRIEVER distance: the ENTIRE faceted block + TF-IDF (best retriever; controlled-vocab exact terms)
    if a.retriever == "faceted-tfidf":
        full = [open(f"{a.skdir}/{i}.md", encoding="utf-8").read() for i in ids]
        Rretr = E.cosine_matrix(E.embed_texts(full, "tfidf"))
    else:
        Rretr = S["MECHANISM"]
    print(f"retriever = {a.retriever}")

    A, B = np.triu_indices(N, 1)
    cross = np.array([fld[ids[x]] for x in A]) != np.array([fld[ids[x]] for x in B])
    famA = np.array([fam[ids[x]] if is_seed[ids[x]] else "" for x in A])
    famB = np.array([fam[ids[x]] if is_seed[ids[x]] else "" for x in B])
    pos = ((famA != "") & (famA == famB))[cross]
    A, B = A[cross], B[cross]
    P = int(pos.sum())
    print(f"cross-field pairs {len(A):,} | twins {P} (prevalence {P/max(len(A),1)*100:.2f}%) | "
          f"seeds {sum(is_seed.values())} in {len({fam[i] for i in ids if is_seed[i]})} families")

    AG = {f: (S[f][A, B] >= a.match) & ~(isnone[f][A] | isnone[f][B]) for f in CORE}  # per-facet agreement
    mech = Rretr[A, B]
    order = np.argsort(-mech)

    # 1. TUNABLE RETRIEVAL (mechanism distance)
    print("\n=== 1. TUNABLE RETRIEVAL (mechanism cosine; high-recall stage) ===")
    print(f"{'top-N':>7} {'precision':>10} {'recall':>8}")
    for Nn in [100, 300, 1000, 3000]:
        if Nn > len(order):
            break
        keep = np.zeros(len(A), bool); keep[order[:Nn]] = True
        p, r, _ = pr(keep, pos, P); print(f"{Nn:>7} {p:>10.3f} {r:>8.3f}")

    # 2. TUNABLE FILTER: k-of-K agreement on the top-1000 retrieved candidates
    cand = np.zeros(len(A), bool); cand[order[:min(1000, len(A))]] = True
    agc = np.sum([AG[f] for f in CORE], axis=0)
    print(f"\n=== 2. TUNABLE FILTER (k-of-{len(CORE)} core facets agree; on top-1000 mech candidates) ===")
    print(f"{'k>=':>4} {'precision':>10} {'recall':>8} {'kept':>6}")
    for k in range(0, len(CORE) + 1):
        p, r, kk = pr(cand & (agc >= k), pos, P); print(f"{k:>4} {p:>10.3f} {r:>8.3f} {kk:>6}")
    print("  (k=0 is flat top-1000; raising k TIGHTENS -> precision up, recall down = the tunable knob)")

    # 3. FACET SELECTION: which subset (all agree) buys the best precision/recall
    print(f"\n=== 3. FACET SELECTION (require ALL facets in the subset to agree; on top-1000) ===")
    rows = []
    for r_ in range(1, len(CORE) + 1):
        for sub in itertools.combinations(CORE, r_):
            keep = cand.copy()
            for f in sub:
                keep &= AG[f]
            p, rc, kk = pr(keep, pos, P)
            if not np.isnan(p):
                rows.append((p, rc, kk, "+".join(s.split("_")[0][:5] for s in sub)))
    print(f"{'subset':26} {'precision':>10} {'recall':>8} {'kept':>6}")
    print("  -- highest precision (tight) --")
    for p, rc, kk, name in sorted(rows, key=lambda x: -x[0])[:4]:
        print(f"{name:26} {p:>10.3f} {rc:>8.3f} {kk:>6}")
    print("  -- best precision*recall (balanced) --")
    for p, rc, kk, name in sorted(rows, key=lambda x: -(x[0] * x[1]))[:4]:
        print(f"{name:26} {p:>10.3f} {rc:>8.3f} {kk:>6}")
    print("  (pick the subset for your target: tight subsets = precision, single facets = recall = SELECTION)")

    # 3b. NORMALIZED distance: weight each facet's agreement by its log-likelihood-ratio (evidence)
    print(f"\n=== 3b. NORMALIZED: log-LR facet weights (in-sample; LOFO-CV is the honest TODO) ===")
    DISC6 = ["STRUCTURE", "DATA_OBJECT", "INFERENCE", "PROBLEM_FORM", "DISTRIBUTION", "COMPLEXITY"]
    eps = 1e-3
    AG6 = {f: (S[f][A, B] >= a.match) & ~(isnone[f][A] | isnone[f][B]) for f in DISC6}
    w = {}
    print(f"  {'facet':14} {'w (log-LR)':>11} {'P(agree|twin)':>13} {'P(agree|rand)':>13}")
    for f in DISC6:
        ptw = AG6[f][pos].mean() if P else 0.0
        pne = AG6[f][~pos].mean() if (~pos).sum() else 0.0
        w[f] = float(np.log((ptw + eps) / (pne + eps)))
    for f in sorted(DISC6, key=lambda x: -w[x]):
        ptw = AG6[f][pos].mean() if P else 0.0; pne = AG6[f][~pos].mean() if (~pos).sum() else 0.0
        print(f"  {f:14} {w[f]:>11.2f} {ptw:>13.3f} {pne:>13.3f}")
    from sklearn.metrics import average_precision_score
    rawk = np.sum([AG6[f] for f in DISC6], axis=0).astype(float)
    wsc = np.sum([w[f] * AG6[f] for f in DISC6], axis=0)
    print(f"  AP over all cross-field pairs: RAW equal-weight count {average_precision_score(pos, rawk):.3f}"
          f"  vs  log-LR WEIGHTED {average_precision_score(pos, wsc):.3f}  (higher = normalization helps)")
    ow = np.argsort(-wsc)
    print(f"  {'top-N(wLR)':>10} {'precision':>10} {'recall':>8}  (weighted-score operating points)")
    for Nn in [50, 100, 200, 500]:
        keep = np.zeros(len(A), bool); keep[ow[:Nn]] = True
        p, r, _ = pr(keep, pos, P); print(f"  {Nn:>10} {p:>10.3f} {r:>8.3f}")

    # 5. COMBINED distance: skeleton bag-of-words (retriever) + log-LR weighted facets, grid-search the mix
    print("\n=== 5. COMBINED DISTANCE (skeleton-retriever + log-LR facets, normalized, grid-searched) ===")
    from sklearn.metrics import roc_auc_score

    def z(x):
        x = np.asarray(x, float); s = x.std()
        return (x - x.mean()) / (s if s > 1e-9 else 1.0)
    skel_z, fac_z = z(Rretr[A, B]), z(wsc)
    ap_s, ap_f = average_precision_score(pos, skel_z), average_precision_score(pos, fac_z)
    print(f"  {'alpha_skel':>10} {'AP':>7} {'AUROC':>7}")
    best = None
    for al in [0.0, 0.2, 0.4, 0.5, 0.6, 0.8, 1.0]:
        comb = al * skel_z + (1 - al) * fac_z
        ap, au = average_precision_score(pos, comb), roc_auc_score(pos, comb)
        print(f"  {al:>10.1f} {ap:>7.3f} {au:>7.3f}")
        if best is None or ap > best[1]:
            best = (al, ap, au)
    print(f"  -> best mix alpha={best[0]:.1f}: AP {best[1]:.3f}  vs skeleton-only AP {ap_s:.3f}, "
          f"facet-only AP {ap_f:.3f}  (combined > both => the skeleton sharpens the facet filter)")

    # 4. CLUSTERING by mechanism distance over the seed papers (the restored view)
    print(f"\n=== 4. CLUSTERING (agglomerative on COMBINED distance alpha={a.alpha}, seed papers) ===")
    ari = float("nan")
    seeds = [i for i in ids if is_seed[i]]
    if len(seeds) >= 6:
        from sklearn.cluster import AgglomerativeClustering
        from sklearn.metrics import adjusted_rand_score
        sidx = [idx[i] for i in seeds]
        # COMBINED distance (the default scorer): alpha*skeleton + (1-alpha)*log-LR weighted facet agreement
        skelm = Rretr[np.ix_(sidx, sidx)]
        facm = np.zeros_like(skelm)
        for f in DISC6:
            ag = ((S[f][np.ix_(sidx, sidx)] >= a.match)
                  & ~isnone[f][sidx][:, None] & ~isnone[f][sidx][None, :])
            facm = facm + w[f] * ag
        zm = lambda m: (m - m.mean()) / (m.std() + 1e-9)  # noqa: E731
        comb = a.alpha * zm(skelm) + (1 - a.alpha) * zm(facm)
        D = np.clip(comb.max() - comb, 0, None); np.fill_diagonal(D, 0)
        truef = [fam[i] for i in seeds]; nfam = len(set(truef))
        cl = AgglomerativeClustering(n_clusters=nfam, metric="precomputed", linkage="average").fit_predict(D)
        ari = adjusted_rand_score(truef, cl)
        print(f"seeds {len(seeds)} | {nfam} families -> {nfam} clusters | ARI vs families = "
              f"{ari:.3f}  (1.0 = method-families recovered exactly)")
        byc = collections.defaultdict(list)
        for s, c in zip(seeds, cl):
            byc[c].append(s)
        shown = 0
        for c, mem in byc.items():
            flds = sorted({fld[m] for m in mem})
            if len(mem) >= 3 and len(flds) >= 2 and shown < 3:
                print(f"  cross-field cluster: {len(mem)}p, fields={flds[:5]}, family={sorted({fam[m] for m in mem})}")
                shown += 1
    else:
        print("  too few seeds distilled yet")

    within = float(agc[pos].mean()) / len(CORE) if P else float("nan")
    print(f"\n=== FACETED SUMMARY [{os.path.basename(a.skdir)}] (canonical cleaned labels) ===")
    print(f"  combined-distance AP (best mix): {best[1]:.3f}")
    print(f"  facet-only AP (log-LR weighted): {ap_f:.3f}")
    print(f"  within-family core-facet agree:  {within:.3f}")
    print(f"  clustering ARI:                  {ari:.3f}")

    # SEED SCENARIO: the canonical discovery use (STATE.md 0a): seed -> cross-domain neighbours under
    # the COMBINED distance (same Rretr + log-LR weights + alpha as everywhere above).
    if a.seed and a.seed in idx:
        k = idx[a.seed]
        zc = lambda v: (v - v.mean()) / (v.std() + 1e-9)  # noqa: E731
        skel_seed = Rretr[k]
        wsc_seed = np.zeros(N)
        for f in DISC6:
            wsc_seed = wsc_seed + w[f] * ((S[f][k] >= a.match) & ~(isnone[f][k] | isnone[f]))
        comb_seed = a.alpha * zc(skel_seed) + (1 - a.alpha) * zc(wsc_seed)
        print(f"\n=== SEED SCENARIO: {a.seed} [{fld[a.seed]}] fam={fam[a.seed]} (combined alpha={a.alpha}) ===")
        print("   facets: " + " | ".join(f"{f}={(fac[a.seed].get(f, '') or '')[:18]}" for f in DISC6))
        print("   -- top cross-domain neighbours by COMBINED distance --")
        for o in [o for o in np.argsort(-comb_seed) if o != k and fld[ids[o]] != fld[a.seed]][:12]:
            print(f"   {comb_seed[o]:+.2f} [{fld[ids[o]]:18}] fam={fam[ids[o]] or '-':22} {ids[o]}")
        oc = list(np.argsort(-comb_seed)); osk = list(np.argsort(-skel_seed))
        print("   -- importable-solver papers: COMBINED rank vs skeleton(faceted-tfidf) rank (of 497) --")
        for wid in ["priv-svm-supportpoint-001", "clf-nlp-001", "mc-math-OC-003", "mc-stat-ME-002", "mb-cs-LG-015"]:
            if wid in idx:
                o = idx[wid]
                print(f"      {wid:26} [{fld[wid]:16}] COMBINED rank {oc.index(o):4} ({comb_seed[o]:+.2f})   skeleton rank {osk.index(o):4}")

    print("\nREAD: (2) precision rises with k = TUNABLE; (3) shows which facets to SELECT for a target; "
          "(4) ARI shows method-families recover as CLUSTERS.")


if __name__ == "__main__":
    main()
