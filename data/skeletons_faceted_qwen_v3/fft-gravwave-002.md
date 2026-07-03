MECHANISM: The paper computes a power spectral density (PSD) estimate from a time-series input using wavelet-based methods. For stationary noise, it applies wavelet smoothing to a periodogram derived from the Fourier transform of the input, avoiding segmentation steps. The wavelet transform decomposes the periodogram into approximation and detail coefficients, which are thresholded to suppress noise fluctuations. The thresholding uses percentile-based soft thresholding informed by generalized Gaussian distribution assumptions. Reconstructed coefficients are then used to estimate the PSD. For non-stationary noise, the method transforms the input into the time-frequency domain using wavelet packet decomposition, computes median values across frequency bins, and derives the PSD from these medians. The process involves discrete wavelet transforms, thresholding operations, and reconstruction algorithms. The method assumes the log-periodogram follows a distribution with additive noise modeled via the Gumbel distribution, and the wavelet coefficients are manipulated to isolate the true PSD signal. The algorithm balances frequency resolution and variance reduction without requiring data segmentation. The wavelet smoothing approach is compared to Welch’s method through metrics like frequency resolution, quality factor, and matched-filter signal-to-noise ratio.  
DOMAIN: gravitational wave data analysis  
STRUCTURE: spectral or transform  
DATA_OBJECT: sequence or time-series  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: estimation  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: dataset-with-DOI-or-handle  
CODE_AVAILABILITY: public-repository  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
