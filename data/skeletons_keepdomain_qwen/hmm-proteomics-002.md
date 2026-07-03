MECHANISM: The paper computes a secondary structure prediction method by refining conformation states from quintuplets of residues instead of single residues, capturing conformational correlations. It combines hidden Markov models (HMMs) with sliding window scores derived from Chou-Fasman propensities, which are estimated under an approximation of conditional independency. The sliding window scores are calculated for each residue using varying window widths, with the optimal width determined empirically as 17. The HMMs are trained on the amino acid sequence, incorporating the window scores as features to model the probabilistic transitions between conformational states. The method ignores the duration effect of conformational segment lengths due to their narrow distribution range. The prediction process involves applying the trained HMM to new sequences, using the sliding window scores to refine state probabilities. The accuracy of the method is evaluated empirically, achieving approximately 70% accuracy on the test data. The computation involves no explicit optimization or sampling steps beyond the HMM training and prediction phases. The Chou-Fasman propensities are approximated as fixed values, not estimated from data, and the HMM parameters are learned using maximum likelihood estimation. The method does not explicitly model uncertainty in the predictions, treating them as point estimates based on the learned model. The sliding window scores are computed independently for each residue position, aggregated over the window, and then combined with the HMM's state transitions to produce the final prediction. The overall algorithm is deterministic in its application of the HMM and sliding window features, with no explicit Bayesian inference or resampling steps involved.
DOMAIN: computational biology - protein structure prediction
STRUCTURE: graphical models
DATA_OBJECT: sequence or time-series
INFERENCE: none
PROBLEM_FORM: prediction or classification
DISTRIBUTION: none
COMPLEXITY: not stated
DATA_AVAILABILITY: none
CODE_AVAILABILITY: none
PREREGISTRATION: none
EVIDENCE_BASIS: empirical-with-private-data
