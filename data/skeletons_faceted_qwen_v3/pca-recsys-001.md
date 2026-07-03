MECHANISM: The paper computes a probabilistic latent factor model for collaborative filtering using Bayesian inference. It models user-item interactions as inner products of latent factor vectors, introducing Gaussian priors on these factors to regularize the model. The likelihood function is defined over observed ratings, assuming Gaussian noise with mean determined by the inner product of latent factors and biases. Variational Inference (VI) is used to approximate the posterior distribution of latent factors and biases by minimizing the KL divergence between an approximate density and the exact posterior. The model extends to include user and item biases, which are also assigned Gaussian priors. The expected rating is predicted by integrating over the posterior distribution of parameters, using samples drawn from the approximate posterior. The optimization involves maximizing the evidence lower bound (ELBO), which balances the fit to the data and the complexity of the model. The process iteratively refines the approximate posterior until convergence, ensuring that the predicted ratings align with observed data while avoiding overfitting through Bayesian regularization. The method is applied to a matrix of user-item interactions, where each entry represents an observed rating, and the latent factors are inferred to capture underlying patterns in the data.  
DOMAIN: recommender systems  
STRUCTURE: graphical models  
DATA_OBJECT: dense matrix or tensor  
INFERENCE: variational  
PROBLEM_FORM: prediction or classification  
DISTRIBUTION: continuous; Gaussian  
COMPLEXITY: not stated  
DATA_AVAILABILITY: dataset-with-DOI-or-handle  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
