MECHANISM: The paper computes a hierarchical Bayesian extension of the Bradley-Terry model for paired comparison data. It defines a likelihood function over binary outcomes (win/loss) between pairs of teams, parameterized by team-specific ability parameters. A hierarchical prior is placed on these parameters to share information across teams, with hyperparameters governing the distribution of abilities. Posterior inference is performed via Markov chain Monte Carlo (MCMC) to estimate team abilities and hyperparameters. The model is applied to Major League Baseball data, where each pair of teams has a record of head-to-head matchups. Predictive performance is evaluated by comparing posterior predictive distributions to maximum likelihood estimates. The method accounts for uncertainty in team abilities through full Bayesian inference, avoiding point estimates. The computational steps include: (1) specifying the Bernoulli likelihood for each match outcome, (2) defining hierarchical normal priors on team abilities and hyperparameters, (3) deriving the posterior distribution, and (4) sampling from it using MCMC. The model's structure explicitly encodes dependencies between teams and matches, with hyperparameters enabling regularization across the league. The paper demonstrates that the Bayesian approach outperforms MLE in predictive accuracy while maintaining interpretability through posterior distributions.
DOMAIN: sports analytics and statistical modeling
STRUCTURE: graphical models
DATA_OBJECT: set or table
INFERENCE: bayesian posterior
PROBLEM_FORM: ranking or retrieval
DISTRIBUTION: binary; bernoulli
COMPLEXITY: not stated
DATA_AVAILABILITY: none
CODE_AVAILABILITY: none
PREREGISTRATION: none
EVIDENCE_BASIS: empirical-with-private-data
