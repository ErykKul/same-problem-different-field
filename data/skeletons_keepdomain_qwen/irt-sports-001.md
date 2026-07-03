MECHANISM: The paper computes a Bayesian posterior probability distribution for log-strength parameters in a Bradley-Terry-Zermelo model applied to NCAA Division I Men’s Ice Hockey. Given game results and a prior distribution, it calculates the maximum a posteriori (MAP) estimate and the Hessian matrix to construct a Gaussian approximation of the posterior. Posterior predictive probabilities are estimated using three methods: 1) setting log-strengths to their MAP values, 2) using the Gaussian approximation for analytical or Monte Carlo integration, or 3) applying importance sampling to re-weight Monte Carlo simulations. The paper defines a method to evaluate models using the Bayes factor, comparing predicted probabilities against actual NCAA tournament outcomes. It describes an online tool that currently uses MAP evaluation but can be refined with Gaussian approximation or importance sampling. The model assumes a logistic relationship between team strengths and game outcomes, with parameters inferred via Bayesian optimization and uncertainty quantified through posterior sampling. The Gaussian approximation is derived from the Hessian at the MAP point, enabling efficient uncertainty propagation. Importance sampling is used to adjust Monte Carlo simulations for more accurate predictive probabilities. The Bayes factor evaluation involves integrating over the posterior predictive distribution to compare model fit against observed tournament results. The online tool implements these methods for real-time probability estimation of future game outcomes.
DOMAIN: sports analytics and Bayesian statistics
STRUCTURE: Bayesian inference
DATA_OBJECT: graph or network
INFERENCE: Bayesian posterior
PROBLEM_FORM: prediction or classification
DISTRIBUTION: binary; logistic
COMPLEXITY: not stated
DATA_AVAILABILITY: none
CODE_AVAILABILITY: none
PREREGISTRATION: none
EVIDENCE_BASIS: empirical-with-private-data
