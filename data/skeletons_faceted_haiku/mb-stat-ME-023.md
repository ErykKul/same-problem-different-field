MECHANISM: Fit separate Gaussian process models to low-fidelity and high-fidelity simulation data, then combine via calibration structure: high-fidelity output equals scaled low-fidelity output plus discrepancy term. Estimate the scaling parameter via marginal likelihood maximization. Use leave-one-out cross-validation to quantify uncertainty in parameter estimates. Derive posterior predictive distribution for high-fidelity response via conditional Gaussian identities. Optimize objective functions by searching candidate input space and computing expected objective under posterior predictive distribution, accounting for parameter and prediction uncertainty.
DOMAIN: Bayesian calibration and multi-fidelity optimization
STRUCTURE: spectral or transform
DATA_OBJECT: continuous function or field
INFERENCE: Bayesian posterior
PROBLEM_FORM: optimization
DISTRIBUTION: continuous; continuous
COMPLEXITY: polynomial iterative
