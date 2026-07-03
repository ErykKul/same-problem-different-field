MECHANISM: The paper computes a variational Bayesian posterior over nonlinear dynamical systems using sparse Gaussian processes. The algorithm begins by defining a probabilistic state-space model with Gaussian process priors over transition functions and parametric likelihoods. Inducing variables are introduced to approximate the latent function values, reducing computational complexity. The evidence lower bound (ELBO) is derived by factorizing the variational distribution into components for inducing variables, latent states, and function values. Optimization proceeds by alternating between sampling from the smoothing distribution using sequential Monte Carlo and updating variational parameters to maximize the ELBO. The posterior over latent states is approximated as a Gaussian distribution conditioned on inducing variables, enabling efficient prediction of future trajectories. The method balances model capacity and computational cost by adjusting the number of inducing variables, avoiding overfitting through variational regularization. Predictive distributions are computed by integrating over the variational posterior of inducing variables, leveraging sparse approximations to achieve linear complexity in time series length. Stochastic variational inference and online learning variants are also described to handle long sequences and streaming data.  
DOMAIN: Gaussian process state-space models  
STRUCTURE: other: variational inference with sparse Gaussian processes  
DATA_OBJECT: latent state trajectory and inducing variables  
INFERENCE: variational and sampling  
PROBLEM_FORM: Bayesian learning  
DISTRIBUTION: none  
COMPLEXITY: polynomial iterative  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: mathematical-proof
