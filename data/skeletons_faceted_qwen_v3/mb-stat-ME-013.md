MECHANISM: The paper computes a kernel density estimator for circular data using wrapped flat-top kernels. The method begins by defining a characteristic function for the underlying circular density, which is then transformed into a kernel function on the real line. This kernel is wrapped onto the circumference of a unit circle to create a circular kernel. The estimator is constructed by summing scaled versions of this wrapped kernel evaluated at data points. The asymptotic mean squared error (MISE) is decomposed into integrated squared bias (ISB) and integrated variance (IV) components. The ISB is derived by analyzing the Fourier coefficients of the kernel and density, while the IV is computed using the variance of the estimator. The method assumes smoothness conditions on the density (e.g., polynomial or exponential decay of Fourier coefficients) to derive convergence rates. The optimal bandwidth parameter is determined by minimizing the theoretical MISE expression, which depends on the smoothness of the density. The estimator achieves faster convergence rates than traditional methods under certain conditions, such as finite support of the characteristic function. The paper validates these results through numerical experiments and theoretical analysis of specific distributions.  
DOMAIN: circular statistics and kernel density estimation  
STRUCTURE: spectral or transform  
DATA_OBJECT: continuous function or field  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: estimation  
DISTRIBUTION: none  
COMPLEXITY: convergence rate  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: mathematical-proof
