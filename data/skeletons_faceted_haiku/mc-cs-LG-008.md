MECHANISM: Extract records from electronic health systems for entities with a target condition or related conditions. Aggregate numerical measurements and categorical diagnoses over a temporal observation window preceding a prediction window. Train a gradient-boosted tree ensemble to predict binary outcome (disease onset within 1-2 years) from aggregated features. Perform feature selection using trained model importance scores, then conduct hyperparameter optimization via Bayesian search. Evaluate on held-out test data using discrimination and classification metrics, comparing against fixed-formula clinical scores.
DOMAIN: Early prediction of liver cirrhosis from electronic health records
STRUCTURE: map-reduce or embarrassingly-parallel
DATA_OBJECT: dense matrix or tensor
INFERENCE: frequentist point estimate
PROBLEM_FORM: prediction or classification
DISTRIBUTION: binary; binary
COMPLEXITY: polynomial iterative
