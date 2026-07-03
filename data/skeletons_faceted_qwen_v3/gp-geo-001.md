MECHANISM: The paper introduces a method to transform Gaussian random fields (GRF) and Gaussian Markov random fields (GMRF) by applying probability integral transformations to their marginal distributions, enabling the modeling of asymmetry and heavy tails. The transformation preserves the Gaussian copula dependence structure while allowing arbitrary marginal distributions. The process involves defining a random vector through inverse cumulative distribution functions applied to standard normal variables, ensuring the joint density incorporates both the transformed margins and the Gaussian copula. The resulting transformed fields (TGRF and TGMRF) maintain the Markov property, with conditional independence determined by the precision matrix. The method is implemented within a Bayesian framework, using Markov chain Monte Carlo (MCMC) for posterior inference. Model selection is evaluated via criteria like the conditional predictive ordinate (CPO) and deviance information criterion (DIC). The approach is applied to spatial count and binary data, with marginal distributions specified as gamma or beta to model Poisson intensity or Bernoulli rates. The computational steps include defining the transformed fields, specifying the copula structure, and performing Bayesian inference with MCMC sampling. The method generalizes traditional GMRF models by allowing flexible marginal distributions while retaining the Gaussian copula for dependence.  
DOMAIN: spatial statistics and Bayesian modeling  
STRUCTURE: graphical models  
DATA_OBJECT: graph or network  
INFERENCE: Bayesian posterior  
PROBLEM_FORM: estimation  
DISTRIBUTION: count; continuous; binary; continuous  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
