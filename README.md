# Same Problem, Different Field: cross-domain solution import via domain-stripped computational fingerprints (reproduction package)

The same underlying computational problem is independently re-solved across unrelated fields under
different names: a recursive Bayesian estimator is a "Kalman filter" in control, "Bayesian forecasting"
in pharmacokinetics, and "data assimilation" in geoscience. Topical and citation-based scientific
embeddings cannot see this kinship, because they cluster papers by the vocabulary and field that differ.

This package reduces each paper to a domain-stripped, method-name-stripped **computational fingerprint**
(one cached LLM call per paper) and ranks cross-field **twins** (papers solving the same computational
problem) with a cheap embedder over those fingerprints. It reproduces the paper's two headline tables.

**It runs offline: no model, no API key, no network** after one small online step: five abstracts are
not redistributable and are rebuilt locally by `make restricted-data` (sha256-verified; see the
redistribution section). Everything else, fingerprints and licensed abstracts, is bundled under
`data/`, so the headline reproduces from `scikit-learn` alone.

## The headline (curated benchmark: 109 papers, 5,812 cross-field pairs, 210 twins)

Average precision (AP): how cleanly the true cross-domain twins sit at the top of the ranked list
(1.0 = every twin above every non-twin; about 0.04 = random at this 3.6% prevalence).

| method | AP |
|---|---|
| abstract + SPECTER | 0.095 |
| abstract + SemCSE | 0.141 |
| abstract + E5-large-v2 | 0.144 |
| abstract + SciNCL | 0.149 |
| abstract + TF-IDF | 0.222 |
| abstract + Qwen3-Embedding-0.6B | 0.226 |
| mechanism skeleton + TF-IDF [Haiku] | 0.513 |
| **faceted fingerprint + TF-IDF [Haiku distiller, ours]** | **0.557** |

The faceted fingerprint embedded with a plain bag-of-words (TF-IDF) is the strongest method, more than
double the abstract. The dedicated scientific embedders (SPECTER, SciNCL, SemCSE, and
SPECTER2 via `src/specter2_local.py`) all fall below the plain abstract+TF-IDF baseline, because they
encode topical and citation similarity, the wrong signal for cross-domain computational matching. Full
AUROC and recall@K columns, plus the extended/wild-run table, are written to `reproduce_out/`.

**Benchmark versions.** The headline above is the grown **109-paper** benchmark: documented cross-domain
imports from the paper's introduction were added (inverse Ising/Potts, self-exciting Hawkes, and optimal
transport as new families; matrix completion and data assimilation as new members of the existing
low-rank and Kalman families).
All three distillers cover the full 109 papers, so `reproduce.py`'s faceted Haiku / Opus / qwen3-14b
rows (AP 0.557 / 0.533 / 0.396) are the three-distiller robustness comparison reported in the paper.
Labels follow the label-by-core audit (`FAMILY_AUDIT.md`; every benchmark paper is labelled by the
computational core its fingerprint actually computes, not by its field or its planted role), giving the
canonical 210 twins; the full dataset specification is `DATASET.md`.

## Quickstart

Python 3.12+ (developed and verified on 3.14; `.tool-versions` pins the verified interpreter for
mise/asdf users, but any recent CPython works).

```
make setup        # one time: create .venv and install requirements
make reproduce    # print both tables, write reproduce_out/
```

or without make:

```
pip install -r requirements.txt
python reproduce.py
```

The first run downloads the SOTA embedder checkpoints (SPECTER, SciNCL, SemCSE, Qwen3-Embedding) from
HuggingFace to print their baseline rows; any that cannot be loaded are skipped and the rest of the
table still prints. The "ours" rows (the headline) need only `scikit-learn`, no download.

## What the two tables mean

- **Curated benchmark** (complete labels within a closed candidate pool): the place to **compare
  methods**. AP is the headline; AUROC is kept only for continuity (at low prevalence a high AUROC is
  nearly free).
- **Extended / wild run** (incomplete labels): this is **detection**, not a scored benchmark. The honest
  metric is recall of the *known* twins (it ignores the unlabelled background); AP there is a lower
  bound, shown only for relative ranking.

## What is in the package

```
same-problem-different-field/
  reproduce.py                   one command -> both tables
  data/                          the BUNDLED, reproducible corpus (derived artifacts only):
    skeletons_faceted_haiku/       fingerprints, our config (Haiku distiller)          [501]
    skeletons_v1_opus/             fingerprints, Opus distiller (comparison)           [501]
    skeletons_faceted_qwen_v3/     fingerprints, Qwen3-14b distiller (comparison)      [501]
    md/                            abstract-only Markdown per paper (title + abstract) [496 bundled;
                                   5 rebuilt locally by make restricted-data, see data/restricted.csv]
    skeletons_keepdomain_qwen/     keep-domain ablation arm (qwen3 distiller)          [109]
    vanco/                         the vancomycin PK example data (gendata.csv, genmodel.txt)
    manifest.jsonl                 per-paper provenance: source URL, license, field, family, role
  datasets/                      the link lists, to rebuild the full-text corpus:
    mode_a_seed_families.csv       curated benchmark (labelled families)
    mode_b_discovery.csv           the wild run (unlabelled arXiv background)
  src/                           fetch + convert + distill + embed code
  reproduce_out/                 the expected tables (regenerated by reproduce.py)
  DATASET.md  FAMILY_AUDIT.md   the benchmark specification and the label-by-core audit
  MODELS.md                      model identifiers, prompt versions, and run dates per distiller/annotator arm
  requirements.txt  Makefile  example.env  SHA256SUMS
```

## What is bundled, and redistribution

This package ships derived artifacts plus abstracts **only where a license covers them**:

- the **fingerprints** (stored in the `skeletons_faceted_*` directories, named so for historical reasons):
  domain-stripped, method-name-stripped LLM re-descriptions of each paper's computation. They do not
  reproduce the source text. (Terminology: the full *fingerprint* is a **mechanism skeleton**, the MECHANISM
  field alone (AP 0.513), **plus** its controlled facets (together AP 0.557); 'skeleton' on its own always
  means the MECHANISM field, not the whole fingerprint.)
- an **abstract-only** Markdown per paper (title + abstract; never the full body), bundled for 496 of
  the 501 papers under the licenses that permit it: abstracts of arXiv-hosted papers are descriptive
  metadata under arXiv's CC0 1.0 grant (https://info.arxiv.org/help/api/tou.html, which defines
  descriptive metadata to include the abstract and permits storing and sharing it, independent of the
  e-print's own license), and a small PMC subset is CC BY (each file's source URL and license are in
  `data/manifest.jsonl`; attribution travels with those records).
- **five abstracts are not redistributable and do not ship** (two publisher pages with no license, one
  IEEE paper, and two PMC NC/ND entries handled conservatively). `data/restricted.csv` records their
  ids, source URLs, and the sha256 of the frozen bytes; `make restricted-data` rebuilds them locally
  (the one online step) and verifies the checksums, and `reproduce.py` refuses to run on a silently
  smaller corpus. If a publisher page has changed, the frozen files are available from the author for
  verification.
- `data/vanco/` is LAPKB's own NPAG example data (the vancomycin model/data pair distributed with
  their open-source solver, https://github.com/LAPKB), included unchanged for the executed import.

The **full-text corpus is not redistributed.** Rebuild it locally from the link lists with `make data`
(fetches arXiv + open URLs; paywalled or non-arXiv rows skip cleanly). Each paper's source URL and
license are recorded in `data/manifest.jsonl`.

The curated benchmark is **109 papers**, all bundled as fingerprints, so the curated headline (faceted
fingerprint + TF-IDF, AP 0.557) reproduces **exactly** once the five restricted abstracts are rebuilt;
the extended/wild run reproduces from the bundled 501-paper fingerprint set.

## Executed cross-domain imports

Each surfaced import is carried end to end by a self-contained, offline script (this is the paper's
import section, made reproducible); expected output is in `reproduce_out/`:

```
python src/pk_npml.py            # clinical NPAG dosing            -> open nonparametric-MLE / EM (vancomycin)
python src/causal_mc.py          # causal-panel fixed effects      -> recsys SoftImpute completion (69% lower RMSE)
python src/kriging_gp.py         # geostatistics kriging           -> ML Gaussian process (same BLUP + uncertainty)
python src/needleman_wunsch.py   # comp.-linguistics edit distance -> bioinformatics Needleman-Wunsch (wild pair)
python src/import_surfacing.py   # the retrieval half: the fingerprint links each pair across fields
```

Four imports across four computational cores (sparse-mixture MLE, low-rank completion, Gaussian-process
regression, sequence alignment), each reproducible with numpy/scikit-learn only. `import_surfacing.py`
shows the fingerprint ranks the recsys factorization paper 3rd of 500 cross-field neighbors of the
ideal-points paper (abstract cosine 0.03), the retrieval a topical embedder misses.

## Optional: rebuild or regenerate

You do **not** need either of these to reproduce the tables.

- **Rebuild the full-text corpus** from the link lists (network needed):

  ```
  make data
  ```

- **Regenerate the fingerprints with your own model** (reproduces the *method*, not the exact bundled
  skeletons). `reproduce.py` reads the three fixed directory names below; re-distill into them with
  `--force` to compare your own distiller:

  ```
  # the eight-facet prompt that produced the bundled Haiku and Opus arms (see MODELS.md):
  python src/distill_v1.py     --backend ollama --model qwen3:14b --outdir data/skeletons_faceted_haiku --force
  # the twelve-facet prompt that produced the bundled qwen3 arms (adds four verifiability facets the distance ignores):
  python src/distill_faceted.py --backend ollama --model qwen3:14b --outdir data/skeletons_faceted_qwen_v3 --force
  python reproduce.py
  ```

  Distillation needs a model (local via ollama, or the Anthropic API via `.env`; see `example.env`); the
  bundled fingerprints need neither. The paper's Haiku/Opus skeletons were produced by agents, not a
  hosted API call, so the bundled fingerprints are the authoritative ones.

## How it works (one paragraph)
F
skeleton" that says what the paper computes and how, with the domain vocabulary and canonical method
names removed, plus a few controlled computational facets (structure or motif, data object, inference,
problem form, outcome distribution, complexity). A tunable distance over the fingerprint retrieves
candidate twins; a cheap TF-IDF over the whole fingerprint is already the strongest ranker. The
distillation prompt is in `src/`, and the method and analysis are in the paper.

## Integrity

```
sha256sum -c SHA256SUMS                 # 2175 files, all OK
python src/name_free_audit.py           # reproduces the anti-cheat name-free rates
```

Each skeleton describes its computation without naming the canonical method, so a cross-field match is
abstraction, not name recognition. `name_free_audit.py` ships the pinned name lists and reports the
name-free rate under each: 93% against the method names the distiller is told to strip (Kalman, Gaussian
process, SVM, EM, HMM, PageRank), 88% if every core's canonical name is added, 82% with generic labels
(PCA, Fourier, MCMC) too. Expected output is in `reproduce_out/name_free_audit.txt`.

Every number reported in the paper is regenerated by a shipped script in `src/`: the AP grid by
`reproduce.py` and `full_grid.py`, the bootstrap confidence intervals by `ap_bootstrap.py` (with the family-level cluster bootstrap by `family_bootstrap.py`), the
precision/recall frontier by `facet_ops.py`, the domain-stripping ablation by `abl_109.py` (with
`distill_faceted.py --keep-domain` regenerating the keep-domain arm), the E5-large-v2 baseline by
`e5_grid.py`, the SPECTER2 baseline (local model + proximity adapter) by `specter2_local.py`, the
held-out-family generalization test by `held_out_family.py`, the three-distiller comparison by
`distiller_subset.py`, the non-mathematical-rejection rate by `nonmath_reject.py`, the interventional
perturbation test by `perturbation_score.py`, the wild three-arm precision by `wild_three_arm_score.py`,
the two-member-family robustness by `perfam_sens.py`, and the per-family / P@1-MRR /
facet-agreement / DOMAIN-ablation diagnostics by `perfam.py`, `p1mrr_boot.py`, `facet_agree_ap.py`, and
`nodomain.py`.

## Status, archive and citation

This repository is the public record of this work: the full method, every reported number, and
everything needed to reproduce them offline (after the one-time `make restricted-data` rebuild of the
five non-bundled abstracts). A frozen copy (release v1.0.0) is deposited in the KU Leuven Research
Data Repository (RDR). Please cite both:

- Paper: Eryk Kulikowski. 2026. Same Problem, Different Field: Cross-Domain Solution Import via
  Domain-Stripped Computational Fingerprints. In *The 2026 ACM/IEEE Joint Conference on Digital
  Libraries (JCDL '26)*. ACM. https://doi.org/10.1145/3805696.3846016
- Dataset: Eryk Kulikowski. 2026. Replication Data for: Same Problem, Different Field - Cross-Domain
  Solution Import via Domain-Stripped Computational Fingerprints. KU Leuven RDR.
  https://doi.org/10.48804/W3B9WC

## License

**Code**: Apache-2.0 (the `LICENSE` file covers the code only). **Derived data produced by this
project** (the fingerprints in `data/skeletons*`, the manifest, the link lists, the validity
artifacts): CC-BY-4.0. **Third-party text keeps its original terms; this package grants no rights
over it**: abstracts of arXiv-hosted papers are bundled under arXiv's CC0 metadata grant, the PMC
CC-BY abstracts under CC BY with the source recorded per paper in `data/manifest.jsonl`, and five
abstracts are not redistributed at all (see the redistribution section). `data/vanco/` is LAPKB's
NPAG example data, credited above.
