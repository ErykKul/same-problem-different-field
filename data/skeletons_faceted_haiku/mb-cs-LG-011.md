MECHANISM: Bayesian optimization is extended to time-varying objectives in the latent space of a generative model. A spatio-temporal Gaussian process surrogate models the objective as a function of both latent code and time. The generative model is a GP-prior variational autoencoder (DGBFGP) with basis-function approximation, where the latent code is an additive combination of covariate-dependent GP functions, including time as a covariate. This makes latent geometry explicitly time-dependent, adapting as objectives drift. The acquisition function balances exploitation and exploration using Thompson sampling. Structured latent representations are maintained through alignment regularizers and latent inversion to mitigate decoder-induced misalignment. Representations and surrogate are periodically updated as new observations arrive.

DOMAIN: black-box optimization, molecular design, Bayesian optimization

STRUCTURE: other: GP-prior VAE with spatio-temporal kernels

DATA_OBJECT: dense matrix or tensor

INFERENCE: Bayesian posterior

PROBLEM_FORM: optimization

DISTRIBUTION: continuous

COMPLEXITY: not stated
