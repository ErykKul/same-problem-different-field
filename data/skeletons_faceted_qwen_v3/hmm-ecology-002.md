MECHANISM: The paper computes a Hidden Markov Model (HMM) to estimate latent behavioral states from a sequence of observed movement data. The model assumes a discrete-time Markov process governing behavioral states, with each state associated with a Gaussian distribution over movement increments (differences in location). The process equation defines each movement increment as a linear transformation of the previous increment, scaled by an autocorrelation parameter and rotated by a turning angle, plus Gaussian noise. The likelihood function is structured as a product of transition probabilities between states and emission probabilities of observations given states. Parameters include state transition probabilities, emission distribution parameters (autocorrelation, turning angle, noise covariance), and initial state probabilities. The model is fitted using maximum likelihood estimation via the TMB package, which compiles the likelihood function in C++ for computational efficiency. The Viterbi algorithm is applied to decode the most probable sequence of latent states from the observed data. The method does not account for measurement error in the observed locations, distinguishing it from Bayesian state-space models. The model is validated through simulation studies and applied to real-world animal tracking data to compare accuracy and computational speed against alternative approaches.  
DOMAIN: animal movement analysis  
STRUCTURE: graphical models  
DATA_OBJECT: sequence or time-series  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: estimation  
DISTRIBUTION: continuous; continuous  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: public-repository  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
