MECHANISM: The paper computes a parameter estimation method for time series with missing data using an iterative multiple imputation approach. Given an initial parameter estimate, missing values are imputed by reconstructing the systematic component of the model and sampling from a conditional distribution derived from the observed data. This process generates multiple complete datasets, each with imputed values that preserve the dependence structure of the original time series. Parameters are reestimated using each completed dataset, and the results are combined through pooling to produce a final parameter estimate. The algorithm iterates this process, updating the parameter estimate and imputing missing values based on the latest estimate until convergence is achieved. The method ensures that the imputed values maintain the distributional and dependence properties of the observed data, minimizing distortions caused by missingness. The iterative nature of the algorithm allows it to propagate the conditional dependence structure through missing data, improving the accuracy of parameter estimation. The method is compatible with any estimator in observation-driven models, making it broadly applicable. Under general conditions, the algorithm is proven to converge almost surely to the true parameter value, regardless of the missing data mechanism or proportion of missingness. The process involves reconstructing the systematic component using the previous parameter estimate and observed values, then sampling from the conditional distribution to impute missing entries. This reconstruction and sampling step is repeated iteratively, with each iteration refining the parameter estimate and improving the alignment between the imputed series and the observed data. The final estimate is obtained by averaging results across multiple imputations, accounting for uncertainty introduced by the imputation process.  
DOMAIN: time series analysis  
STRUCTURE: other: iterative parameter estimation  
DATA_OBJECT: sequence or time-series  
INFERENCE: sampling or Monte-Carlo  
PROBLEM_FORM: estimation  
DISTRIBUTION: continuous; continuous  
COMPLEXITY: consistency  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: simulation-study
