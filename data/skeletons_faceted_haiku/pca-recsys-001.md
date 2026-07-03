MECHANISM: Latent Factor Model (LFM) decomposes a sparse user-item rating matrix into a product of two low-rank factor matrices: predicted rating r_ui ≈ p_u^T q_i, where p_u is a user factor vector and q_i is an item factor vector. The Bayesian variant (BLFM) places Gaussian priors over all latent factors and uses Variational Inference to approximate the intractable posterior distribution. The algorithm maximizes the Evidence Lower Bound (ELBO) via KL divergence minimization between a tractable approximate posterior and the true posterior. An extension (BLFMBias) adds user-dependent and item-dependent bias terms b_u and b_i to model systematic deviations. Predictions are obtained by integrating over the posterior samples of latent factors and biases.
DOMAIN: Recommender systems and collaborative filtering
STRUCTURE: sparse linear algebra
DATA_OBJECT: sparse matrix
INFERENCE: Bayesian posterior
PROBLEM_FORM: prediction
DISTRIBUTION: continuous; binomial assumed for likelihood
COMPLEXITY: not stated
