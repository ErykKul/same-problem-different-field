MECHANISM: Apply linear transformation (least squares) to project feature vectors onto a lower-dimensional space that maximizes variance between classes while minimizing within-class variance. Estimate mean and standard deviation of the projected data for each class. Define decision boundary using z-score normalization of projected test data, measuring deviation from each class mean relative to that class's standard deviation. Assign new instances to the class with smallest absolute z-score.
DOMAIN: Brain-computer interface classification for EEG signals
STRUCTURE: dense linear algebra
DATA_OBJECT: dense matrix or tensor
INFERENCE: deterministic or closed-form
PROBLEM_FORM: classification
DISTRIBUTION: continuous; Gaussian
COMPLEXITY: polynomial iterative
