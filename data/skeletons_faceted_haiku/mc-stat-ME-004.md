MECHANISM: Given a sequence of observations of a function defined on a spatial domain, compute the spectral density operator through the Fourier transform of autocovariance operators. Decompose the spectral density into eigenvalues and eigenfunctions via spectral decomposition. Use a multilayer perceptron neural network to approximate sequences of functions that are Fourier transformable, thereby approximating the spectral density without explicitly computing large autocovariance kernels. The network is trained directly on grid values to produce frequency-domain representations. Key innovation: avoid the computational bottleneck of matrix operations on G×G domains by learning the spectral density through neural network composition with frequency-domain principal components.
DOMAIN: Functional time series analysis and spectral density estimation
STRUCTURE: spectral or transform
DATA_OBJECT: sequence or time-series
INFERENCE: optimization only
PROBLEM_FORM: estimation
DISTRIBUTION: continuous; continuous
COMPLEXITY: convergence rate
