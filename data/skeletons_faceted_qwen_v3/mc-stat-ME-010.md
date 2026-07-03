MECHANISM: The paper computes variable importance in regression models by decomposing a goodness-of-fit measure using Shapley values. The method involves averaging marginal contributions of each predictor across all subsets of variables, ensuring properties like monotonicity and normalization. The goodness-of-fit measure must satisfy lower and upper bounds, with the latter set to unity for interpretability. The algorithm iterates over all subsets of predictors, calculates the difference in fit when adding each predictor, and weights these differences by the number of subsets. The Shapley value for each predictor is the weighted average of these marginal contributions. For generalized linear models, the Kullback-Leibler $R^2$ is proposed as a fit measure, which reduces to classical $R^2$ in linear models and McFadden’s index in binary models. The method ensures that Shapley values are non-negative, sum to the total fit, and can be interpreted as relative or absolute importance depending on the fit measure’s bounds. The approach is deterministic, relying on combinatorial enumeration of subsets and algebraic decomposition of fit measures.  
DOMAIN: statistical regression methods  
STRUCTURE: combinatorial or NP-hard  
DATA_OBJECT: set or table  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: estimation  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: public-benchmark-used  
CODE_AVAILABILITY: public-repository  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
