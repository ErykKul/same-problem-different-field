MECHANISM: The paper computes a Bayesian inference framework that combines Gaussian-process-based emulators with Markov Chain Monte Carlo (MCMC) sampling. The method begins by training a Gaussian process on a limited set of non-LTE simulations, which are used to approximate the relationship between stellar parameters and synthetic spectra. High-dimensional spectral data is compressed into a lower-dimensional representation using principal component analysis (PCA), reducing computational complexity. The emulator then predicts spectral features for new parameter values by interpolating the PCA coefficients. These predictions are combined with a likelihood function derived from observed spectra to compute posterior distributions over stellar parameters. The MCMC algorithm explores the posterior space, generating samples that quantify uncertainties in parameter estimates. The framework ensures that uncertainties from the emulator are propagated into the final inference results, maintaining calibration of posterior distributions. The process is iterative, with the emulator's accuracy validated against direct model evaluations and applied to real stellar data for parameter recovery.  
DOMAIN: quantitative stellar spectroscopy  
STRUCTURE: other: Gaussian process emulation with MCMC  
DATA_OBJECT: grid or lattice  
INFERENCE: Bayesian posterior  
PROBLEM_FORM: estimation  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-private-data
