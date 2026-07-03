MECHANISM: The paper computes a probabilistic model to estimate stellar variability in light curves using Gaussian processes (GPs). The method defines a mean function and a covariance matrix via kernel functions that encode different variability components (granulation, oscillation, rotation). The GP model combines these kernels to describe the light curve's stochastic and quasi-periodic features. The algorithm uses Bayesian inference to estimate hyperparameters by maximizing the log-likelihood function, which involves computing the determinant and inverse of the covariance matrix. Model comparison is performed via Bayes factors, integrating the joint posterior distribution of parameters using importance sampling. The process includes outlier rejection, binning data to reduce high-frequency noise, and fitting the best model to simulated transits to evaluate parameter recovery. The method accounts for white noise and uses Markov chain Monte Carlo (MCMC) sampling to explore the parameter space, with hyperparameters derived from posterior distributions. The model is tested on real and simulated data to assess its ability to correct stellar variability and improve transit parameter estimation.  
DOMAIN: exoplanet transit characterization  
STRUCTURE: other: Gaussian process regression  
DATA_OBJECT: sequence or time-series  
INFERENCE: Bayesian posterior  
PROBLEM_FORM: estimation  
DISTRIBUTION: continuous; continuous  
COMPLEXITY: not stated  
DATA_AVAILABILITY: dataset-with-DOI-or-handle  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
