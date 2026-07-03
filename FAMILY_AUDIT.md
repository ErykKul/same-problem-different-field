# Family-label audit (2026-06-29; 18 Opus agents, one per family)

**Headline.** Every family has a genuine same-computation cross-field CORE, and the 4 planted distractors
were correctly flagged as non-fitting (the anti-cheat works). BUT ~12 of 99 members across 11 families were
flagged as not cleanly fitting their family's core computation. The labels are at the **same problem-class**
level; the fingerprint matches at the **same mechanism** level, so where a member shares the problem but not
the mechanism, the agents (judging mechanism) flag it. Review before submission.

## Clean (members all fit)
- `hawkes_self_exciting`, `inverse_ising_potts` (CONSISTENT)
- `gaussian_process` (MOSTLY; kriging/GMRF are defensible GP aliases), `optimal_transport` (MOSTLY)
- `diffusion_heat`, `dynamic_programming_viterbi`, `linear_text_classifier`: members fit; the only flag is the
  planted DISTRACTOR (by design, correctly separable) -- `diff-physics-dist-001`, `dp-fin-distractor-001`,
  `clf-nlp-distractor-001`.

## Tier 1 -- clear bugs: empty / survey skeletons (no computation at all) -> FIX or DROP
- `hmm-speech-001` (hmm): a literature survey, all facets 'none', no instantiated computation.
- `pa-cities-noname-001` (preferential_attachment): empty fingerprint (MECHANISM/STRUCTURE/DATA all none).
- `replv-evolution-001` (replicator_lotka_volterra): empty skeleton, describes no computation.

## Tier 2 -- mechanism mismatch: member solves a materially different computation -> REVIEW
- `eigen-chem-noname-001` (eigenvector_centrality): full Huckel eigenSPECTRUM (MO energies), not leading-eigenvector centrality.
- `irt-ecology-001` (irt): spatial logistic occupancy GLM, not the Bradley-Terry ability-minus-difficulty structure.
- `mcmc-phylo-001` (mcmc_metropolis): MCMC convergence DIAGNOSTICS (ESS), not the Metropolis kernel itself.
- `kalman-pharma-noname-001` (recursive_bayes_kalman): batch/static MAP (L-BFGS); its own fingerprint says "not filtering" -- not recursive filtering. [Consistent with the SVPK finding: individual PK fitting IS MAP, not a Kalman filter.]
- `pa-linguistics-001` (preferential_attachment): sample-space-collapse process, explicitly an ALTERNATIVE to preferential attachment.
- `replv-mwu-noname-001` (replicator_lotka_volterra): online-learning regret (MWU) via DP/Brownian closed form, no replicator ODE.
- `sparse-finance-001` (sparse_l1_lasso): L0 best-subset (NP-hard, difference-of-convex), not L1-LASSO (the convex relaxation).
- `fft-neuro-001` (fourier_spectral): cross-channel PHASE synchronization (Hilbert) + spectral entropy, not single-series PSD.

## Tier 3 -- granularity / SHOWCASE touchpoints -> DECIDE
- `em_latent_mixture` (MIXED) = the VANCO family. PK (NPAG) = NPMLE of a mixing distribution (interior-point +
  adaptive grid); ML/physics = EM responsibility loop for a Gaussian mixture; `em-astro-001` weak. Same PROBLEM
  (latent-mixture estimation), different ALGORITHMS. Defensible under "same problem"; flagged at mechanism level.
  (The fingerprint still ranks NPAG close to the EM members -- cos 0.088 in the wild run -- so retrieval works.)
- `pca-polmeth-001` (pca_svd_lowrank) = the IDEAL-POINTS paper: your retrieval showcase (rank-3 recsys match) AND
  the related-work "ideal-point estimator = recsys matrix factorization" line. The agent flags it as a metric-
  DISTANCE latent-space model (Euclidean distance inside a logit), which the fingerprint explicitly contrasts
  with the inner-product/low-rank form. So the "ideal-points = low-rank factorization" framing for THIS paper
  needs a look (the general claim holds for IRT-style ideal points; this specific paper may be the distance form).

## Re-read under the SOLUTION-IMPORT thesis (this narrows the genuine errors)
The agents judged at the FINEST mechanism level. But solution-import wants the **same PROBLEM**, where a
*different* mechanism is the entire value of importing (you have problem P solved by a bespoke M1; you find
another field solving P by a standard M2; you import M2). And the fingerprint matches at the mechanism-CLASS
level (it ranks NPMLE and EM together at cos 0.088). So the agents over-flag relative to both. Triage:

- **Genuine errors (act):** the 3 empty/survey skeletons (no computation), plus the members that do not share
  the PROBLEM at all -- `eigen-chem-noname-001` (full spectrum, not a ranking), `irt-ecology-001` (occupancy
  GLM, not paired comparison), `mcmc-phylo-001` (diagnostics, not sampling), `fft-neuro-001` (phase coupling,
  not PSD), and `kalman-pharma-noname-001` (batch MAP, not recursive -- the defining feature of the family).
- **Defensible under "same problem" (keep, know they're there):** `em-*` NPMLE-vs-EM, `sparse-finance-001`
  L0-vs-L1, `pca-polmeth-001` distance-vs-inner-product, `pa-linguistics-001` collapse-vs-PA. Same problem,
  different mechanism = the import case. These are CANDIDATES, which is exactly how the paper frames imports.

## Implications
- **Numbers:** drop the 3 empty + decide the ~5 different-PROBLEM members; re-run the AP after cleaning.
- **Showcase line to soften (vanco lesson):** the related-work edit states the ideal-point estimator *is* a
  recsys matrix factorization. `pca-polmeth-001` is a metric-DISTANCE model, so state it as a CANDIDATE ("can
  be cast as" / "is closely related to"), not an identity. The pairing is a *fine* solution-import candidate
  (same problem: latent embedding from sparse dyadic interactions; different geometry), just not a proof.
- **The core phenomenon (same-computation cross-field families) is real and survives** -- label hygiene, not a
  thesis failure. Decide the granularity criterion (recommend: same PROBLEM = your thesis) and apply it
  consistently across all 18 families.
