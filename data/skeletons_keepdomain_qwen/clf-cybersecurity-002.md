MECHANISM: The paper implements and evaluates three Bayesian classifier variants—Multinomial, Bernoulli, and Gaussian—for detecting network intrusions. Each variant assumes different feature distributions: Bernoulli treats features as binary, Multinomial as discrete counts, and Gaussian as continuous. The method trains each classifier on a network intrusion dataset, where features include packet attributes and protocol types, and labels indicate normal or attack traffic. During training, the classifiers compute posterior probabilities using Bayes' theorem, with likelihoods derived from the assumed feature distributions. Testing involves evaluating accuracy on held-out data, comparing how well each variant's assumptions align with the actual feature properties. Results show that Bernoulli achieves higher accuracy (69.9% test) than Multinomial (31.2% test) and Gaussian, suggesting that the assumption mismatch between feature properties and model assumptions significantly impacts performance. The study concludes that the choice of Bayesian variant directly correlates with accuracy, independent of feature preprocessing. No novel algorithm is proposed; the focus is on empirical comparison of existing methods.  
DOMAIN: network intrusion detection  
STRUCTURE: graphical models  
DATA_OBJECT: set or table  
INFERENCE: Bayesian posterior  
PROBLEM_FORM: classification  
DISTRIBUTION: binary; Bernoulli, Gaussian  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-private-data
