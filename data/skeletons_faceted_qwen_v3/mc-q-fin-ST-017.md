MECHANISM: The paper computes distributional comparisons and tail analysis of lead-time data by transforming daily bookings into probability vectors constrained to sum to one. It applies Wasserstein distance to quantify divergence between volume and revenue distributions, detecting structural breaks using Bai-Perron tests with HAC standard errors. For tail analysis, it fits generalized Pareto distributions (GPD) via peak-over-threshold methods, assessing threshold stability. Parametric models (Gamma, Weibull, Lognormal) are fitted to daily probability mass functions using interval-censored cross-entropy minimization, which maps discrete observations to continuous distributions. Nonparametric generalized additive models (GAMs) are also evaluated for comparison. The process involves estimating shape parameters for GPD, computing tail-mass ratios, and comparing model performance via proper scoring rules (CRPS). All steps respect the compositional nature of the data, avoiding direct regression on constrained proportions. The analysis includes synthetic sampling to approximate integrals under the estimated distribution and evaluates model robustness across different lead-time thresholds.  
DOMAIN: tourism demand forecasting  
STRUCTURE: other: statistical modeling  
DATA_OBJECT: probability vector  
INFERENCE: optimization only  
PROBLEM_FORM: estimation  
DISTRIBUTION: proportion or bounded; Gamma, Weibull, Lognormal, GPD  
COMPLEXITY: not stated  
DATA_AVAILABILITY: proprietary  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-private-data
