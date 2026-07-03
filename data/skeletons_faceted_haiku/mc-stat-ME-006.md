MECHANISM: Decompose a time series into wavelet coefficients at multiple scales using a discrete wavelet transform with Daubechies filters. Compute harmonic regression coefficients using least absolute deviations (robust to outliers) at each scale. From these LAD regression coefficients, construct a periodogram (spectral density estimator) at a fixed resolution level. Derive the asymptotic distribution of this wavelet-based periodogram for long-memory processes with heavy-tailed innovations, showing convergence to a quadratic form in a Gaussian vector whose covariance depends on memory properties and filter choice.
DOMAIN: Robust spectral analysis of long-memory time series
STRUCTURE: spectral or transform
DATA_OBJECT: sequence or time-series
INFERENCE: frequentist point estimate
PROBLEM_FORM: estimation
DISTRIBUTION: heavy-tailed; Gaussian
COMPLEXITY: asymptotic distribution
