MECHANISM: The paper computes a two-stage regression method that transforms an observed quantity into its empirical distribution value using a smoothed cumulative distribution function (CDF), then models the transformed quantity with a beta distribution parameterized by a mean and precision. The first stage maps the original quantity to the unit interval while preserving rank order, eliminating scale-specific distortions. The second stage fits a beta regression model with a mean model linked to covariates via a link function (e.g., logit) and a precision model linked to covariates via another link function (e.g., log). Predictions are mapped back to the original scale using the empirical quantile function. The method handles heteroscedasticity and non-normality by modeling the full conditional distribution through the beta distribution's mean-precision structure, avoiding assumptions about variance functions or weighting schemes. Estimation uses maximum likelihood with numerical optimization, and inference employs bootstrap resampling to construct prediction intervals. The approach guarantees coherent predictions across percentiles by jointly modeling the entire distribution in a single likelihood, unlike quantile regression which estimates quantiles independently.  
DOMAIN: regression methods  
STRUCTURE: other: distributional modeling  
DATA_OBJECT: continuous function or field  
INFERENCE: optimization only  
PROBLEM_FORM: estimation  
DISTRIBUTION: continuous; continuous  
COMPLEXITY: not stated  
DATA_AVAILABILITY: public-benchmark-used  
CODE_AVAILABILITY: public-repository  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
