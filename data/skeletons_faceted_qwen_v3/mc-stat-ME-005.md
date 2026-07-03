MECHANISM: The paper computes version-specific causal effects by modeling treatment versions as latent variables within a mixture-of-experts framework. It defines a conditional distribution of outcomes given treatment, decomposed into a weighted sum of version-specific outcome models, where weights are determined by a gating function. The gating function is parameterized via multinomial logistic regression, while each version-specific outcome model assumes normality with mean and variance parameters. The method estimates parameters by maximizing the likelihood of observed data through the expectation-maximization (EM) algorithm. In the E-step, posterior responsibilities for latent versions are computed using Bayes' theorem, combining version assignment probabilities and version-specific outcome densities. In the M-step, parameters are updated by maximizing the expected complete-data log-likelihood, which involves re-estimating gating function coefficients, outcome model means, and variances. The approach explicitly accounts for treatment-version heterogeneity and recovers unobserved version structures while maintaining identifiability under standard assumptions. The estimator is derived via inverse probability weighting and relies on overlap conditions to ensure positivity of treatment-version assignment probabilities. The method provides a principled way to estimate heterogeneous causal effects across latent versions of treatment without requiring explicit version observations.
DOMAIN: causal inference with multiple treatment versions
STRUCTURE: other: mixture-of-experts
DATA_OBJECT: mixture model with latent variables
INFERENCE: maximum-likelihood
PROBLEM_FORM: estimation
DISTRIBUTION: continuous; continuous
COMPLEXITY: polynomial iterative
DATA_AVAILABILITY: dataset-with-DOI-or-handle
CODE_AVAILABILITY: public-repository
PREREGISTRATION: none
EVIDENCE_BASIS: simulation-study
