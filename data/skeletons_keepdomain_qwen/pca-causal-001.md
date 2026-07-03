MECHANISM: The paper computes a matrix completion estimator for causal panel data models by constructing a matrix of control outcomes where some entries are observed and others are missing. It imputes missing entries using a nuclear norm minimization approach, which enforces low-rank structure on the matrix to approximate the original incomplete matrix. The method generalizes existing matrix completion results by allowing missing data patterns to exhibit time series dependencies, rather than assuming arbitrary missingness. The imputed matrix is used to estimate counterfactual outcomes for treated units/periods by leveraging the completed control outcomes. The approach connects matrix completion to interactive fixed effects models and synthetic control methods, showing how these frameworks relate through their assumptions about unobserved heterogeneity. The estimator is evaluated in simulations using real data, where it outperforms unconfoundedness-based and synthetic control estimators in terms of accuracy for counterfactual prediction. The algorithm involves solving a convex optimization problem with constraints derived from the nuclear norm, which penalizes matrices with high rank. The time series dependency in missing data is modeled by incorporating temporal correlation structures into the matrix completion objective function. The method assumes that the true underlying matrix has low rank, which is a key assumption for the success of nuclear norm minimization. The paper does not explicitly describe the implementation of the optimization solver but relies on standard convex optimization techniques.  
DOMAIN: causal inference in econometrics  
STRUCTURE: other: matrix completion  
DATA_OBJECT: dense matrix or tensor  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: estimation  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: simulation-study
