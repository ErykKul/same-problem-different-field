MECHANISM: Specifies a nonlinear state-space model where the state transition and observation functions are modeled as Gaussian process priors. Augments the model with sparse inducing points to make inference tractable. Develops a variational Bayes approximation via an evidence lower bound (ELBO) that decouples the posterior over states, latent function values, and inducing variables. Optimizes the ELBO to find approximate posterior distributions over the state dynamics and learns hyperparameters. Enables tractable smoothing and filtering for time-series data without requiring approximation schemes that scale with trajectory length.
DOMAIN: Machine learning, time-series modeling, state-space models
STRUCTURE: other: kernel-based regression
DATA_OBJECT: sequence or time-series
INFERENCE: variational
PROBLEM_FORM: estimation
DISTRIBUTION: continuous; continuous
COMPLEXITY: polynomial iterative
