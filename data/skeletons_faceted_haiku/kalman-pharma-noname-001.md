MECHANISM: Estimate individual parameters of a nonlinear population model by minimizing an objective function that combines prediction error and prior information. Given observations, covariates, a fixed population model with fixed covariance matrices, compute predicted values using differential equation solvers. Construct the objective function as negative log-likelihood of observations plus a penalty term (Bayesian prior) on the individual deviations from population mean. Optimize the objective function via gradient-based nonlinear optimization (limited-memory BFGS with box constraints) to find the maximum a posteriori estimate. This is a static Bayesian inference problem (not filtering).
DOMAIN: Pharmacokinetics and therapeutic drug monitoring.
STRUCTURE: optimization only
DATA_OBJECT: dense matrix or tensor
INFERENCE: Bayesian posterior
PROBLEM_FORM: estimation
DISTRIBUTION: continuous; continuous
COMPLEXITY: polynomial iterative
