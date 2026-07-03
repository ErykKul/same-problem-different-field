MECHANISM: A collapsed Gibbs sampler draws from the posterior distribution of a hidden Markov model by integrating out missing observations and latent states. At each iteration, model parameters and unobserved data are sampled conditioning on observed data. The collapsed representation reduces effective dimensionality and improves mixing. Samples are aggregated to estimate posterior summaries.
DOMAIN: Hidden Markov models, missing data, Bayesian inference
STRUCTURE: finite-state machine
DATA_OBJECT: sequence or time-series
INFERENCE: Bayesian posterior
PROBLEM_FORM: estimation
DISTRIBUTION: none
COMPLEXITY: convergence rate
