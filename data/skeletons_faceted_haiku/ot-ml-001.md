MECHANISM: Compute a minimum-cost mass-conserving coupling between two discrete distributions, a constrained linear assignment that routes mass from one distribution to the other while minimizing total transport cost subject to both marginal constraints. Add an entropy penalty to the objective, making it strictly convex and uniquely solvable. The regularized optimum is obtained by fast alternating rescaling of the rows and columns of an exponentiated-cost (Gibbs) kernel until the coupling matches both prescribed marginals. The converged coupling yields a smooth approximation to the transport cost that serves as a distance between the two distributions. The iterative scaling runs orders of magnitude faster than solving the exact linear program.
DOMAIN: machine learning
STRUCTURE: dense linear algebra
DATA_OBJECT: dense matrix or tensor
INFERENCE: optimization only
PROBLEM_FORM: optimization
DISTRIBUTION: none
COMPLEXITY: polynomial iterative
DATA_AVAILABILITY: public-benchmark-used
CODE_AVAILABILITY: public-repository
PREREGISTRATION: none
EVIDENCE_BASIS: empirical-with-released-data
