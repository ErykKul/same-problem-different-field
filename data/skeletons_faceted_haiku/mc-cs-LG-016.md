MECHANISM: A latent-constrained conditional variational autoencoder (LC-CVAE) generates new realizations from limited observations by learning a shared latent embedding across multiple realizations at sparse anchor points, then completing the dense latent field using multi-output Gaussian process regression from neighborhood features, and finally decoding to produce time-series fields. Training jointly on multiple independent realizations with cross-realization alignment constraints promotes a homogeneous latent structure that generalizes to unseen realizations.
DOMAIN: generative modeling, climate simulation
STRUCTURE: other: deep generative architecture with sparse Gaussian process completion
DATA_OBJECT: sequence or time-series
INFERENCE: Bayesian posterior
PROBLEM_FORM: simulation or generation
DISTRIBUTION: continuous, normal
COMPLEXITY: convergence rate
