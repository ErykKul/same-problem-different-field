MECHANISM: A Bayesian envelope model performs dimension reduction in multivariate regression by identifying a low-dimensional subspace containing predictor information. Variational inference approximates the posterior distribution through a reparameterized representation that improves conditioning. A coordinate-ascent variational inference algorithm iteratively optimizes variational factors. For nonconjugate likelihood terms, a Laplace approximation (second-order Taylor expansion of the log-likelihood) is used to create a tractable variational factor within each coordinate update. The algorithm alternates between updating the subspace parameters and updating variance parameters, using the Laplace approximation to handle the nonconjugate terms. Convergence is established in the limit of the Laplace approximation error.
DOMAIN: Bayesian inference and dimension reduction
STRUCTURE: other: variational inference with Laplace approximation
DATA_OBJECT: dense matrix or tensor
INFERENCE: variational
PROBLEM_FORM: estimation
DISTRIBUTION: continuous
COMPLEXITY: polynomial iterative
