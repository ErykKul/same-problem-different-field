MECHANISM: The paper computes Bayesian parameter estimation for astrophysical galaxy models using a Markov Chain Monte Carlo (MCMC) approach. It modifies the CIGALE code to replace its grid-based parameter sampling with MCMC, which iteratively explores the parameter space by generating samples from a posterior distribution. The method constructs theoretical Spectral Energy Distribution (SED) models based on a grid of parameters, including stellar population properties, dust content, and star formation histories. For each sample, the algorithm calculates the likelihood of the SED matching observed photometric fluxes from UV to IR. The posterior distribution is updated using Metropolis-Hastings steps, which accept or reject new parameter samples based on their likelihood and prior probabilities. The process continues until the posterior converges, providing estimates of parameter means, medians, and credible intervals. The method is tested on simulated data to validate parameter recovery and applied to real data from the SINGS sample. The advantages include reduced computational time compared to grid-based methods and less sensitivity to parameter sampling density. The output is a set of posterior distributions for each parameter, enabling statistical constraints on galaxy formation and evolution properties.  
DOMAIN: astrophysical galaxy parameter estimation  
STRUCTURE: other: Markov Chain Monte Carlo  
DATA_OBJECT: continuous function or field  
INFERENCE: Bayesian posterior  
PROBLEM_FORM: estimation  
DISTRIBUTION: continuous; continuous  
COMPLEXITY: polynomial iterative  
DATA_AVAILABILITY: public-benchmark-used  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
