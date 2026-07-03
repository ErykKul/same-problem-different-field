MECHANISM: The paper computes a Bayesian hierarchical model that transforms categorical distributions into Euclidean space using a tree-based decomposition. Each distribution is represented as a set of conditional probabilities on internal nodes of a tree, which are then logit-transformed into real-valued parameters. These parameters are modeled as linear combinations of latent factor vectors, enabling low-dimensional representation of high-dimensional distributions. A simultaneous autoregressive (SAR) prior is introduced to capture spatial dependencies across locations. Posterior inference is performed via Markov chain Monte Carlo (MCMC) sampling, leveraging Pólya–Gamma augmentation to handle the logistic transformation. The model avoids parametric assumptions about the underlying distributional process and allows flexible estimation through the tree structure. Factor loadings are regularized using a combination of sparsity-inducing priors and spatial correlation structures. The effective number of factors is automatically calibrated through an infinite factor model framework. The method is evaluated through numerical experiments on real population data, demonstrating improved performance over standard Dirichlet mixture models.  
DOMAIN: Bayesian inference for categorical data  
STRUCTURE: graphical models  
DATA_OBJECT: graph or network  
INFERENCE: Bayesian posterior  
PROBLEM_FORM: estimation  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-private-data
