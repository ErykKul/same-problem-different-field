MECHANISM: The paper introduces a generalized van der Ziel–McWhorter (GVZM) power spectral density (PSD) function to model electroencephalogram (EEG) noise spectra. The GVZM PSD is derived from a maximum entropy equilibrium of ion channel populations, characterized by a $1/f^{\theta}$ behavior in mid-frequencies without singularities. The model is validated through three approaches: (1) theoretical derivation of GVZM PSDs from ion channel dynamics, (2) construction of mixed autoregressive models whose periodograms asymptotically approach GVZM PSDs, and (3) development of two real-time algorithms for estimating steady-state visual evoked potential (SSVEP) frequencies. The algorithms use statistical methods to analyze SSVEP signals, including spectral estimation and hypothesis testing for frequency detection. The GVZM model is compared to existing SSVEP estimators via pairwise statistical tests, demonstrating improved accuracy. The computational steps involve spectral density modeling, autoregressive simulation, and real-time signal processing with statistical inference. The model's parameters are estimated using maximum entropy principles and validated against empirical EEG data. The algorithms for SSVEP frequency estimation employ spectral analysis techniques and are evaluated for their convergence and accuracy in real-time scenarios. The paper emphasizes the GVZM model's ability to capture EEG noise characteristics across a wide frequency range while maintaining computational tractability.  
DOMAIN: neurophysiological signal modeling  
STRUCTURE: spectral or transform  
DATA_OBJECT: continuous function or field  
INFERENCE: frequentist point estimate  
PROBLEM_FORM: estimation  
DISTRIBUTION: continuous; continuous  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-private-data
