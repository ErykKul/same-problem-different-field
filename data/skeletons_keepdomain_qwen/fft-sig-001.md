MECHANISM: The paper computes a Bayesian nonparametric estimator for the spectral density of a stationary time series. A prior is defined as a mixture of B-spline distributions, generalizing the Bernstein polynomial prior. Whittle’s likelihood approximation is used to form a pseudo-posterior distribution over the spectral density. The number of mixture components and knot locations are determined adaptively from the data. Posterior samples are generated via a Metropolis-within-Gibbs Markov chain Monte Carlo algorithm, with parallel tempering to improve mixing. The method is evaluated through simulation studies comparing $L_1$-error and uniform coverage probabilities against the Bernstein polynomial prior. The algorithm is applied to annual sunspot data and gravitational wave detector data from LIGO’s sixth science run. The B-spline prior is shown to provide more accurate estimates for spectral densities with sharp features. The computational steps involve kernel density estimation, Bayesian updating via MCMC, and adaptive model selection for the B-spline basis. The method does not assume a parametric form for the spectral density and instead infers it through posterior sampling. The implementation relies on numerical integration of the Whittle likelihood and parallel computation for tempering.  
DOMAIN: time-series analysis and Bayesian statistics  
STRUCTURE: sampling or Monte-Carlo  
DATA_OBJECT: sequence or time-series  
INFERENCE: Bayesian posterior  
PROBLEM_FORM: estimation  
DISTRIBUTION: continuous; continuous  
COMPLEXITY: not stated  
DATA_AVAILABILITY: public-benchmark-used  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
