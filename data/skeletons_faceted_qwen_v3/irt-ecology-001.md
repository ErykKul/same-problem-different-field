MECHANISM: The paper computes a hierarchical Bayesian model to estimate spatially-varying regression coefficients for species-environment relationships. The process model uses a logistic transformation of a linear combination of non-spatial and spatially-varying covariate effects, where spatial effects are modeled as realizations of a smooth latent surface. Spatially-varying effects are approximated using Nearest Neighbor Gaussian Processes (NNGPs), which replace full Gaussian Process covariance matrices with conditional densities over a sparse neighbor set. The observation model assumes independent Bernoulli detections conditional on true presence, with detection probabilities modeled via logistic regression on site- or observation-level covariates. For multi-species models, a spatial factor dimension reduction is applied to jointly estimate species-specific coefficients while accounting for residual correlations. Posterior inference is performed via Gibbs sampling with Pólya-Gamma data augmentation, enabling efficient computation of posterior predictive maps with uncertainty propagation. The method accommodates both single-species and multi-species scenarios, with spatially-varying effects determined by indicator variables.  
DOMAIN: ecology, species distribution modeling  
STRUCTURE: graphical models  
DATA_OBJECT: point set  
INFERENCE: Bayesian posterior  
PROBLEM_FORM: estimation  
DISTRIBUTION: binary; Bernoulli  
COMPLEXITY: not stated  
DATA_AVAILABILITY: public-benchmark-used  
CODE_AVAILABILITY: public-repository  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
