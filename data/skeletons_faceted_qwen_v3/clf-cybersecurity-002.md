MECHANISM: The paper computes a probabilistic classification model based on Bayesian assumptions, where each variant (Multinomial, Bernoulli, Gaussian) makes distinct assumptions about the distribution of input features. The method begins by preprocessing a dataset, handling missing values, and selecting relevant features using a chi-square test. For each variant, the algorithm estimates prior probabilities of classes and likelihoods of features given classes. In the Gaussian variant, feature likelihoods are modeled as normal distributions, with parameters (mean, variance) estimated from training data. In the Multinomial variant, feature likelihoods are modeled as multinomial distributions, with probabilities derived from term frequencies. In the Bernoulli variant, feature likelihoods are modeled as binary presence/absence, with probabilities estimated from binary occurrences. The classifier computes posterior probabilities for each class using Bayes' theorem, combining prior and likelihood terms. The class with the highest posterior probability is selected as the prediction. The method evaluates performance using accuracy metrics on test and training data, comparing results across variants. The paper emphasizes that the choice of variant significantly affects accuracy due to differing assumptions about feature distributions, with Gaussian performing best when features are continuous and Multinomial performing poorly when features are not discrete. The implementation involves no novel algorithmic steps beyond standard Bayesian classification techniques.  
DOMAIN: network intrusion detection  
STRUCTURE: graphical models  
DATA_OBJECT: set or table  
INFERENCE: Bayesian posterior  
PROBLEM_FORM: classification  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: dataset-with-DOI-or-handle  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
