MECHANISM: The paper computes Bayesian posterior distributions over phylogenetic trees using Markov chain Monte Carlo (MCMC) sampling. It quantifies Monte Carlo error in three summary measures: edge/branch (split) probabilities, tree probabilities, and estimated summary trees. The method calculates effective sample size (ESS) metrics by estimating variance from MCMC samples, which reflects the precision of posterior approximations. Three ESS measures are identified as practical for assessing Monte Carlo error in phylogenetic contexts. The computation involves generating posterior samples via MCMC, calculating variance estimates for each summary statistic, and deriving ESS values based on these variances. Visualization tools are introduced to compare multiple MCMC runs by incorporating Monte Carlo error metrics. The approach emphasizes evaluating within-chain mixing and between-chain convergence to ensure reliable posterior inference. The paper does not propose new MCMC algorithms but focuses on analyzing existing samples to assess their adequacy for phylogenetic inference. The ESS measures are derived from the relationship between sample variance and the theoretical variance of the posterior distribution. The method relies on standard Bayesian inference techniques applied to tree structures, with no novel mathematical formulation beyond variance estimation and ESS calculation.  
DOMAIN: Bayesian phylogenetics  
STRUCTURE: other: Monte Carlo  
DATA_OBJECT: tree or hierarchy  
INFERENCE: Bayesian posterior  
PROBLEM_FORM: estimation  
DISTRIBUTION: continuous and Bayesian posterior  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: simulation-study
