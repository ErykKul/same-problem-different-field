MECHANISM: The paper introduces transformed Gaussian random fields (TGRF) and transformed Gaussian Markov random fields (TGMRF) by applying marginal transformations to standard GRF and GMRF models. These transformations map Gaussian margins to desired distributions (e.g., gamma or beta) to accommodate asymmetry and heavy tails in spatial data. The dependence structure is preserved via a Gaussian copula, which links the transformed margins to maintain spatial correlation. The method is implemented in a Bayesian framework, where posterior inference is performed using Markov chain Monte Carlo (MCMC) techniques. For spatial Poisson and Bernoulli regression, the transformed fields model Poisson intensity and Bernoulli rates, respectively, by linking the gamma or beta margins to the observed count or presence/absence data. The models are validated through simulation studies and applied to ecological datasets with spatial count and presence/absence data. The Bayesian approach allows for uncertainty quantification in parameter estimates and model selection. The Gaussian copula facilitates efficient computation of spatial dependencies, even after marginal transformations. The method generalizes traditional spatial models by relaxing the Gaussian assumption on margins while retaining the copula-based dependence structure. The paper demonstrates that the new models outperform traditional spatial models in ecological applications, as shown by improved fit and predictive accuracy. The computational steps include: (1) defining the transformed marginal distributions, (2) constructing the Gaussian copula for dependence, (3) specifying the likelihood under the transformed model, (4) performing Bayesian inference via MCMC, and (5) validating the model using simulations and real data.  
DOMAIN: spatial statistics and Bayesian inference  
STRUCTURE: graphical models  
DATA_OBJECT: grid or lattice  
INFERENCE: Bayesian posterior  
PROBLEM_FORM: estimation  
DISTRIBUTION: count; gamma; binary; beta  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: simulation-study
