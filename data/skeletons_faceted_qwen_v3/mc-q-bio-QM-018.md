MECHANISM: The paper computes a Bayesian longitudinal mixture model to classify TCR clonotypes into dynamic (expanding/contracting) or static categories. It uses Poisson-distributed counts of clonotype frequencies over time, with Gamma-distributed intensity parameters and hierarchical priors on hyperparameters. The model integrates out latent parameters to derive posterior predictive distributions for static and dynamic components, using Hamiltonian Monte Carlo for sampling. A separate penalized log-linear model with L1 regularization identifies associations between VJ gene family co-occurrences and patient characteristics, fitting a saturated contingency table with sparse parameter estimation. Both models handle missing data and incorporate hierarchical structures across patients. The Bayesian framework allows probabilistic classification of clonotypes and estimation of gene enrichment patterns through penalized maximum likelihood.  
DOMAIN: immunology  
STRUCTURE: graphical models  
DATA_OBJECT: sequence or time-series  
INFERENCE: Bayesian posterior  
PROBLEM_FORM: estimation  
DISTRIBUTION: count; Poisson  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-private-data
