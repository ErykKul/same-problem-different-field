MECHANISM: Precondition a posterior distribution by exploiting an estimated sparse precision matrix Q derived from Laplace approximation at the mode. Transform parameters q to q' via sparse matrix square root (q' = L'Pq where L is Cholesky decomposition of permuted Q) to decorrelate and rescale the parameter space. Use permutation algorithms to maximize sparsity in the Cholesky factor. Pass the preconditioned log-density and gradient to a Hamiltonian Monte Carlo sampler (NUTS) which generates posterior samples more efficiently by taking longer trajectories with fewer gradient evaluations.
DOMAIN: Bayesian hierarchical models and Markov chain Monte Carlo sampling
STRUCTURE: sparse linear algebra
DATA_OBJECT: sparse matrix
INFERENCE: Bayesian posterior
PROBLEM_FORM: simulation or generation
DISTRIBUTION: none
COMPLEXITY: polynomial iterative
