MECHANISM: The paper computes a document classification system using a multinomial naïve Bayes classifier trained on features extracted from clinical reports. The system processes text documents by extracting word-level n-grams and UMLS concept-level features, which are mapped to medical ontologies. These features are combined into a feature vector representing each document. The classifier estimates the probability that a document belongs to the "related" or "unrelated" category using Bayes' theorem under the assumption of feature independence. Training involves computing maximum likelihood estimates for the conditional probabilities of each feature given the class labels, using a manually annotated corpus of 90% training data. The system evaluates performance using ten-fold cross-validation on the remaining 10% test data, measuring accuracy, precision, recall, and F-score. The UMLS concepts are integrated by mapping text to standardized medical terminology, enhancing the classifier's ability to distinguish brain-tumor-related reports. The method does not involve deep learning or non-linear models, relying instead on probabilistic inference and feature weighting. The final model selects the class with the highest posterior probability for each document. The system's performance is reported as an F-score of 94.7 when combining both word-level and UMLS features.  
DOMAIN: medical informatics  
STRUCTURE: graphical models  
DATA_OBJECT: sequence or time-series  
INFERENCE: Bayesian posterior  
PROBLEM_FORM: classification  
DISTRIBUTION: binary; multinomial  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-private-data
