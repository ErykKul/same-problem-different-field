MECHANISM: A latent discrete-state model governs time-variation in parameter values. A transition matrix defines probabilities of switching between states at each time step. The likelihood factorizes over observations conditioned on the latent state sequence, which is then estimated via filtering and smoothing algorithms. State-specific parameters and state probabilities are jointly estimated from data using maximum likelihood or Bayesian approaches. Extensions include infinite state spaces via Dirichlet processes and endogenous switching where state transitions depend on the error term.
DOMAIN: econometrics and time-series analysis
STRUCTURE: graphical models
DATA_OBJECT: sequence or time-series
INFERENCE: maximum likelihood estimation; Bayesian inference via MCMC; filtering and smoothing
PROBLEM_FORM: estimation
DISTRIBUTION: depends on application; commonly Gaussian with state-dependent mean and variance; measured distribution varies
COMPLEXITY: polynomial iterative
