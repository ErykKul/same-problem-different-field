MECHANISM: The paper computes an estimator for the spectral density of a functional time series using a multilayer perceptron neural network. The method leverages the theory of spectral functional principal components to approximate the spectral density without explicitly computing autocovariance kernels, which are computationally infeasible for large grids. The estimator is trained directly on grid values of the functional time series, bypassing the need for sample autocovariance calculations. The algorithm constructs a neural network with output layers designed to approximate the spectral density operator, which is represented as an integral operator with a kernel derived from the Fourier transform of the autocovariance sequence. The network's architecture is based on linear filters and Fourier transforms, ensuring that the estimator converges to the true spectral density under general assumptions. The method is parallelizable, enabling faster computation compared to traditional approaches. The theoretical justification relies on universal approximation results in metrics relevant to the problem, demonstrating that the neural network can approximate the spectral density operator with arbitrary precision given sufficient depth and width. The estimator is deterministic, as it does not involve sampling or Bayesian inference, and it operates on functions defined over large spatial domains represented as dense grids. The approach is validated through simulations and applied to functional magnetic resonance imaging (fMRI) data, though domain-specific terms are omitted in this description. The core computation involves transforming the functional time series into a form compatible with neural network training, using spectral decomposition and Fourier analysis to approximate the spectral density operator. The method's efficiency stems from avoiding high-dimensional matrix operations associated with traditional autocovariance kernel computations.  
DOMAIN: functional time series analysis  
STRUCTURE: other: deep learning model  
DATA_OBJECT: grid or lattice  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: estimation  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-private-data
