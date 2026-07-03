MECHANISM: The paper computes market regime identification and intra-regime return dynamics using a pipeline involving three stages. First, it decomposes a time-series of observations into intrinsic mode functions (IMFs) via empirical mode decomposition, then applies the Hilbert transform to obtain instantaneous amplitudes, frequencies, and energies. Instantaneous energy is normalized and thresholded to identify three regimes: Normal, High, and Extreme. Second, it applies Holo-Hilbert Spectral Analysis (HHSA) to the IMFs, decomposing them into amplitude-modulation components. This yields carrier frequencies (dominant oscillatory time scales) and amplitude-modulation frequencies (temporal variations in oscillation strength), with amplitude-modulation energy quantifying volatility intensity. Third, it discretizes the original time-series into five quintile states based on full-sample quantiles, then estimates Variable-Length Markov Chains (VLMC) using context trees to model transitions between these states within each regime. Unconditional state probabilities and conditional transition metrics (e.g., self-persistence, mean-reversion, continuation, exhaustion) are computed to characterize regime-specific dynamics. The method relies on deterministic calculations for regime thresholds, frequentist estimation of VLMC parameters, and spectral decomposition for volatility profiling. No closed-form solutions are derived; instead, the pipeline combines adaptive time-frequency analysis with probabilistic modeling of discrete-state transitions. The output includes regime-specific volatility signatures and transition matrices that capture asymmetry, persistence, and predictability across market states.  
DOMAIN: financial time series analysis  
STRUCTURE: spectral or transform  
DATA_OBJECT: sequence or time-series  
INFERENCE: frequentist point estimate  
PROBLEM_FORM: estimation  
DISTRIBUTION: discrete; discrete  
COMPLEXITY: not stated  
DATA_AVAILABILITY: public-benchmark-used  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
