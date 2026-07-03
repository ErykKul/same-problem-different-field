MECHANISM: The paper introduces a five-parameter generalized van der Ziel–McWhorter (GVZM) power spectral density (PSD) function to model EEG noise spectra. The GVZM PSD approximates a power law $1/f^{\theta}$ in mid-frequencies while ensuring finite total power and amplitude at low frequencies. The model defines EEG periodograms as random variables scaled by a chi-square distribution with two degrees of freedom, capturing statistical variations around the mean PSD. Two real-time SSVEP frequency estimation algorithms are proposed: one based on chi-square distribution testing for frequency spikes and another using an F-distribution estimator derived from the GVZM model. The algorithms statistically outperform existing methods by leveraging the GVZM noise model's accurate representation of EEG periodograms. The model is validated through three approaches: (1) deriving it from quantum mechanical ion channel kinetics in maximum entropy equilibrium, (2) linking autoregressive time series to the GVZM PSD, and (3) demonstrating improved SSVEP estimation performance. The GVZM PSD is defined using an integral involving a modified arctangent function, with parameters interpreted as noise floor, spectral exponent, and frequency transition points. The model's statistical properties are derived from the Central Limit Theorem, ensuring asymptotic validity for large data samples. Simulations using the GVZM PSD and chi-square-distributed periodograms match recorded EEG data, confirming the model's accuracy.  
DOMAIN: neurological signal processing  
STRUCTURE: spectral or transform  
DATA_OBJECT: continuous function or field  
INFERENCE: frequentist point estimate  
PROBLEM_FORM: estimation  
DISTRIBUTION: continuous; chi-square  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-private-data
