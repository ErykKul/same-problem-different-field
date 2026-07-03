MECHANISM: The paper computes a wavelet-based method for estimating power spectral density (PSD) from gravitational wave detector data. For stationary noise, it applies wavelet smoothing directly to the periodogram, avoiding segmentation steps used in the Welch method. This involves decomposing the periodogram into wavelet coefficients, applying a thresholding or smoothing operation to suppress noise, and reconstructing the PSD. For non-stationary noise, the method computes wavelet packet coefficients across frequency bins, then takes the median of these coefficients to estimate the PSD. The wavelet packet decomposition is performed using a discrete wavelet transform with a specified mother wavelet, and the median operation is applied independently to each frequency bin. The method claims improved frequency resolution and reduced variance compared to Welch's method for stationary noise, and greater robustness for non-stationary noise. The wavelet parameters (e.g., decomposition level, thresholding rule) are chosen based on the characteristics of gravitational wave detector noise. The algorithm is implemented as a sequence of transform, thresholding, and aggregation operations on the input time-series data. The output is a PSD estimate that can be used for matched filtering and parameter estimation in gravitational wave data analysis. The method does not assume parametric forms for the noise distribution and relies on the properties of wavelet transforms for noise suppression and spectral estimation.

DOMAIN: gravitational wave data analysis

STRUCTURE: spectral or transform

DATA_OBJECT: sequence or time-series

INFERENCE: deterministic or closed-form

PROBLEM_FORM: estimation

DISTRIBUTION: none

COMPLEXITY: not stated

DATA_AVAILABILITY: none

CODE_AVAILABILITY: none

PREREGISTRATION: none

EVIDENCE_BASIS: empirical-with-private-data
