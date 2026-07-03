MECHANISM: The paper computes a Bayesian posterior distribution over a multidimensional parameter space using a Markov Chain Monte Carlo (MCMC) algorithm. The process begins by defining a prior probability distribution over parameters, which are then updated iteratively based on observed data through a likelihood function. At each step, a proposal distribution generates candidate parameter values, and these are accepted or rejected based on a transition probability derived from the ratio of posterior probabilities between the candidate and current states. The algorithm ensures detailed balance and asymptotic convergence to the target posterior distribution. The likelihood function is computed as a weighted sum of squared differences between theoretical model outputs and observed data, normalized by measurement uncertainties. The method explicitly handles parameter degeneracies by sampling regions of high posterior density without requiring uniform grid sampling. It calculates marginalized distributions by binning samples and counting frequencies, and uses convergence diagnostics to assess chain stability. The computational workflow includes burn-in phase discarding, thinning of chains, and covariance matrix estimation for improved sampling efficiency. The algorithm scales linearly with the number of parameters and avoids exponential growth in computation time compared to grid-based methods.  
DOMAIN: astrophysical parameter estimation  
STRUCTURE: other: markov-chain-monte-carlo  
DATA_OBJECT: parameter space  
INFERENCE: bayesian posterior  
PROBLEM_FORM: estimation  
DISTRIBUTION: continuous; continuous  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: public-repository  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-simulated-data
