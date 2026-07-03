MECHANISM: The paper computes two nonparametric methods for estimating the joint population distribution of model parameters from observed data. The first method, NPAG, uses a primal-dual interior-point optimization to maximize the likelihood over a discrete grid of support points, iteratively expanding and contracting the grid to refine estimates. It constructs a discrete distribution by assigning weights to support points, solving a convex optimization problem for weights while keeping support points fixed. The second method, NPB, employs a Bayesian approach with a Dirichlet process prior, using a stick-breaking process to generate weights and Gibbs sampling to estimate the posterior distribution of parameters. Both methods estimate the population distribution as a discrete mixture of Dirac delta functions, with NPAG relying on deterministic optimization and NPB incorporating stochastic sampling. The algorithms handle uncertainty by either maximizing likelihood deterministically or computing Bayesian posteriors with credibility intervals. The methods are applied to pharmacokinetic data but are described in generic mathematical terms without domain-specific entities or quantities.  
DOMAIN: pharmacokinetics and statistics  
STRUCTURE: other: nonparametric maximum likelihood and Bayesian inference  
DATA_OBJECT: discrete distribution  
INFERENCE: Bayesian posterior  
PROBLEM_FORM: estimation  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: public-repository  
CODE_AVAILABILITY: public-repository  
PREREGISTRATION: none  
EVIDENCE_BASIS: simulation-study
