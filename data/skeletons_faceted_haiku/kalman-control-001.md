MECHANISM: Recursively estimate latent system state from noisy sequential observations. Maintain a posterior distribution over the state at each time step. For nonlinear state-transition and observation models, linearize the dynamics around the current state estimate (Extended Kalman Filter) or use deterministic sampling of representative points around the mean to approximate the posterior (Unscented Kalman Filter). Perform prediction: apply the dynamics model and propagate uncertainty via Jacobians or sample transformation. Perform correction: compute residual between observed and predicted measurement, scale by the Kalman gain, and update state and error covariance.
DOMAIN: Control systems and power grid state estimation.
STRUCTURE: dynamic programming
DATA_OBJECT: sequence or time-series
INFERENCE: Bayesian posterior
PROBLEM_FORM: estimation
DISTRIBUTION: continuous; continuous
COMPLEXITY: polynomial iterative
