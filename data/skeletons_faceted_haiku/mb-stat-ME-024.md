MECHANISM: Transform observed distributional observations into Euclidean space using tree-based logit decomposition: each distribution becomes a vector of logit-transformed conditional probabilities on internal nodes of a binary tree. Fit Bayesian latent factor model in the transformed space, expressing each distribution as a linear combination of latent factor distributions plus a mean. Use Polya-Gamma augmentation to obtain pseudo-linear Gaussian representation. Introduce spatial or other structural priors (e.g., simultaneous autoregressive) on factor loadings. Sample posterior via Gibbs algorithm.
DOMAIN: Bayesian factor models for categorical data
STRUCTURE: spectral or transform
DATA_OBJECT: tree or hierarchy
INFERENCE: Bayesian posterior
PROBLEM_FORM: estimation
DISTRIBUTION: none
COMPLEXITY: polynomial iterative
