MECHANISM: A Bayesian mixture model partitions observations into two latent categories (dynamic and static) by computing the posterior probability of each observation belonging to each component. Observations in the dynamic component are modeled with a time-varying parameter drawn from a prior distribution at each time point; observations in the static component share a single parameter across all time points. Hyperpriors with empirical Bayes estimation allow borrowing strength across observations. Inference via Hamiltonian Monte Carlo samples from the posterior over all latent indicators and parameters. A second model uses penalized log-linear regression on counts in a contingency table with L1 regularization to induce sparsity and identify significant associations.
DOMAIN: Longitudinal immunology data, categorical data analysis
STRUCTURE: graphical models
DATA_OBJECT: sequence or time-series
INFERENCE: Bayesian posterior
PROBLEM_FORM: estimation
DISTRIBUTION: count
COMPLEXITY: not stated
