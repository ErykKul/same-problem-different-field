MECHANISM: The paper computes a statistical measure of similarity between an irregularly sampled time series and a set of sinusoidal functions with varying frequencies. It begins by defining a generalization of the Fourier transform for irregular sampling, where the periodogram is calculated as the squared magnitude of a complex-valued transform of the time series. This transform is derived by solving a least-squares optimization problem to fit sinusoidal components to the data, with coefficients determined by solving a system of linear equations involving sums of cosine and sine terms evaluated at the sampling times. The energy associated with each frequency is computed as the squared norm of the optimal sinusoidal fit, normalized by the number of samples. The method adjusts for irregular sampling by modifying the statistical properties of the periodogram, including deriving the distribution of the periodogram values under the assumption of Gaussian noise. It also addresses the issue of aliasing by analyzing the relationship between the Nyquist frequency and the sampling pattern, showing that irregular sampling allows detection of higher frequencies than regular sampling. The paper compares the Lomb-Scargle periodogram with simpler techniques, emphasizing that while the former provides more accurate statistical properties, simpler methods often yield comparable results with lower computational cost. The algorithm involves iterative computation of the periodogram across a range of frequencies, with thresholds for false alarm rates derived from the assumed noise distribution.  
DOMAIN: astronomy  
STRUCTURE: spectral or transform  
DATA_OBJECT: sequence or time-series  
INFERENCE: frequentist point estimate  
PROBLEM_FORM: estimation  
DISTRIBUTION: continuous; exponential  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: simulation-study
