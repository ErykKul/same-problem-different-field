MECHANISM: The paper computes a reconstruction model that enforces sparse constraints in both spatial and temporal dimensions using weighted l1 norms. The method introduces adjustable weights to balance sparsity between dimensions, and applies a modified fast iterative soft-thresholding algorithm (pFISTA) to solve the optimization problem. The algorithm alternates between applying a tight frame transform (for sparsity) and a proximal operator (for thresholding), using an undersampled k-space data matrix as input. The tight frame operators are defined as cyclic shift discrete wavelet transforms (CSDWT) for temporal sparsity and shift-invariant discrete wavelet transforms (SIDWT) for spatial sparsity. The reconstruction process involves iteratively updating an image series estimate by minimizing a weighted combination of data fidelity and sparsity terms. The algorithm guarantees convergence under specific step-size conditions, and the weights are tuned to reduce noise while preserving temporal fidelity. The method is applied to undersampled radial k-space data, which is first re-sorted into dynamic time series. The output is a reconstructed image time-series in x-y-t space, with each frame represented as a grid. The optimization problem is formulated as a convex minimization with a regularizer that combines temporal and spatial sparsity terms, and the solution is derived using proximal gradient descent steps. The algorithm's efficiency is demonstrated through empirical comparisons on in vivo datasets, showing reduced reconstruction time and improved visual quality compared to prior methods.  
DOMAIN: medical imaging  
STRUCTURE: sparse linear algebra  
DATA_OBJECT: grid or lattice  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: estimation  
DISTRIBUTION: none  
COMPLEXITY: polynomial iterative  
DATA_AVAILABILITY: public-benchmark-used  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
