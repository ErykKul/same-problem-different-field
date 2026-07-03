MECHANISM: This paper computes the asymptotic distribution of a wavelet-based NKK periodogram derived from least absolute deviations (LAD) harmonic regression. The process begins by applying a wavelet transform to decompose an input sequence into scale-specific components, represented as wavelet coefficients. These coefficients are then modeled using harmonic regressors, which are sinusoidal functions parameterized by frequency and phase. The LAD estimator is applied to these regressors to robustly estimate the harmonic parameters, minimizing the sum of absolute deviations rather than squared errors. The resulting parameter estimates are used to construct the NKK periodogram, which is a quadratic form of the estimated parameters scaled by a factor dependent on the sample size. The paper analyzes the limiting behavior of this periodogram under long-range dependence, showing that it converges in distribution to a nonstandard limit characterized as a quadratic form in a Gaussian random vector. The covariance structure of this Gaussian vector depends on the memory properties of the underlying process and the wavelet filters used. The analysis involves deriving the asymptotic distribution of the LAD estimator through a change of variables and renormalization, leading to a central limit theorem for the transformed objective function. The final result establishes the theoretical foundation for using robust wavelet-based periodograms in spectral analysis of long-memory time series with heavy-tailed innovations.  
DOMAIN: time series analysis with long-range dependence  
STRUCTURE: spectral or transform  
DATA_OBJECT: sequence or time-series  
INFERENCE: frequentist point estimate  
PROBLEM_FORM: proof or characterization  
DISTRIBUTION: none  
COMPLEXITY: closed-form  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: mathematical-proof
