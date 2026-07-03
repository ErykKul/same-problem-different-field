MECHANISM: The paper computes a time-aware latent space optimization framework that integrates temporal dynamics into both the surrogate model and the generative representation. The method defines a continuous latent space for structured entities, where each latent code is a function of auxiliary covariates, including time. A Gaussian process (GP) prior is placed over latent functions, enabling the latent geometry to adapt to temporal drift. The surrogate model uses a spatio-temporal kernel that combines spatial (latent code) and temporal dimensions. Optimization proceeds by iteratively sampling latent points via an acquisition function that balances exploration and exploitation under the evolving GP posterior. The generative model maps latent codes to entities through a decoding function, and the latent space is updated using variational inference with alignment regularizers to maintain consistency with observed objectives. Time is explicitly modeled as a covariate, allowing the latent geometry to shift as objectives evolve. The algorithm alternates between updating the GP surrogate, refining the latent representation, and selecting new latent queries for evaluation. The method ensures robustness to varying drift speeds by jointly modeling temporal changes in both the surrogate and the latent embedding.  
DOMAIN: molecular design and Bayesian optimization  
STRUCTURE: graphical models  
DATA_OBJECT: continuous function  
INFERENCE: variational  
PROBLEM_FORM: optimization  
DISTRIBUTION: continuous; continuous  
COMPLEXITY: not stated  
DATA_AVAILABILITY: public-benchmark-used  
CODE_AVAILABILITY: public-repository  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
