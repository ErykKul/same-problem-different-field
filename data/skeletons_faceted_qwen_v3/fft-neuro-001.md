MECHANISM: The paper computes three features from multichannel time-series observations: (1) power spectrum density across four frequency bands using Fourier transform and Welch's method, (2) spectral entropy calculated as the information entropy of normalized power distribution across frequency bins, and (3) phase synchronization index derived from instantaneous phase differences between signal pairs using Hilbert transforms. The process involves bandpass filtering, epoch segmentation, artifact removal through automated detection, and normalization of power measurements. For each subject, the algorithm first divides the signal into 4-second epochs, applies a Hamming window, computes 1024-point FFTs, and averages power estimates across 30 epochs. Spectral entropy is calculated by treating normalized power as a probability distribution and applying the Shannon entropy formula. Phase synchronization is quantified by computing the magnitude of the complex average of exponential terms derived from phase differences between paired signals. The method compares these features between two groups: one with diagnosed pathology and one without, and correlates the features with external cognitive test scores. No probabilistic modeling or optimization is performed; all computations are deterministic transformations of the raw signal. The output is a set of quantitative metrics used for diagnostic classification.  
DOMAIN: biomedical signal processing  
STRUCTURE: spectral or transform  
DATA_OBJECT: time-series  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: diagnosis  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-private-data
