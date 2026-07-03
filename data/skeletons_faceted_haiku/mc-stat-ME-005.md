MECHANISM: Given observed outcomes and treatment assignments with unobserved multiple versions within each treatment, model the outcome conditional on treatment as a mixture-of-experts framework where each mixture component corresponds to a latent version. Use the EM algorithm to iteratively compute posterior responsibilities (expectations of latent version indicators) and maximize the expected complete-data log-likelihood. For each treatment, estimate a multinomial logistic gating function for version probabilities and a normal density expert function for outcomes. Recover version-specific causal effects and their estimates through maximum likelihood estimation.
DOMAIN: Causal inference with latent treatment versions
STRUCTURE: other: mixture model with EM estimation
DATA_OBJECT: set or table
INFERENCE: Bayesian posterior
PROBLEM_FORM: estimation
DISTRIBUTION: continuous; continuous
COMPLEXITY: convergence rate
