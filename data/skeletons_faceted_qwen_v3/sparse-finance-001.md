MECHANISM: The paper computes a robust and sparse portfolio optimization model that balances variance, worst-case value-at-risk, and fixed transaction costs. The model is formulated as a convex optimization problem with an ellipsoidal uncertainty set and cardinality constraints. The algorithm iteratively solves subproblems using second-order information, approximating the original problem as a difference-of-convex (DC) problem. A proximal DC algorithm is applied, where each subproblem is solved with a semismooth Newton method. The algorithm ensures convergence to a local minimizer with a locally linear convergence rate. The model incorporates a risk-aversion coefficient and uncertainty level, which are linked through a one-to-one correspondence. The solution involves convex combinations of benchmark portfolios, such as mean-variance and minimum-variance portfolios. The algorithm is generalized to handle large-scale instances by reducing dimensionality based on active assets. The computational steps include matrix inversion, quadratic programming, and proximal updates. The method is validated against exact solutions from CPLEX and benchmark portfolios. The analysis characterizes how portfolio cardinality changes with uncertainty levels and transaction costs. The algorithm's efficiency is demonstrated through numerical experiments on real-world datasets.  
DOMAIN: financial optimization and robust statistics  
STRUCTURE: other: proximal difference-of-convex algorithm  
DATA_OBJECT: dense matrix  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: optimization  
DISTRIBUTION: none  
COMPLEXITY: NP-hard; local linear convergence rate  
DATA_AVAILABILITY: dataset-with-DOI-or-handle  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
