MECHANISM: The paper computes a classification model that maps input documents to sentiment labels (positive/negative) using probabilistic and optimization-based methods. The process begins by representing each document as a vector of feature counts, where features are derived from unigrams, bigrams, or parts-of-speech tags. For Naive Bayes, the model estimates the probability of each class given the document by assuming conditional independence of features, using maximum likelihood with smoothing. For Maximum Entropy, the model maximizes the entropy of a probability distribution over classes, subject to constraints derived from feature expectations in the training data, using iterative scaling to optimize parameters. For Support Vector Machines, the model finds a hyperplane in feature space that maximally separates classes by solving a constrained optimization problem with a margin maximization objective. The classification decision for a new document is determined by the model's learned parameters, with Naive Bayes and MaxEnt producing probabilistic outputs and SVMs using a sign-based decision rule. The paper evaluates performance using cross-validation and compares baselines derived from human-selected features. It also investigates the impact of feature selection (e.g., unigrams vs. bigrams), frequency vs. presence, and contextual markers (e.g., negation tags) on accuracy.  
DOMAIN: text sentiment analysis  
STRUCTURE: sparse linear algebra  
DATA_OBJECT: sparse matrix  
INFERENCE: frequentist point estimate  
PROBLEM_FORM: classification  
DISTRIBUTION: binary; multinomial  
COMPLEXITY: not stated  
DATA_AVAILABILITY: dataset-in-repository  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
