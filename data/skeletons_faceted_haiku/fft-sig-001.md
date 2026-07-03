MECHANISM: Estimates the power spectral density of a stationary univariate time series in a Bayesian nonparametric framework. Specifies a prior over spectral density functions using a mixture of B-spline basis functions with unknown number of components and knot locations. Uses Whittle's likelihood approximation to form the pseudo-posterior distribution. Draws samples from the posterior via Metropolis-within-Gibbs MCMC with parallel tempering. Infers both the spectral function and the prior specification (number of components, knot positions) from data.
DOMAIN: Signal processing, time series analysis, Bayesian spectral estimation
STRUCTURE: spectral or transform
DATA_OBJECT: sequence or time-series
INFERENCE: Bayesian posterior
PROBLEM_FORM: estimation
DISTRIBUTION: continuous; continuous
COMPLEXITY: polynomial iterative
