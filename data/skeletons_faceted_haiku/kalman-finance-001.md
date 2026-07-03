MECHANISM: Recursively estimate latent volatility and model parameters from noisy observed prices using Bayesian filtering. Maintain a posterior distribution over unknown quantities at each time step. For nonlinear state-transition and observation models, select the best filter (Extended Kalman Filter, Unscented Kalman Filter, or Particle Filter) at each timestep by comparing each filter's mean-squared error to the Posterior Cramer-Rao Lower Bound. Perform prediction and correction steps, then switch to whichever filter achieves the best performance relative to PCRLB at the current timestep. Calibrate model parameters via Normal Maximum Likelihood Estimation on the estimated latent process.
DOMAIN: Financial volatility modeling and parameter estimation.
STRUCTURE: dynamic programming
DATA_OBJECT: sequence or time-series
INFERENCE: Bayesian posterior
PROBLEM_FORM: estimation
DISTRIBUTION: continuous; continuous
COMPLEXITY: polynomial iterative
