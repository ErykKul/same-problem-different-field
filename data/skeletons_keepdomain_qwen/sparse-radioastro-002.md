MECHANISM: The paper computes signal reconstruction from incomplete and noisy Fourier measurements using convex optimization. It formulates the problem as a global minimization of a convex objective function that incorporates sparsity constraints and optional prior information about the signal structure. The optimization balances fidelity to the measurements against the sparsity of the reconstructed signal, using a regularization term weighted by a user-defined parameter. The method replaces the standard CLEAN algorithm's local greedy approach with a global convex optimization framework, which allows for more accurate reconstructions when prior information is available. The algorithm iteratively solves the convex problem using proximal gradient methods or similar techniques, with convergence guarantees under certain conditions. The paper evaluates the method on simulated datasets representing two distinct signal types: compact astrophysical sources and cosmic string imprints in the cosmic microwave background. The simulations use generic interferometric configurations to test robustness across different observational scenarios. The method's performance is quantified by comparing reconstructed images to ground-truth signals in terms of resolution, noise suppression, and fidelity to prior constraints. The approach is applicable to any signal that can be represented as a sparse or compressible vector in a Fourier basis, with potential extensions to other transform domains. The paper does not implement the algorithm in software but provides theoretical justification for its use in radio interferometry.  
DOMAIN: radio interferometry and compressed sensing  
STRUCTURE: sparse linear algebra  
DATA_OBJECT: sparse matrix  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: estimation  
DISTRIBUTION: none  
COMPLEXITY: polynomial iterative  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: simulation-study
