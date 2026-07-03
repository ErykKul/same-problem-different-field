MECHANISM: The paper computes features from resting-state EEG recordings by first segmenting the EEG signal into four frequency bands (δ: 1–4 Hz, θ: 4–8 Hz, α: 8–13 Hz, β: 13–30 Hz) using spectral decomposition. For each frequency band, it calculates power spectral density (PSD) to quantify oscillation power, computes spectral entropy (SE) as a measure of signal complexity, and derives phase synchronization index (PSI) by analyzing inter-channel phase coherence across left/right frontal, temporal, central, and occipital brain regions. These features are extracted separately for 30 normal control (NC) subjects and 30 probable Alzheimer’s disease (AD) patients. The paper then compares group differences in these features using statistical tests, identifies correlations between AD group features and cognitive scores (MMSE/MoCA), and evaluates the discriminative potential of α power and β PSI for AD screening. No novel algorithmic steps are described beyond standard signal processing and statistical comparison methods. The analysis is deterministic, with no explicit modeling of uncertainty or probabilistic inference. The computational workflow is applied to time-series EEG data without modifying the underlying signal processing pipeline. The paper does not claim to develop new computational methods but applies existing techniques to a specific biomedical application.  
DOMAIN: biomedical signal processing, neurodegenerative disease  
STRUCTURE: other: signal processing and statistical analysis  
DATA_OBJECT: sequence or time-series  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: estimation  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-private-data
