MECHANISM: The paper computes a Bayesian nonparametric estimator for a continuous function (the spectral density) using a mixture of B-spline basis functions. A Dirichlet process prior is placed on the weights of the mixture components, and another Dirichlet process prior is placed on the knot locations, which determine the shape of the B-splines. The spectral density is reparameterized as a scaled version of the B-spline mixture, ensuring integration to one. The Whittle likelihood approximation is used to construct a pseudo-posterior distribution, which combines the B-spline prior with observed data. Posterior samples are generated via a Metropolis-within-Gibbs Markov chain Monte Carlo algorithm, where parameters such as weights, knot locations, and the number of mixture components are iteratively updated. Parallel tempering is employed to improve mixing and convergence of the MCMC sampler. The method allows for data-driven selection of the number of knots and their positions, adapting to sharp features in the spectral density. The B-spline basis functions have local support, enabling accurate modeling of abrupt changes in the target function. The algorithm is evaluated through simulation studies and applied to real-world time series data, demonstrating improved performance over Bernstein polynomial priors in terms of error metrics and coverage probabilities.  
DOMAIN: time-series analysis  
STRUCTURE: other: Bayesian nonparametric model  
DATA_OBJECT: continuous function or field  
INFERENCE: Bayesian posterior  
PROBLEM_FORM: estimation  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-private-data
