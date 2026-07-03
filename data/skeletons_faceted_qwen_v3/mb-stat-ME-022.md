MECHANISM: The paper computes a weighted estimator for the mean outcome in a target population using source individual-level data and target covariate summaries. It first applies entropy balancing to adjust source data by solving an optimization problem that matches reweighted source covariate moments to target covariate summaries. The entropy balancing estimator is derived by maximizing a Lagrangian function subject to constraints that align sample moments. The estimator's asymptotic normality is established under regularity conditions, with variance estimated using a weighted covariance matrix derived from source data and target summaries. A second method introduces a flexible model-based reweighting approach, where a working model π(x;α) for the covariate shift function is calibrated to match target summaries via minimum divergence constraints. This involves minimizing an augmented objective function with constraints derived from target summary statistics, incorporating uncertainty in the summaries. The model parameters α are estimated by solving a constrained optimization problem that enforces alignment between source data and target summaries. The proposed estimator is shown to be consistent and asymptotically normal under correct model specification, with a test statistic constructed to validate the model. Both methods aim to account for covariate shift and uncertainty in target summaries, with the flexible model offering greater adaptability when the log-density ratio is nonlinear in the covariates.  
DOMAIN: causal inference and transportability  
STRUCTURE: other: constrained optimization  
DATA_OBJECT: set or table  
INFERENCE: frequentist point estimate  
PROBLEM_FORM: estimation  
DISTRIBUTION: continuous; normal  
COMPLEXITY: not stated  
DATA_AVAILABILITY: public-benchmark-used  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
