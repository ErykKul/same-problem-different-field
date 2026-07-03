MECHANISM: The paper computes a posterior distribution over latent states and model parameters in a Bayesian hidden Markov model with missing observations. The algorithm integrates out both the missing data and their corresponding latent states through analytical marginalization, reducing the parameter space dimensionality. It employs a forward-backward recursion to compute probabilities for observed data, where forward probabilities are recursively calculated by summing over previous states weighted by transition and emission probabilities. Backward probabilities are similarly computed in reverse. The collapsed Gibbs sampler iteratively samples parameters and observed latent states from their conditional distributions, leveraging the reduced parameter space to achieve faster convergence. The method's efficiency arises from avoiding explicit sampling of missing data and latent states associated with missing observations, instead analytically integrating them out. The computational complexity per iteration is reduced as the missing rate increases, due to fewer states being processed. The algorithm's theoretical guarantees include improved convergence rates and lower time complexity compared to standard Gibbs samplers. The method is validated through numerical simulations and real data experiments measuring effective sample size and runtime.  
DOMAIN: Bayesian statistics  
STRUCTURE: graphical models  
DATA_OBJECT: sequence or time-series  
INFERENCE: Bayesian posterior  
PROBLEM_FORM: estimation  
DISTRIBUTION: none  
COMPLEXITY: polynomial iterative  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-private-data
