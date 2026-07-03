MECHANISM: The paper computes a generalization bound for learning operators using random feature approximations of vector-valued kernels. It begins by representing the target operator as an integral over a probability space, then approximates this integral with a finite sum of random features sampled from the same space. These features are used to construct an explicit feature map that replaces the original kernel, reducing computational complexity. The method applies spectral regularization to the feature map, solving a regularized optimization problem that balances approximation error and generalization. The regularization function is defined through spectral filtering, which depends on the eigenvalues of the empirical covariance operator derived from the data. The solution is expressed as a linear combination of the random features, weighted by coefficients determined through gradient descent or accelerated variants. The analysis derives convergence rates for the approximation error, showing that the number of random features required scales with the square root of the dataset size. It also establishes minimax-optimal learning rates under both well-specified and misspecified conditions, accounting for the discrepancy between the true operator and the RKHS induced by the kernel. The method is applied to neural operators, where the input and output spaces are function spaces, and the random features are generated through nonlinear transformations of the input functions. The theoretical guarantees are derived using tools from functional analysis, including Hilbert-Schmidt operators and reproducing kernel Hilbert spaces, and are validated through numerical illustrations in the appendix.  
DOMAIN: machine learning: kernel methods and neural operators  
STRUCTURE: spectral or transform  
DATA_OBJECT: function or field  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: estimation  
DISTRIBUTION: none  
COMPLEXITY: convergence rate  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: mathematical-proof
