MECHANISM: The paper computes a matrix completion estimator to estimate missing entries in a matrix representing outcomes for entities across time points. The method constructs a matrix where observed entries correspond to untreated entities and time points, and missing entries correspond to treated entities and time points. It assumes the matrix has a low-rank structure, which is enforced by minimizing the nuclear norm of the matrix. The optimization problem involves solving a convex program that balances the fit to observed data with the low-rank constraint. The method generalizes existing matrix completion results by allowing missing data patterns to exhibit time series dependencies, which are modeled as structured patterns in the matrix. The completed matrix is used to impute counterfactual outcomes for treated entities and time points. The approach is compared to alternative methods like synthetic control and unconfoundedness-based estimators through simulations. The algorithm iteratively refines the matrix approximation until convergence, ensuring the solution adheres to the low-rank constraint. The method does not explicitly model uncertainty in the imputed values but relies on the convex optimization to produce a single estimate. The computational steps involve forming the matrix, defining the nuclear norm objective, solving the optimization problem, and validating the results against simulated data. The method's effectiveness depends on the assumption that the true matrix is low-rank and that the missing data patterns are compatible with the time series dependencies.  
DOMAIN: causal inference and econometrics  
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
