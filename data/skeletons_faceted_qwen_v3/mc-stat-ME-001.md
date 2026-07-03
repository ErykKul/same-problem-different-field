MECHANISM: The paper computes a multi-resolution variable selection method for spatial point processes. It transforms the continuous point-process likelihood into a Poisson generalized linear model (GLM) with an offset using a Berman–Turner quadrature approach. A two-dimensional Haar wavelet basis expansion decomposes the spatial domain into localized resolution levels, enabling tile-specific interactions between covariates and spatial scales. The intensity function is expressed as an exponential of a linear combination of wavelet coefficients and covariates, with coefficients parameterized by resolution-specific basis functions. Regularized estimation applies LASSO or SCAD penalties to select relevant predictors at each resolution level, balancing sparsity and localized relevance. The method estimates the intensity function by maximizing a penalized composite likelihood, incorporating both global and local covariate effects. Wavelet coefficients are localized through scaling and detail subspaces, allowing detection of spatial heterogeneity in predictor relevance. The algorithm iteratively refines coefficient estimates across resolution levels, ensuring that selected predictors are both statistically significant and spatially localized. The process involves solving a convex optimization problem with constraints on coefficient magnitudes, leveraging sparse linear algebra techniques. The final model provides a resolution-dependent map of predictor importance, capturing how covariates influence event occurrence at different spatial scales.  
DOMAIN: spatial statistics and point process modeling  
STRUCTURE: sparse linear algebra  
DATA_OBJECT: grid or lattice  
INFERENCE: frequentist point estimate  
PROBLEM_FORM: estimation  
DISTRIBUTION: count; poisson  
COMPLEXITY: not stated  
DATA_AVAILABILITY: dataset-with-DOI-or-handle  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
