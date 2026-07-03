MECHANISM: The paper computes a test-time adaptation framework for time-series forecasting and classification. It processes input windows of length L, composed of sequences of entities, and applies weak time-preserving transformations to generate augmented views. For classification, it minimizes entropy of predicted probabilities while enforcing consistency between predictions from original and transformed windows. For regression, it minimizes variance across predictions from transformed windows and optionally distills from an exponential-moving-average teacher. A quadratic penalty term constrains daily parameter updates to prevent drift. When uncertainty proxies (mean entropy or augmentation variance) exceed a threshold, it falls back to refreshing batch-normalization statistics without gradient updates. The backbone model remains frozen, and only normalization affine parameters are updated using unlabeled test data. The method balances adaptation to non-stationary distributions with stability through drift control and uncertainty-triggered fallbacks. It evaluates performance on synthetic and real-world time-series data using metrics like MAE, RMSE, and AUC. The algorithm iteratively applies gradient steps on unsupervised objectives, with hyperparameters controlling update frequency, window size, and penalty strength.  
DOMAIN: time series forecasting and adaptation  
STRUCTURE: other: iterative optimization  
DATA_OBJECT: sequence or time-series  
INFERENCE: optimization only  
PROBLEM_FORM: prediction or classification  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: public-repository  
CODE_AVAILABILITY: public-repository  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
