MECHANISM: The paper computes probabilistic models for sequence data using Bayesian inference and Gaussian processes. It replaces dot-product attention in Transformers with symmetric kernels derived from sparse Gaussian processes (SGP), enabling uncertainty quantification. A sparse variational Gaussian process (SVGP) is adapted for online learning, leveraging HiPPO's polynomial projections to maintain long-term memory through recurrence. The model uses variational inference to approximate posterior distributions over parameters, combining data from multiple time steps. For generative models, pseudo videos are constructed via data augmentation, introducing self-supervised signals to improve latent state modeling. The algorithm iteratively updates memory states using linear ordinary differential equations (ODEs) discretized into recurrence relations. Variational objectives are optimized to minimize divergence between approximate and true posteriors, with Monte Carlo sampling used for predictive uncertainty estimation. The method scales to high-dimensional inputs by decomposing computations across attention heads and inducing variables. It handles sequential data through time-varying orthogonal projections and adaptive basis functions, ensuring computational efficiency while preserving long-range dependencies. The framework integrates probabilistic uncertainty into deep learning architectures, enabling both prediction and generation tasks with calibrated uncertainty estimates.
DOMAIN: deep sequence models
STRUCTURE: spectral or transform
DATA_OBJECT: sequence or time-series; graph or network
INFERENCE: Bayesian posterior; variational
PROBLEM_FORM: estimation; simulation or generation
DISTRIBUTION: continuous; Gaussian
COMPLEXITY: not stated
DATA_AVAILABILITY: public-benchmark-used
CODE_AVAILABILITY: public-repository
PREREGISTRATION: none
EVIDENCE_BASIS: empirical-with-released-data
