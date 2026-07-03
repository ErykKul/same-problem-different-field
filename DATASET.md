# Cross-domain computational-twin benchmark: dataset construction

This document specifies, in full, the canonical procedure for building the cross-domain
computational-fingerprint dataset: the corpora, the labeling rules, source acquisition, fingerprint
distillation, and the evaluation protocol. Following it reproduces a dataset of the same standard.

## 1. Purpose and organizing principle

The dataset supports one task: retrieving cross-domain **import pairs**, i.e. computationally isomorphic papers from different fields
that solve the **same underlying computational problem** under different names, so a bespoke
implementation in one field can import another field's standard, specialized solver in place of
re-deriving its own.

The organizing unit is the **method family**: one computational core (a specific mathematical object
computed for a specific inferential goal) that is *known to be swappable*. A standard, specialized
implementation of the core exists, so when the fingerprint pairs a paper's bespoke version with the
standard one in another field, that pair is an actionable import candidate, and the family serves as
ground truth precisely because the swap is already known to work.

## 2. Corpora

Two corpora with distinct jobs that are never conflated.

**Curated retrieval benchmark (the scored benchmark).** ~100 papers across ~18 method families. The
candidate pool is closed and the labels are complete, so ranking metrics (P@1, P@5, MRR, AUROC, AP,
clustering ARI) are trustworthy. This is the only corpus on which methods are compared.

**Scale / noise corpus (the wild run).** ~500 papers: the curated members embedded in a large
unlabeled background of in-the-wild and randomly sampled papers, a deliberate fraction of which are
non-mathematical. Only the families are labeled, so precision and AP are **not** validation here. Its
two jobs are detection (does the distance surface known twins among the noise?) and the
no-method-rejection check (does the fingerprint stay silent on papers with no computation?). The one
honest scale number is recall of the known twins, which ignores the unlabeled background.

## 3. Method families

A family qualifies when it satisfies all of:

1. **One core.** It is a single mathematical computation (a specific object computed for a specific
   goal), not a topic or a loose theme.
2. **Swappable.** A standard, specialized implementation of the core exists, so importing it across a
   field boundary is an actionable engineering act.
3. **Cross-field.** The core is genuinely re-derived in multiple distinct fields under different names
   and vocabulary.

Families span a range of sizes; two-member families (a single cross-field pair) are admissible and are
reported separately so their leverage on the headline can be checked.

## 4. Paper roles and the labeling rule

Each paper is assigned exactly one `(family, field, role)`. `role` is one of:

**member**: the paper's computational core solves the **same problem** as the family core: the same
mathematical object computed for the same inferential goal. The field, vocabulary, and even the
specific *algorithm* may differ; a different algorithm for the same problem is itself the import
target, so it still counts as a twin. A member must **present or apply** a computational method
(a method, model, estimator, simulation, or proof). Surveys, reviews, position pieces, and
announcements are never members: they originate no method of their own.

**distractor**: a hard negative attached to a family to test that retrieval is by computation, not by
topic or name. A distractor is one of:
- *topical near-miss*: same field as a member, or shared surface vocabulary, but a core that solves a
  **different** computational problem (e.g. a full eigen-decomposition where the family is a single
  dominant-eigenvector ranking; a static batch optimizer where the family is recursive filtering; a
  convergence-diagnostic where the family is the sampler itself); or
- *no-method paper*: a survey, review, position, or descriptive report with no computation of its own.

**Anti-cheat exemplars.** Wherever findable, include members that *use* a family's method **without
naming it**, so a match cannot be name recognition (e.g. an unnamed nonparametric-MLE / support-point
estimator, kriging as an unnamed Gaussian process, a sports-ranking computation presented without
the words "eigenvector centrality" or "PageRank").

**The rule in one line.** Same computational problem (an importable solver) **and** the paper presents a
method ⇒ *member*; different computational problem **or** no method ⇒ *distractor*. Each assignment is a
verifiable determination from the paper's mathematics (released as the skeleton, Section 6), not an
annotator's subjective judgment, so the labels rest on verifiability rather than consensus. A paper is a
member of the family whose computation it actually performs.

## 5. Source acquisition

Papers are specified as versioned CSV link-lists, one row per paper with columns
`id, url, family, field, role, method_named, license, note` (lines beginning `#` are comments). The
build step fetches each row and normalizes it to Markdown with YAML front-matter:

- **arXiv** → LaTeXML / ar5iv HTML with the mathematics preserved as LaTeX; on failure, fall back to the
  arXiv PDF; as a last resort, the abstract only.
- **Other open URLs** → PDF or HTML, converted to Markdown.
- **Paywalled / institutional-only resolvers** (a bare DOI/handle with no open copy, or a row flagged as
  needing access) are skipped cleanly; the open subset carries the headline result.

Provenance (final source URL, SHA-256 of the fetched bytes, retrieval timestamp, byte and character
counts) is recorded in `manifest.jsonl`.

> **Canonical requirement.** The fingerprint is distilled from each paper's **full text**, not its
> abstract. An abstract under-determines the mechanism and can yield an empty fingerprint for a paper
> that does in fact present a method, so full text is mandatory for every member. For redistribution,
> only abstracts are bundled (copyright); the full text is re-fetchable from the link-lists.

## 6. Fingerprint distillation

Each paper is reduced to a **faceted computational fingerprint** by a single LLM call (cached), at
**temperature 0**, with one **fixed prompt** that is part of the method and held constant across the
entire corpus. The canonical configuration uses a small instruct model (Claude Haiku). The call emits
one labeled line per facet; the eight facets are:

- **MECHANISM**: a complete 6–12 sentence, domain-neutral skeleton of *what is computed* and the
  algorithmic steps in order, in generic mathematical language. Every domain, application, and dataset
  word is stripped (no "patient", "stock", "gene", "galaxy", "city", "voter"; use "an entity", "a
  quantity", "an observation"), and canonical method *names* are avoided unless the mathematics cannot
  be stated without them. This is the primary retrieval signal and is never abbreviated.
- **DOMAIN**: the topical field, 3–8 words. The **only** facet permitted to name the field; it acts as
  the recall control.
- **STRUCTURE**: the domain-neutral computational pattern, exactly one value (scaffolded by the
  Berkeley motifs: dense/sparse linear algebra, spectral/transform, N-body, structured grid,
  unstructured mesh, map-reduce, combinational logic, graph traversal, dynamic programming,
  branch-and-bound, graphical models, finite-state machine, or `other: <few words>`; `none` if no
  computation).
- **DATA_OBJECT**: the primary structure operated on, exactly one value (dense matrix/tensor, sparse
  matrix, grid/lattice, mesh, graph/network, point set, sequence/time-series, tree/hierarchy, set/table,
  continuous function/field; `none`).
- **INFERENCE**: how unknowns/uncertainty are handled, exactly one value (deterministic/closed-form,
  frequentist point estimate, Bayesian posterior, variational, sampling/Monte-Carlo, bootstrap/
  resampling, optimization only; `none`).
- **PROBLEM_FORM**: the abstract goal, exactly one value (estimation; prediction/classification;
  optimization; decision/test; search; counting; simulation/generation; proof/characterization;
  control; ranking/retrieval).
- **DISTRIBUTION**: if an outcome variable is modeled, both its measured distribution (count,
  continuous, proportion/bounded, ordinal, binary, survival, heavy-tailed) and the distribution the
  estimator assumes; else `none`.
- **COMPLEXITY**: the stated complexity class or guarantee (closed-form, polynomial iterative,
  combinatorial/NP-hard, consistency, finite-sample bound, convergence rate, regret bound); `not stated`
  if absent.

Controlled-vocabulary facets take **exactly one** value, lowercased and copied verbatim from its list,
so two papers doing the same thing receive the same label (consistency over nuance; nuance lives in
MECHANISM).

**No-method handling.** The prompt first decides whether the paper computes anything at all. A
qualitative, position, survey-without-method, or purely descriptive paper has no computational core:
STRUCTURE, DATA_OBJECT, INFERENCE, DISTRIBUTION, COMPLEXITY return `none` and MECHANISM is a single
sentence. Such a paper therefore can never read as a twin, the intended behavior, and the reason
no-method papers are deliberately mixed into the corpus.

**Domain-retaining arm.** For the ablation that isolates domain-stripping from the LLM re-description, a
second skeleton is distilled with the identical prompt minus the strip instruction (domain words kept).

## 7. Stored representations

Per paper the dataset stores: the faceted skeleton (one file per distiller configuration), the abstract
(the native input for baseline embedders), and the manifest record. The skeleton is the released,
inspectable label justification.

## 8. Evaluation protocol

A **positive (twin)** is a cross-**field**, same-**family** pair of **members**; same-field pairs are
excluded so the task is strictly cross-domain. All cross-field member-or-distractor pairs form the
candidate set.

- **Headline metric: AP** (average precision) over all cross-field pairs; how cleanly the true twins
  concentrate at the top of the similarity ranking (1.0 = every twin above every non-twin; the random
  baseline is the pair prevalence, on the order of a few percent). AUROC, P@1, P@5, MRR, and clustering
  ARI are reported alongside.
- Each representation (the canonical skeleton, the abstract baseline, the keep-domain arm) is embedded
  (TF-IDF is the canonical embedder; sentence/scientific embedders are run for comparison), cross-field
  pairs are scored by similarity, and the metrics are computed against the twin labels.
- The **wild corpus** reports only recall of the known twins in the top-K and the fraction of
  pairs touching a non-mathematical paper that score as twins (the no-method rejection check).

The scored metrics come only from the canonical pairwise operator over the closed curated pool; ad-hoc
inline or seed-only scoring is a drift hazard and is not used.

### 8.1 Construct-validity and perturbation tests

Two experiments test the operator beyond the curated pool; both ship their LLM outputs under
`datasets/validity/` so the scoring reproduces offline (`make validity`), while regenerating the outputs
needs a model.

- **Three-arm wild precision** (`src/wild_three_arm.py` builds the pairs; `src/wild_three_arm_score.py`
  scores). Three blind annotators judge 90 cross-field wild pairs, 30 each from the system top, a random
  control, and single-facet-collision hard negatives (highest-similarity pairs sharing exactly one core
  facet). The metric is majority-vote precision per arm with a bootstrap CI, plus Fleiss kappa. This is
  prospective precision on unlabeled pairs, the non-circularity check the closed pool cannot give.
- **Interventional perturbation** (`src/perturbation_wf.js` rewrites and distills;
  `src/perturbation_score.py` scores). Each paper is rewritten two ways, a re-skin (new field, same
  computation) and a math-edit (same field, new computation); the fingerprint and the abstract are scored
  for cosine self-similarity to the original under each. The fingerprint should stay invariant under the
  re-skin and move under the math-edit; the abstract should do the reverse. The reported statistic is the
  interaction (a double dissociation).

## 9. Reproduction

- Rebuild the full-text corpus from the link-lists: `make data`.
- Distill the fingerprints (one cached LLM call per paper): `python src/distill_faceted.py`.
- Print the scored tables from the bundled skeletons + abstracts, no model and no network required:
  `make reproduce` (i.e. `python reproduce.py`); this also prints the construct-validity and perturbation
  numbers from the shipped outputs.
- Reproduce only the construct-validity and perturbation numbers, offline: `make validity`.

## 10. Quality bar

A dataset of this standard satisfies, for every paper:

1. **Members have a real, full-text mechanism.** Every member's skeleton has a non-empty MECHANISM that
   describes a genuine computation, distilled from full text; never from an abstract alone.
2. **Members match the family's problem.** The member's computation solves the family core's problem,
   verifiable directly from its skeleton; a different field or a different algorithm is allowed, a
   different *problem* is not.
3. **Surveys and announcements are distractors.** A paper that reviews or announces methods rather than
   presenting one is a no-method distractor, regardless of how much method vocabulary it contains.
4. **Distractors are genuine.** Each distractor is either a topical near-miss whose core solves a
   different problem, or a no-method paper; never a true twin in disguise.
5. **Names do not leak.** MECHANISM avoids canonical method names; anti-cheat members use a family's
   method without naming it, so retrieval cannot be name recognition.
6. **One source of truth.** The `(family, field, role)` labels live in the versioned link-list and drive
   every scored number; the manifest mirrors them. Any relabeling is made once, in the link-list, and
   the full suite is re-scored from it.
