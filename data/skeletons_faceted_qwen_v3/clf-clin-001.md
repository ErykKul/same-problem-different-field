MECHANISM: The paper computes a probabilistic classification of text documents into two categories using a multinomial naïve Bayes model. The method begins by extracting features from the text, which are represented as counts of terms or concepts. Features are derived from both raw word occurrences and structured medical concepts from a controlled vocabulary. The classifier assumes independence between features within each document and calculates the probability of document membership in each category based on feature frequencies. Training involves estimating the likelihood of each feature under each category using maximum likelihood estimation. During inference, the posterior probability of each category is computed for a new document by combining feature likelihoods with prior category probabilities. The classification decision selects the category with the highest posterior probability. The method combines two feature sets: one based on raw word frequencies and another based on concept identifiers from a medical ontology. The combined feature set improves classification accuracy by leveraging both lexical and semantic information. The algorithm uses logarithmic transformations to avoid numerical underflow and applies a ten-fold cross-validation to assess performance. Evaluation metrics include precision, recall, and the balanced F-score, which measure the accuracy of category assignments against a manually annotated gold standard.  
DOMAIN: medical document classification  
STRUCTURE: graphical models  
DATA_OBJECT: set or table  
INFERENCE: Bayesian posterior  
PROBLEM_FORM: classification  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-private-data
