MECHANISM: The paper computes a Bayesian inference framework to estimate miscentering parameters in galaxy cluster profiles. It defines a halo model with an orbiting term, parameterized by density scale, truncation radius, and shape parameters. For each halo, the 3D density profile is projected into 2D using line-of-sight integration. Miscentering is modeled as a Rayleigh distribution of offsets, with a fraction of halos miscentered. The stacked profile approach integrates miscentered profiles weighted by their distribution, while the Gaussian mixture model combines individual halo likelihoods. The likelihood function uses a Gaussian distribution for observed data, comparing measurements to model predictions with a covariance matrix. The mixture model explicitly includes miscentering parameters in the likelihood, contrasting with the stacked model's implicit integration. Bayesian MCMC sampling is used to infer parameters, marginalizing over halo structure parameters to isolate miscentering constraints. The method is validated against simulated data from IllustrisTNG, comparing posterior estimates to true values.  
DOMAIN: astrophysics, galaxy cluster analysis  
STRUCTURE: other: Gaussian mixture model  
DATA_OBJECT: sequence or time-series  
INFERENCE: Bayesian posterior  
PROBLEM_FORM: estimation  
DISTRIBUTION: continuous; Rayleigh  
COMPLEXITY: not stated  
DATA_AVAILABILITY: dataset-with-DOI-or-handle  
CODE_AVAILABILITY: public-repository  
PREREGISTRATION: none  
EVIDENCE_BASIS: simulation-study
