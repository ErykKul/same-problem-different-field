MECHANISM: The paper computes a constrained stochastic optimization procedure involving three stages: (1) compressing a high-dimensional latent state into a low-rank tensor query using spectral hard-thresholding, (2) delegating the compressed query to an external oracle modeled as a noisy operator, and (3) updating the latent state via Riemannian optimization on fixed-rank manifolds. The compression step minimizes a quadratic distortion objective under a query-budget constraint, formalized as a rate-distortion problem. The oracle returns a noisy response, which is integrated into a differentiable loss function. The optimization occurs on a manifold defined by fixed multilinear ranks, using retraction-based Riemannian updates. Convergence guarantees are derived under assumptions of smoothness, bounded variance, and specific step-size conditions. The method involves truncating singular values below a threshold proportional to the largest singular value, projecting the tensor onto a low-rank subspace, and iteratively adjusting the latent state using stochastic gradients. The process balances information preservation (via spectral retention) against communication cost (via rank reduction), with theoretical analysis showing optimality of spectral hard-thresholding for quadratic distortion. The algorithm alternates between compression, delegation, and update phases, with each phase involving matrix operations, tensor decompositions, and manifold-specific gradient computations.  
DOMAIN: AI/ML: bounded-context reasoning  
STRUCTURE: other: Riemannian optimization on manifolds  
DATA_OBJECT: dense matrix or tensor  
INFERENCE: optimization only  
PROBLEM_FORM: optimization  
DISTRIBUTION: none  
COMPLEXITY: convergence rate  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-private-data
