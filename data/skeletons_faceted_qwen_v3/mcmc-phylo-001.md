MECHANISM: The paper computes measures of effective sample size (ESS) for phylogenetic trees to quantify Monte Carlo error in Bayesian MCMC inference. It extends classical ESS definitions, which rely on variance of the sample mean, to high-dimensional tree structures by considering summaries such as split probabilities, tree topology probabilities, and summary trees. The method involves estimating the limiting variance of posterior summaries using autocovariances from MCMC samples, then deriving ESS as the hypothetical number of independent samples that would yield the same variance. For tree-specific summaries, the paper evaluates three categories of ESS measures: generalizations of continuous-variable ESS, reduced-dimensional representations of trees, and ad-hoc approaches. It validates these measures through simulations by comparing brute-force estimates of sampling variability with ESS-based estimates. The approach includes running multiple MCMC chains, computing split probabilities and tree summaries, and drawing independent samples from the posterior to assess Monte Carlo error. The paper also introduces visualization tools to compare chains by accounting for Monte Carlo error in split probabilities and tree summaries. It demonstrates that existing ESS measures for continuous parameters are insufficient for tree structures due to dependencies and high dimensionality, and highlights the need for within-chain and between-chain diagnostics to assess convergence. The study concludes that tree-specific ESS measures are critical for reliable Bayesian phylogenetic inference, as they reveal discrepancies in sampling variability that standard post-MCMC workflows overlook.  
DOMAIN: phylogenetics  
STRUCTURE: other: Monte Carlo simulation  
DATA_OBJECT: graph or network  
INFERENCE: Bayesian posterior  
PROBLEM_FORM: estimation  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: public-benchmark-used  
CODE_AVAILABILITY: public-repository  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
