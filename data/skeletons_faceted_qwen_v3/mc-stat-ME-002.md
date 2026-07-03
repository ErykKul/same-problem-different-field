MECHANISM: The paper computes a matrix factorization under nonnegativity and row-sum constraints to decompose a data matrix into two matrices representing abundances and end-members. The method maximizes the determinant of the product of the end-member matrix with its transpose, promoting maximal volume. The optimization problem is formulated as minimizing the Frobenius norm of the difference between the observed data and the product of the abundance and end-member matrices, while maximizing the determinant of the end-member matrix. This is achieved through an alternating optimization scheme, where the abundance matrix and end-member matrix are updated iteratively. Each update step involves solving a quadratic programming subproblem with nonnegativity and row-sum constraints. The algorithm uses projected fast gradient methods for each subproblem, ensuring convergence to a local optimum. The uniqueness of the solution is guaranteed under sufficient scattered conditions, which impose constraints on the geometry of the end-member matrix. The method is compared against existing algorithms using simulated data, demonstrating improved recovery of true end-members in highly mixed datasets. The computational core involves matrix operations, determinant maximization, and constrained optimization, with no reliance on stochastic or probabilistic inference. The algorithm's structure is iterative and relies on convex subproblems for each matrix update.

DOMAIN: sedimentary geology

STRUCTURE: other: quadratic programming

DATA_OBJECT: dense matrix or tensor

INFERENCE: deterministic or closed-form

PROBLEM_FORM: estimation

DISTRIBUTION: none

COMPLEXITY: polynomial iterative

DATA_AVAILABILITY: none

CODE_AVAILABILITY: none

PREREGISTRATION: none

EVIDENCE_BASIS: simulation-study
