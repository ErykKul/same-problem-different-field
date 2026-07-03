MECHANISM: The paper computes a signal transformation using composite orthogonal matrices constructed from wavelet-like operators. The process begins by representing an input signal as a vector in ℝ^N, then applying a sequence of orthogonal matrix operations (products, Kronecker products, block-diagonal constructions) to produce a transformed coefficient vector. These matrices are designed to preserve energy and enable perfect reconstruction. The transformed coefficients are then subjected to a deterministic thresholding rule, where coefficients below a magnitude threshold are set to zero. The threshold is determined by the universal threshold formula, which depends on the noise level and the number of coefficients. After thresholding, the signal is reconstructed by applying the inverse of the composite matrix. The effectiveness of the transformation is evaluated using Lorenz curves, which quantify the concentration of energy into fewer coefficients. The method is compared across different matrix constructions (single-basis, Kronecker products, block-diagonal) under identical thresholding rules. Simulations and real-world data experiments demonstrate that composite matrices achieve greater energy concentration and lower mean-squared error than single-basis transforms. The framework is generalizable to higher-dimensional data through Kronecker extensions and adaptive block structures.  
DOMAIN: signal processing, wavelet transforms  
STRUCTURE: spectral or transform  
DATA_OBJECT: dense matrix  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: estimation  
DISTRIBUTION: none  
COMPLEXITY: polynomial iterative  
DATA_AVAILABILITY: dataset-in-repository  
CODE_AVAILABILITY: public-repository  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
