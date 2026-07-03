MECHANISM: The paper computes a Bayesian posterior distribution over a hybrid discrete-continuous state space representing an unknown, time-varying number of entities. The state includes binary flags indicating entity activity and continuous parameters describing their dynamics. A birth/death process models entity appearance/disappearance, while a transition distribution governs continuous state evolution. The method alternates between prediction (using a Chapman-Kolmogorov equation) and update steps (via Bayes theorem) to recursively refine the posterior. A particle filter approximates the posterior with a set of weighted samples, where each sample represents a possible state configuration. Auxiliary sampling is used to improve particle diversity by incorporating current observations during proposal generation. The observation model sums nonlinear contributions from active entities, with noise modeled as a general distribution (not restricted to Gaussian). The algorithm handles non-Gaussian process and observation noise without requiring preprocessing. Point estimates are derived via minimum mean square error (MMSE) computation from the particle weights and states. The method operates directly on raw sensor signals, avoiding thresholding or detection steps.  
DOMAIN: multi-target tracking in signal processing  
STRUCTURE: other: particle filter  
DATA_OBJECT: set or table  
INFERENCE: Bayesian posterior  
PROBLEM_FORM: estimation  
DISTRIBUTION: continuous; possibly non-Gaussian  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: simulation-study
