MECHANISM: The paper computes a statistical method for detecting periodic signals in irregularly sampled astronomical time series using the Lomb-Scargle (LS) periodogram. The algorithm calculates the power of sinusoidal fits to the data by adjusting for irregular sampling intervals, computing the best-fit amplitude and phase at each frequency. It evaluates the significance of detected periodicities by comparing the periodogram's power values to a reference distribution derived from the data's noise characteristics. The method involves transforming the time series into a frequency domain representation, accounting for the non-uniform sampling by modifying the standard Fourier transform equations. The paper discusses the theoretical challenges of applying the LS periodogram, including the reinterpretation of the Nyquist frequency in irregular sampling contexts. It compares the LS periodogram's performance to simpler techniques like the Schuster periodogram, showing that in many cases, simpler methods yield comparable results. The computation involves iterative optimization of frequency parameters and statistical hypothesis testing to determine the significance of detected signals. The paper emphasizes that while the LS periodogram recovers some statistical properties of the standard periodogram, its implementation requires careful handling of sampling irregularities and computational adjustments to avoid biases. The method is applied to light curves from astronomical observations, where the goal is to identify periodic or semi-periodic components from noisy data. The algorithm's steps include pre-processing the time series to remove trends, computing the periodogram across a range of frequencies, and post-processing to identify significant peaks. The paper concludes that the LS periodogram's advantages are context-dependent and that simpler methods may suffice for many astronomical applications.  
DOMAIN: astronomy, time series analysis  
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
