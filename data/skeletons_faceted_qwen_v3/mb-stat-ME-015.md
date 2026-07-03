MECHANISM: The paper computes Bayes factors to quantify evidence for or against a null hypothesis by comparing marginal likelihoods under different hypotheses. It derives prior-predictive densities for binary outcomes under both the null and alternative hypotheses, using conjugate Beta priors for the success probabilities in each group. The method involves numerical integration to compute the Bayes factor as a function of observed data, solving equations to find critical values where the Bayes factor crosses a specified threshold, and calculating probabilities of the Bayes factor falling below this threshold under the null and alternative hypotheses. These probabilities are interpreted as Bayesian analogues of type-I-error rates and power. The approach avoids Monte Carlo simulations by relying on analytical expressions for the prior-predictive densities and numerical root-finding to determine critical values. The method also computes the probability of achieving compelling evidence under the null hypothesis, ensuring robustness under prior uncertainty. The process is repeated for different hypothesis formulations, including two-sided and one-sided tests, and involves selecting the smallest sample size that satisfies specified power and error rate criteria. The computational steps include parameter estimation, integration over prior distributions, and optimization to meet statistical requirements.  
DOMAIN: Bayesian statistics, clinical trial design  
STRUCTURE: other: numerical integration and equation solving  
DATA_OBJECT: continuous function or field  
INFERENCE: Bayesian posterior  
PROBLEM_FORM: optimization  
DISTRIBUTION: binary; continuous  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: public-repository  
PREREGISTRATION: none  
EVIDENCE_BASIS: simulation-study
