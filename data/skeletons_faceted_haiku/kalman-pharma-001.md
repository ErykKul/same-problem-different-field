MECHANISM: Estimate time-varying parameters of a nonlinear dynamical system by augmenting the state vector with unknown parameters as additional states. Use cubature Kalman filtering, which approximates nonlinear integrals via symmetric spherical cubature rules applied to Gaussian distributions. For numerical stability, perform filtering via Cholesky factorization of covariance matrices (square root algorithm). Couple the cubature filter with multiple-model hypothesis testing: maintain a bank of filters corresponding to discrete parameter hypotheses (e.g., different input delays), compute prediction residuals for each, update posterior probabilities, and select the most likely model. Parameters follow random-walk process models; discrete-valued unknowns use model selection.
DOMAIN: Pharmacology and medical dynamical systems.
STRUCTURE: dynamic programming
DATA_OBJECT: sequence or time-series
INFERENCE: Bayesian posterior
PROBLEM_FORM: estimation
DISTRIBUTION: continuous; continuous
COMPLEXITY: polynomial iterative
