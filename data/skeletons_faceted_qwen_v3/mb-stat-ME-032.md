MECHANISM: The paper computes a focused information criterion (FIC) to select models in semiparametric linear hazard regression. For a given focus quantity (e.g., survival probability of an entity), it estimates the mean squared error (MSE) of the estimator for that quantity. The MSE is decomposed into variance and squared bias components. The variance is estimated using a martingale-based approach, involving integrals of weight functions against observed event data. The squared bias is estimated by comparing the current model's estimator to a full-model estimator, with adjustments for variance. The FIC is the sum of the estimated variance and the truncated squared bias (non-negative). A weighted version (wFIC) extends this by integrating over a weighted loss function, where weights depend on time and covariate values. The model selection process involves ranking all $3^q$ candidate models (splitting covariates into time-varying, time-constant, or excluded) based on the FIC or wFIC score. Model averaging across top models is also discussed, using weights derived from the FIC scores. The computation relies on least squares estimation of regression functions and cumulative hazard rates, with explicit formulas for variance and bias estimation.  
DOMAIN: survival analysis  
STRUCTURE: other: model selection criteria  
DATA_OBJECT: continuous function or field  
INFERENCE: frequentist point estimate  
PROBLEM_FORM: optimization  
DISTRIBUTION: continuous; nonnegative  
COMPLEXITY: not stated  
DATA_AVAILABILITY: public-benchmark-used  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
