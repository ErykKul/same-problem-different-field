MECHANISM: Estimate time-varying states of multiple targets from raw superpositional sensor signals (sums of target contributions). Maintain a hybrid state combining continuous kinematic variables and discrete birth/death indicators for each target slot. Model transitions via factorized densities for target activity (Markov chain with birth/death probabilities) and dynamics (nonlinear, non-Gaussian motion). Model observations as nonlinear functions of active target states summed together plus non-Gaussian noise. Apply particle filter (sequential Monte Carlo) using auxiliary resampling to recursively approximate the posterior distribution. Extract point estimates via MMSE averaging over particles weighted by likelihoods.
DOMAIN: Target tracking and radio-frequency tomography.
STRUCTURE: other: particle filtering with birth/death process
DATA_OBJECT: sequence or time-series
INFERENCE: sampling or Monte-Carlo
PROBLEM_FORM: estimation
DISTRIBUTION: continuous; continuous
COMPLEXITY: polynomial iterative
