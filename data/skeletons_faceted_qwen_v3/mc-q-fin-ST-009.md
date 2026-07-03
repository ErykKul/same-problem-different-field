MECHANISM: The paper computes a two-stage LASSO regression to identify significant factors explaining cross-sectional returns. In the first stage, a penalized least-squares objective minimizes the deviation between observed returns and a linear combination of control factors, selecting those with non-zero coefficients as effective predictors. In the second stage, each test factor is regressed on the selected control factors to identify additional confounders with non-zero coefficients. The union of these sets forms the final predictor set for an ordinary least squares (OLS) regression. The method explicitly penalizes model complexity via L1 regularization, ensuring sparsity while mitigating omitted variable bias. The algorithm iteratively refines factor selection by alternating between estimating factor loadings and filtering confounders, with final inference based on heteroscedasticity-robust standard errors. The process is applied to high-dimensional data, balancing model fit and interpretability through regularization strength tuning. The method guarantees consistency under sparsity assumptions and avoids overfitting by leveraging cross-validation for hyperparameter selection. The final model combines both strong and weak but relevant factors to explain returns, with significance determined by t-statistics on estimated coefficients. The approach is tailored to financial data but described in generic mathematical terms without domain-specific variables.  
DOMAIN: asset pricing and factor investing  
STRUCTURE: sparse linear algebra  
DATA_OBJECT: dense matrix or tensor  
INFERENCE: frequentist point estimate  
PROBLEM_FORM: estimation  
DISTRIBUTION: none  
COMPLEXITY: consistency  
DATA_AVAILABILITY: public-benchmark-used  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
