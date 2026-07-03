MECHANISM: The paper computes a particle filter algorithm for multi-target tracking from superpositional sensor data, which is the sum of contributions from all targets. The method operates directly on raw sensor signals without preprocessing, unlike conventional track-before-detect methods that require thresholding. It uses a Bayesian framework with importance sampling and resampling steps to approximate the posterior distribution of target states. The algorithm incorporates a birth/death model to handle an unknown, time-varying number of targets without requiring initial state knowledge. Each particle represents a hypothesis about the number of targets and their states, with weights updated based on the likelihood of the superpositional data. The likelihood function is computed using the sum of contributions from all targets, without assuming Gaussian noise or specific functional forms for target contributions. The method generalizes Salmond et al.'s single-target track-before-detect particle filter by extending it to multiple targets. The algorithm's performance is evaluated using a simulation example in radio-frequency tomography, where it outperforms existing methods in terms of the optimal subpattern assignment (OSPA) metric. The key innovation lies in avoiding preprocessing and handling non-Gaussian noise through the particle filter's probabilistic structure. The method's steps include initializing particles, propagating them through time, updating weights based on sensor data, and resampling to focus on high-likelihood hypotheses.
DOMAIN: multi-target tracking, signal processing
STRUCTURE: other: particle filter
DATA_OBJECT: sequence or time-series
INFERENCE: Bayesian posterior
PROBLEM_FORM: estimation
DISTRIBUTION: continuous; non-Gaussian
COMPLEXITY: not stated
DATA_AVAILABILITY: none
CODE_AVAILABILITY: none
PREREGISTRATION: none
EVIDENCE_BASIS: simulation-study
