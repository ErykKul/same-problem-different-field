MECHANISM: The Bradley-Terry model assigns latent strength parameters to each team. The probability that one entity defeats another is a logistic function of the difference in log-strengths. A hierarchical Bayesian framework is constructed: log-strengths are drawn from a Gaussian prior parameterized by a hyperparameter sigma, which itself has a Gamma hyperprior. Estimation proceeds via Hamiltonian Monte Carlo (MCMC) sampling from the posterior distribution. Ranking and prediction are obtained from posterior expectations and posterior predictive distributions, respectively.
DOMAIN: sports analytics; ranking and prediction
STRUCTURE: graphical models
DATA_OBJECT: set or table
INFERENCE: Bayesian posterior via MCMC; hierarchical priors
PROBLEM_FORM: ranking or retrieval; prediction
DISTRIBUTION: measured as binary outcomes (win/loss) in head-to-head paired comparisons; estimator assumes logistic (sigmoid) model for win probability given strength difference
COMPLEXITY: polynomial iterative
