MECHANISM: The paper computes a simulation-based evaluation of pulsar detection techniques by generating synthetic pulsar populations with statistical distributions of parameters such as period, luminosity, and duty cycle. These populations are modeled using a snapshot approach calibrated against existing surveys, iteratively adjusting until detection statistics match reference data. The simulation incorporates observational selection effects, including sensitivity thresholds, geometric configurations, and interstellar medium properties. For each pulsar, the model calculates signal characteristics like flux density, dispersion measure, and scintillation parameters (timescale, bandwidth) based on Galactic electron density distributions. Detection thresholds are applied across three methods: image-based SNR (image SNR > 5), time-domain SNR (SNR_p > 9), and scintillation-based correlation SNR (SNR_cor > 5). The simulation evaluates how observational parameters (frequency, bandwidth, resolution) affect detection rates for normal and millisecond pulsars. It quantifies the number of pulsars uniquely detectable by each method, identifying optimal configurations (e.g., 1420 MHz, 10 kHz channel width) that maximize detection efficiency. The model also accounts for binary pulsar challenges, such as orbital motion introducing phase variations that reduce time-domain sensitivity. Results are validated by comparing simulated detection rates with theoretical expectations and analyzing parameter dependencies (e.g., duty cycle, modulation index) that influence method-specific performance. The framework is applied to GMRT survey configurations, testing how frequency bands and channel resolutions impact scintillation detection and cross-verifying results with existing pulsar surveys.  
DOMAIN: astronomy, pulsar detection  
STRUCTURE: other: simulation  
DATA_OBJECT: set or table  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: detection or search  
DISTRIBUTION: binary; Gaussian  
COMPLEXITY: not stated  
DATA_AVAILABILITY: public-benchmark-used  
CODE_AVAILABILITY: public-repository  
PREREGISTRATION: none  
EVIDENCE_BASIS: simulation-study
