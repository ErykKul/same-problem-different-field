MECHANISM: The paper computes transport scaling laws by analyzing mean square displacement (MSD) of trajectories, revealing sub-ballistic motion characterized by a Hurst exponent. It segments trajectories into phases (transition, search, climb) using a Hidden Markov Model (HMM) based on trajectory-derived features, linking phase-specific dynamics to global transport properties. Statistical comparisons across aircraft types and skill levels quantify how search phase efficiency and glide ratios influence transport scaling. The method involves estimating MSD as a function of time lag, fitting power-law relationships, and applying probabilistic segmentation to identify phase boundaries. It calculates glide ratios from horizontal and vertical velocity statistics, analyzes survival functions for phase durations, and compares distributions of thermaling radii and climb velocities. The analysis reveals that learning effects manifest primarily in the search phase through improved detection and exploitation of atmospheric lift, reflected in higher Hurst exponents for more experienced pilots. The method relies on transforming raw trajectory data into informative features for HMM calibration and uses empirical data to validate transport laws across diverse flight conditions.  
DOMAIN: movement ecology and transport physics  
STRUCTURE: graphical models  
DATA_OBJECT: sequence or time-series  
INFERENCE: frequentist point estimate  
PROBLEM_FORM: estimation  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: public-benchmark-used  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
