MECHANISM: The paper computes a Bayesian hierarchical model that separates structural zeros from positive counts using a hurdle mechanism. The model employs a beta-binomial distribution to handle bounded counts with overdispersion, incorporating hierarchical priors for state-level coefficients. A cross-margin covariance component is introduced to capture dependencies between participation and intensity parameters, identified through the hierarchical layer rather than the conditional likelihood. The model includes a Cholesky-based sandwich variance correction for pseudo-posterior inference under survey weights, guided by a parameter-specific design effect ratio diagnostic. A log-scale marginal effect decomposition translates regression coefficients into policy-relevant quantities. The algorithm iteratively estimates parameters using Markov Chain Monte Carlo (MCMC) methods, with hierarchical priors regularizing high-dimensional covariance structures. The beta-binomial kernel accommodates bounded support and overdispersion, while the hurdle component distinguishes participation from intensity. The model is applied to a dataset of childcare providers, estimating the effect of poverty on enrollment participation and intensity. The hierarchical structure allows state-varying coefficients and cross-margin covariance, with the LKJ prior providing finite-sample regularization. The pseudo-posterior framework adjusts for survey weights, and the sandwich correction improves credible interval coverage. The decomposition separates the poverty reversal into extensive-margin (access) and intensive-margin (intensity) components, quantifying their relative contributions.  
DOMAIN: Bayesian hierarchical modeling for bounded counts  
STRUCTURE: graphical models  
DATA_OBJECT: set or table  
INFERENCE: Bayesian posterior  
PROBLEM_FORM: estimation  
DISTRIBUTION: bounded; beta-binomial  
COMPLEXITY: not stated  
DATA_AVAILABILITY: dataset-with-DOI-or-handle  
CODE_AVAILABILITY: public-repository  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
