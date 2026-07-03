MECHANISM: The paper computes the recovery of a dictionary matrix Φ and sparse coefficient matrix X from a given matrix Y=ΦX using ℓ₁-minimisation. It formulates the problem as an optimisation over Φ and X with sparsity constraints on X. Algebraic conditions for local identifiability of (Φ,X) are derived by analysing the Hessian of the ℓ₁-criterion. These conditions are generalised to the case where Φ is a basis. Under a Bernoulli-Gaussian sparse model for X, the paper shows that incoherent bases are locally identifiable with high probability when N≈CK log K. The analysis involves bounding the probability of failure using concentration inequalities for random matrices. The method does not assume convexity of the ℓ₁-criterion but derives sufficient conditions for local minima. The key computation involves verifying the algebraic conditions on the Hessian and the probabilistic properties of the coefficient matrix. The result contrasts with prior work requiring combinatorially many samples by showing logarithmic dependence on K. The paper does not implement the method computationally but focuses on theoretical guarantees of identifiability.  
DOMAIN: signal processing and sparse representation  
STRUCTURE: sparse linear algebra  
DATA_OBJECT: sparse matrix  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: estimation  
DISTRIBUTION: continuous; sparse  
COMPLEXITY: finite-sample bound  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: mathematical-proof
