MECHANISM: The paper computes a velocity correction factor ω by applying a formula to pairs of extreme observations (innermost and outermost entities in a radial dataset). For each entity, it calculates ω using the difference between two scaled velocity-radius ratios derived from the extreme entities. This ω is then subtracted from observed velocities to produce adjusted Keplerian velocities. The method assumes a deterministic relationship between radial distance and velocity, with no probabilistic modeling or parameter estimation. It operates on a dataset of radial positions and observed velocities, using only the first and last entries to compute ω. The adjusted velocities are compared to theoretical expectations using metrics like RMSE and R-squared. No iterative optimization or statistical inference is performed; the correction factor is derived directly from the dataset's extremal values. The model does not require tuning parameters beyond ω, which is computed per galaxy. The approach is applied to a sequence of radial observations, with each entity's adjusted velocity calculated using the same formula. The method's success is evaluated by comparing its fit to alternative models using empirical metrics on the same dataset.  
DOMAIN: astrophysics - galaxy dynamics  
STRUCTURE: other: empirical formula  
DATA_OBJECT: sequence or time-series  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: estimation  
DISTRIBUTION: continuous; continuous  
COMPLEXITY: not stated  
DATA_AVAILABILITY: dataset-with-DOI-or-handle  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
