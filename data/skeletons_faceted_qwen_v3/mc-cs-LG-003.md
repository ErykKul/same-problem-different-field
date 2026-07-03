MECHANISM: The paper computes a gradient-boosted ensemble of decision trees to predict accident severity from a set of features. The algorithm iteratively builds trees that correct residuals from prior models, with each tree contributing a weighted adjustment to the cumulative prediction. Hyperparameters are optimized via randomized search cross-validation, which samples configurations from a predefined space and evaluates performance on held-out data. Class imbalance is addressed by assigning higher weights to underrepresented severity levels during training, ensuring the model prioritizes accurate prediction of rare outcomes. Feature importance is derived from the magnitude of each variable's contribution to reducing prediction error across the ensemble. The model operates on a table of observations, each with values for time, location, and environmental variables, and outputs a probability distribution over severity levels (1–4). No explicit probabilistic modeling is performed; instead, the final prediction is the class with the highest cumulative tree output. The method does not incorporate uncertainty quantification or Bayesian inference, relying solely on deterministic tree-based aggregation. The computational steps include data preprocessing (imputation, outlier removal), feature selection, and iterative tree training with early stopping to prevent overfitting. The model's performance is evaluated using precision, recall, and accuracy metrics on a held-out test set.  
DOMAIN: traffic accident prediction  
STRUCTURE: other: gradient-boosted ensemble  
DATA_OBJECT: set or table  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: prediction or classification  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: dataset-with-DOI-or-handle  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
