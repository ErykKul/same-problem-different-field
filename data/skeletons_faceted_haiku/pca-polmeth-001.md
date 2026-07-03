MECHANISM: A Latent Space Item Response Model (LSIRM) embeds legislators and bills jointly in a shared Euclidean metric space of low dimension. Each legislator i and bill j receives a latent position (vector in R^K). The probability of a "Yea" vote is modeled using a logit link that depends on: the legislator's baseline propensity (theta_i), the bill's baseline popularity (beta_j), and the Euclidean distance between the legislator's and bill's positions (scaled by a proximity parameter gamma). Estimation is performed via Markov chain Monte Carlo (Gibbs sampling with Metropolis-Hastings steps) over the full joint posterior. The key distinction from prior methods is use of Euclidean distance (satisfying triangle inequality) rather than quadratic/Gaussian utilities.
DOMAIN: Political methodology and legislative voting analysis
STRUCTURE: sparse linear algebra
DATA_OBJECT: sparse matrix
INFERENCE: Bayesian posterior
PROBLEM_FORM: estimation
DISTRIBUTION: binary; binomial
COMPLEXITY: not stated
