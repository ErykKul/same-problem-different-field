MECHANISM: The paper computes a probabilistic model where a latent state variable evolves according to a Markov process with transition probabilities defined by a matrix. Observations are linked to the state via a measurement equation, which can be any distributional form. The algorithm iteratively computes the posterior distribution of the state sequence using filtering (forward recursion) and smoothing (backward recursion) steps. Filtering calculates the probability of the current state given past observations, while smoothing refines this using future data. Parameter estimation is performed via maximum likelihood using an expectation-maximization (EM) algorithm, which alternates between filtering/smoothing to estimate the state sequence and maximizing the likelihood to update model parameters. Bayesian inference employs Markov Chain Monte Carlo (MCMC) methods, including forward filtering and backward sampling to sample from the joint posterior distribution of states and parameters. The transition matrix is estimated by maximizing the likelihood or sampling from the posterior, with constraints on its structure depending on the model variant. The method handles uncertainty in both the state sequence and parameters, with Bayesian approaches explicitly modeling posterior distributions and frequentist approaches relying on point estimates. The paper discusses challenges such as label switching in Bayesian inference and non-identification issues in hypothesis testing for the number of states.  
DOMAIN: econometrics  
STRUCTURE: graphical models  
DATA_OBJECT: sequence or time-series  
INFERENCE: Bayesian posterior  
PROBLEM_FORM: estimation  
DISTRIBUTION: none  
COMPLEXITY: polynomial iterative  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: mathematical-proof
