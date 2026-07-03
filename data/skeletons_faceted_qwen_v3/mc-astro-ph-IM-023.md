MECHANISM: The paper computes satellite lifetime predictions by simulating orbital decay using a semianalytic propagator that integrates mean orbital elements under atmospheric drag and J2 perturbations. It estimates ballistic coefficients from TLE data and space weather records, then performs Monte Carlo simulations to quantify uncertainty in deorbit dates. The validation process compares predicted deorbit times against historical data, adjusting for space weather forecasts and drag coefficient estimation errors. The algorithm iteratively propagates orbits with adaptive timesteps, calculates atmospheric density using NRLMSISE-00, and applies Gauss-Legendre quadrature to average perturbations. It uses a log-uniform distribution to disperse drag parameters, generating ensembles of predictions. Error metrics include median bias, continuous ranked probability score (CRPS), and Cramér-von Mises (CvM) calibration of percentile ranks. The method accounts for process noise through dispersion factors and filters out non-stationary perturbations like maneuvering or cross-tagging. Final accuracy is evaluated by comparing predicted distributions against actual deorbit dates across 934 satellites.  
DOMAIN: satellite lifetime prediction  
STRUCTURE: simulation or generation  
DATA_OBJECT: sequence or time-series  
INFERENCE: sampling or Monte-Carlo  
PROBLEM_FORM: prediction or classification  
DISTRIBUTION: continuous; continuous  
COMPLEXITY: not stated  
DATA_AVAILABILITY: public-benchmark-used  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
