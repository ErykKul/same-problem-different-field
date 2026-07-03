MECHANISM: The paper computes a matrix autoregressive model with a separable bilinear structure to capture cross-variable and cross-node dependencies in multivariate network time series. The state matrix Y_t is expressed as Y_t = B_net Y_{t-1} B_var^T + E_t, where B_net encodes network topology via a linear combination of identity and normalized adjacency matrices, and B_var is a low-rank matrix representing latent factors. Estimation proceeds via a Scaled Gradient Descent algorithm with block-specific preconditioners to address the mismatch between rigid network scalars and flexible variable subspaces. The method establishes non-asymptotic error bounds under an equivalence-invariant distance metric, showing that estimation accuracy improves with network size for sparse graphs. The computational steps include: (1) projecting high-dimensional observations onto a low-rank subspace via B_var, (2) propagating latent factors across the network using B_net, and (3) reconstructing observed variables from propagated factors. The algorithm balances gradient scales between network and variable components to ensure convergence to the global optimum despite non-convexity. The model's structure explicitly decouples network spillovers from variable dynamics, enabling dimension reduction while preserving cross-channel interactions. Theoretical analysis demonstrates that network-induced regularization reduces variance in parameter estimation for large sparse networks.  
DOMAIN: network statistics and high-dimensional time series  
STRUCTURE: matrix autoregression  
DATA_OBJECT: matrix  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: estimation  
DISTRIBUTION: none  
COMPLEXITY: finite-sample bound  
DATA_AVAILABILITY: public-benchmark-used  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
