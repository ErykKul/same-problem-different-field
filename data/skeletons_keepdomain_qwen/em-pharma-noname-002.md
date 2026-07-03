MECHANISM: The paper introduces two non-parametric methods for population pharmacokinetic modeling. The first method, non-parametric adaptive grid, partitions the parameter space into a grid and iteratively refines it based on the likelihood of observed drug concentration data. It uses kernel density estimation to approximate the posterior distribution of parameters without assuming a parametric form. The second method, non-parametric Bayesian, employs a Bayesian framework with a prior distribution over the parameter space and updates it using Markov Chain Monte Carlo (MCMC) sampling to approximate the posterior. Both methods avoid parametric assumptions about the distribution of pharmacokinetic parameters. The adaptive grid method dynamically adjusts grid resolution to focus on regions of high posterior density, while the Bayesian method integrates over parameter space to quantify uncertainty. The methods are applied to model drug concentration-time profiles in populations, accounting for inter-individual variability. The computational steps involve likelihood computation, grid refinement, kernel density estimation, and MCMC sampling. The paper emphasizes flexibility in modeling without restrictive parametric assumptions.  
DOMAIN: pharmacokinetics and statistics  
STRUCTURE: other: non-parametric methods  
DATA_OBJECT: continuous function or field  
INFERENCE: Bayesian posterior  
PROBLEM_FORM: estimation  
DISTRIBUTION: continuous; continuous  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: mathematical-proof
