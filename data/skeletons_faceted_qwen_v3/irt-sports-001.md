MECHANISM: The paper computes a Bayesian posterior distribution over log-strength parameters for entities based on pairwise comparison outcomes. It defines a probability model where the likelihood of an outcome depends on the difference between log-strength parameters of two entities, using a logistic function. A prior distribution is combined with the likelihood to form the posterior, which is maximized to find the maximum a posteriori (MAP) estimates. The MAP estimates are computed iteratively using an equation derived from the posterior's gradient. A Gaussian approximation to the posterior is constructed by computing the Hessian matrix of the log-posterior at the MAP point, which involves second derivatives of the likelihood and prior terms. Posterior predictive probabilities for future outcomes are estimated by integrating the outcome probability over the posterior distribution, approximated either via Monte Carlo sampling from the Gaussian approximation or through importance sampling weighted by the ratio of the true posterior to the Gaussian approximation. The method evaluates models using Bayes factors comparing predicted probabilities against actual outcomes. An online tool is described that uses MAP estimates or Gaussian approximations to compute real-time predictive probabilities for future events.  
DOMAIN: sports analytics  
STRUCTURE: optimization only  
DATA_OBJECT: set or table  
INFERENCE: Bayesian posterior  
PROBLEM_FORM: prediction or classification  
DISTRIBUTION: binary; logistic  
COMPLEXITY: polynomial iterative  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-private-data
