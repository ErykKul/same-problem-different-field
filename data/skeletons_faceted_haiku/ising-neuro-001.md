MECHANISM: Infer the parameters of a pairwise maximum-entropy graphical model over many binary variables from observed joint activity patterns. Learn single-variable field parameters (marginal activation levels) and pairwise coupling parameters (interactions) so that the model reproduces the observed first-order means and second-order correlations. Estimation maximizes the likelihood, equivalently matching model moments to empirical moments, a convex inverse problem in the parameter space. The fitted model assigns a probability to every joint binary pattern and can be conditioned on an external covariate so that the field parameters depend on it. Couplings quantify direct dependence between variable pairs beyond what shared external drive explains.
DOMAIN: neuroscience
STRUCTURE: graphical models
DATA_OBJECT: graph or network
INFERENCE: frequentist point estimate
PROBLEM_FORM: estimation
DISTRIBUTION: binary; pairwise maximum-entropy
COMPLEXITY: polynomial iterative
DATA_AVAILABILITY: data-on-request
CODE_AVAILABILITY: none
PREREGISTRATION: none
EVIDENCE_BASIS: empirical-with-private-data
