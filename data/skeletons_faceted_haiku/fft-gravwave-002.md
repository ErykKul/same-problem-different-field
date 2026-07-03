MECHANISM: Estimates the power spectral density (PSD) of a noisy time series using wavelet transforms. For stationary noise, decomposes the logarithm of the periodogram via discrete wavelet transform, applies percentile soft thresholding to detail coefficients to remove fluctuation noise, then reconstructs the PSD estimate. For non-stationary noise, applies wavelet packet transform to the time series, squares the packet coefficients, and takes the median across frequency bands. Both approaches avoid the variance-resolution trade-off inherent in traditional periodogram methods by operating in the wavelet domain rather than requiring data segmentation.
DOMAIN: Signal processing, gravitational wave data analysis, spectral estimation
STRUCTURE: spectral or transform
DATA_OBJECT: sequence or time-series
INFERENCE: frequentist point estimate
PROBLEM_FORM: estimation
DISTRIBUTION: continuous; continuous
COMPLEXITY: polynomial iterative
