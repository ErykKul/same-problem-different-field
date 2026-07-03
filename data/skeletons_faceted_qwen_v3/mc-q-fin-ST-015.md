MECHANISM: The paper computes a timescale separation method for decomposing multivariate time series into slow and fast components. It formulates the problem as minimizing the drift of variance or higher-order moments under constraints, leading to generalized eigenvalue problems. For variance timescales, it minimizes the time derivative of variance for each component while enforcing a unit variance constraint, resulting in an eigenvalue problem involving autocovariance matrices. The solution involves solving a generalized eigenvalue equation where the eigenvectors represent directions of slowest/fastest decay in non-stationarity. For tail timescales, it minimizes the drift of higher-order moments (e.g., 2k-th moment) under orthogonality constraints, leading to a nonlinear optimization problem. This is solved via fixed-point iteration, which alternates between updating weight vectors and normalizing them. The method uses discretized time differences to approximate derivatives and computes autocovariance matrices with specified lags. Eigenvalues derived from these problems quantify autocorrelation and relate to relaxation timescales through a closed-form equation. The approach applies to both linear (variance-based) and nonlinear (tail-based) decompositions, with distinct computational steps for each. The method is implemented using numerical solvers for eigenvalue problems and iterative algorithms for nonlinear optimization.  
DOMAIN: financial time series analysis  
STRUCTURE: spectral or transform  
DATA_OBJECT: dense matrix  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: estimation  
DISTRIBUTION: continuous; Gaussian  
COMPLEXITY: polynomial iterative  
DATA_AVAILABILITY: public-benchmark-used  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-private-data
