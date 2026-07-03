MECHANISM: The paper computes a variational approximation to a Bayesian posterior distribution over parameters of a multivariate regression model with dimension reduction. The method reparameterizes the posterior to address ill-conditioning, then applies coordinate-ascent variational inference (CAVI) with Laplace approximations for nonconjugate blocks. At each coordinate update, the algorithm maximizes an expectation of the log-likelihood under the current variational distribution, approximates the resulting objective with a Gaussian centered at the mode, and updates the variational factor to match this approximation. The reparameterization transforms the constrained manifold parameters into unconstrained Euclidean parameters, enabling efficient computation. The Laplace approximation replaces intractable updates by expanding the objective function around its maximum, yielding a quadratic form that defines the variational factor's mean and covariance. The procedure iterates over parameter blocks, alternating between optimizing conjugate blocks with closed-form updates and approximating nonconjugate blocks via Laplace. Theoretical analysis shows that the Laplace approximation error converges to zero asymptotically under certain regularity conditions. The method avoids sampling-based inference by directly optimizing the evidence lower bound (ELBO) through deterministic coordinate-wise updates. The algorithm maintains estimation accuracy by ensuring the variational approximation remains close to the true posterior, as validated through simulation studies and real-data analysis. The reparameterization and Laplace steps together reduce computational bottlenecks caused by high curvature and nonconjugacy in the original parameterization.  
DOMAIN: Bayesian statistics and dimension reduction models  
STRUCTURE: coordinate-ascent variational inference  
DATA_OBJECT: posterior distribution  
INFERENCE: Bayesian posterior  
PROBLEM_FORM: estimation  
DISTRIBUTION: continuous; normal and inverse-Wishart  
COMPLEXITY: polynomial iterative  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
