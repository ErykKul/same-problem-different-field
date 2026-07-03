MECHANISM: This paper computes the recovery of a dictionary matrix and sparse coefficient matrix from a given set of training signals using ℓ₁-minimization. The process begins by formulating the problem as a matrix factorization task, where a dense matrix Y is decomposed into a dictionary matrix Φ and a sparse coefficient matrix X. The ℓ₁-norm of X is minimized subject to the constraint ΦX = Y. The algorithm iteratively adjusts Φ and X to reduce the ℓ₁-norm, leveraging the sparsity of X. The paper derives algebraic conditions for local identifiability of Φ, ensuring that under certain incoherence properties of Φ and statistical properties of X (e.g., Bernoulli-Gaussian sparsity), Φ is a local minimum of the ℓ₁-criterion. The analysis involves concentration of measure arguments to show that with sufficient training samples (N ≈ CK log K), incoherent bases are locally identifiable. The method does not assume convexity, as the ℓ₁-criterion admits multiple local minima, but empirical results suggest that under the Bernoulli-Gaussian model, the true dictionary is the only local minimum up to permutation and sign ambiguities. The computation involves solving a non-convex optimization problem with constraints on the dictionary's norm and sparsity of X, using numerical descent techniques. The paper establishes theoretical guarantees for recovery based on the number of training samples, sparsity level, and coherence of the dictionary.  
DOMAIN: sparse representation and dictionary learning  
STRUCTURE: sparse linear algebra  
DATA_OBJECT: sparse matrix  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: estimation  
DISTRIBUTION: binary and sparse; sparse  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: mathematical-proof
