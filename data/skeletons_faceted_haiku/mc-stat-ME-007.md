MECHANISM: Monitor multiple basket cohorts during a clinical trial with continuous interim analysis to detect futility early. For each basket, maintain posterior distributions of binary response rates from conjugate Beta priors updated with observed data. Compute similarity weights across baskets using Jensen-Shannon Divergence and pool information through weighted mixture of posterior distributions. Handle incomplete outcome data through Bayesian multiple imputation using a Weibull survival model. At each interim analysis, test whether the posterior probability of futility exceeds a threshold and drop non-promising baskets.
DOMAIN: Clinical trial design for basket trials
STRUCTURE: graphical models
DATA_OBJECT: set or table
INFERENCE: Bayesian posterior
PROBLEM_FORM: decision or test
DISTRIBUTION: binary; binary
COMPLEXITY: not stated
