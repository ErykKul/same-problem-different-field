MECHANISM: The paper computes a classification algorithm that modifies linear discriminant analysis (LDA) to handle heteroscedastic class distributions. It projects input vectors onto a lower-dimensional space using a weight vector derived from minimizing mean squared error. The method estimates the mean and standard deviation of projected data for each class, then normalizes these values using z-scores to define a decision boundary. This boundary is determined by the intersection of two Gaussian distributions parameterized by class-specific means and standard deviations. For a new input, the algorithm computes its projected weight sum, applies z-score normalization relative to training-set-derived parameters, and classifies the input based on which class's distribution the normalized value falls closer to. The approach generalizes conventional LDA by incorporating variance information into the decision boundary, reducing to standard LDA when class variances are equal. The method assumes Gaussian distributions for class-conditional data and uses deterministic calculations without explicit probabilistic modeling.  
DOMAIN: brain-computer interfaces  
STRUCTURE: dense linear algebra  
DATA_OBJECT: dense matrix  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: classification  
DISTRIBUTION: binary; Gaussian  
COMPLEXITY: closed-form  
DATA_AVAILABILITY: public-benchmark-used  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
