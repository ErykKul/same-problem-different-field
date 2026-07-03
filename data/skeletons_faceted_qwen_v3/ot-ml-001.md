MECHANISM: The paper computes a distance metric between two distributions by solving a regularized optimal transport problem. The method introduces an entropic regularization term to the classical transportation problem, transforming it into a differentiable optimization problem. The regularization ensures the solution can be computed efficiently using iterative matrix scaling. The algorithm alternates between scaling the rows and columns of a matrix to satisfy marginal constraints while minimizing the regularized objective function. The process involves iteratively updating the matrix entries until convergence, leveraging the properties of the entropy function to ensure numerical stability. The final output is a distance measure that satisfies the properties of a metric. The method's efficiency arises from the separability of the regularization term, which allows for fast computation using the Sinkhorn-Knopp algorithm. The algorithm's convergence is guaranteed under standard assumptions on the input matrices. The approach avoids solving the original linear program directly, instead approximating the solution through a sequence of matrix operations. The resulting distance is shown to be equivalent to the original optimal transport distance under certain conditions. The method's performance is validated through empirical comparisons on benchmark datasets.  
DOMAIN: optimal transportation theory  
STRUCTURE: other: matrix scaling algorithm  
DATA_OBJECT: dense matrix  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: estimation  
DISTRIBUTION: none  
COMPLEXITY: polynomial iterative  
DATA_AVAILABILITY: public-benchmark-used  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
