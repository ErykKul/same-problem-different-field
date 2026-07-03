MECHANISM: The Bradley-Terry-Zermelo model estimates latent team strength parameters from game outcomes (paired comparisons). The probability that team i defeats team j is modeled as a logistic function of the difference in log-strengths. A Bayesian framework places priors over log-strengths (Haldane, generalized logistic, or Gaussian) and computes posterior distributions via the likelihood from game results. Posterior predictive probabilities for future games are obtained by marginalizing over posterior uncertainty in strengths via MAP evaluation, Gaussian approximation, or importance sampling.
DOMAIN: sports analytics; NCAA hockey ranking
STRUCTURE: graphical models
DATA_OBJECT: set or table
INFERENCE: Bayesian posterior via maximum a posteriori (MAP); Gaussian approximation; importance sampling
PROBLEM_FORM: ranking or retrieval; prediction
DISTRIBUTION: measured as binary game outcomes (win/loss); estimator assumes logistic (sigmoid) win probability
COMPLEXITY: polynomial iterative
