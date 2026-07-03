MECHANISM: Formulate a hierarchical hurdle beta-binomial model for bounded counts (0 to N) with state-varying coefficients. First-stage hurdle model handles structural zeros (binary outcome: zero or positive). Second-stage conditional on non-zero: beta-binomial distribution for the count out of known total. Estimate cross-margin dependence via covariance component in hierarchical layer. Apply Cholesky-based sandwich variance calibration to account for survey weights. Compute design-effect ratio diagnostics. Derive log-scale marginal effect decompositions to translate coefficients into policy-relevant quantities.
DOMAIN: Bayesian hierarchical models for bounded counts
STRUCTURE: other: mixture/hurdle decomposition
DATA_OBJECT: table
INFERENCE: Bayesian posterior
PROBLEM_FORM: estimation
DISTRIBUTION: binary; binomial
COMPLEXITY: polynomial iterative
