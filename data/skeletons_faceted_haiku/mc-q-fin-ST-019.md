MECHANISM: Trains a generative adversarial network (generator and discriminator) using Wasserstein loss with gradient penalty; augments adversarial objective with four differentiable structural constraints: generalized Pareto distribution tail index matching, autocorrelation function alignment on squared returns, leverage effect (correlation between past returns and future volatility) matching, and cross-scale volatility correlation alignment via Frobenius norm; jointly optimizes all constraints via weighted sum; generates synthetic time series by sampling from latent Gaussian and passing through generator.
DOMAIN: Synthetic financial time series generation with distribution alignment
STRUCTURE: other: generative adversarial network
DATA_OBJECT: sequence or time-series
INFERENCE: sampling or Monte-Carlo
PROBLEM_FORM: simulation or generation
DISTRIBUTION: continuous; continuous
COMPLEXITY: polynomial iterative
