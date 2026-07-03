MECHANISM: The paper computes a robust and sparse portfolio selection model by extending the classical mean-variance (MV) framework. It incorporates an ellipsoidal uncertainty set to account for parameter estimation errors and introduces fixed transaction costs as a penalty term to discourage over-diversification. The optimization problem is formulated as a mixed-integer program, which is challenging to solve for large asset universes. To address this, the authors develop a semismooth Newton-based proximal difference-of-convex algorithm. This algorithm iteratively solves a sequence of convex subproblems by decomposing the non-convex objective into the difference of two convex functions. The proximal term ensures stability, while the semismooth Newton method accelerates convergence. The algorithm is proven to converge to at least a local minimizer with a locally linear convergence rate. Analytical and numerical experiments validate the model's properties, including the one-to-one correspondence between the risk-aversion coefficient and robustness levels. The paper also characterizes how the number of traded assets varies with uncertainty levels and transaction costs. The method explicitly handles constraints on portfolio cardinality and transaction costs through the optimization formulation.  
DOMAIN: finance, portfolio optimization  
STRUCTURE: optimization  
DATA_OBJECT: set or table  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: optimization  
DISTRIBUTION: none  
COMPLEXITY: convergence rate  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: simulation-study
