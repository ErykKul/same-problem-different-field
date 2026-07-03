MECHANISM: The paper computes coverage degradation of conformal prediction under distribution shift by training a model on training data, calibrating a conformal predictor on a validation set, and evaluating coverage on test data. It uses SHAP values to analyze feature importance concentration, identifying single-feature dependence as a predictive signal for catastrophic failure. The method involves quantifying feature temporal stability via Jaccard similarity between training and test feature value sets, and assessing coverage restoration through periodic retraining. The algorithm iteratively trains models, splits data into calibration and evaluation subsets, and computes mean coverage with standard deviation across trials. It identifies robustness through feature importance redistribution and evaluates the impact of retraining frequency on coverage. The analysis includes hypothesis testing for correlations between feature stability, task complexity, and coverage degradation, and applies a decision framework based on SHAP concentration thresholds. The method does not involve sampling, Bayesian inference, or optimization beyond model training and calibration.  
DOMAIN: conformal prediction under distribution shift  
STRUCTURE: other: model calibration and evaluation  
DATA_OBJECT: feature set  
INFERENCE: frequentist point estimate  
PROBLEM_FORM: estimation  
DISTRIBUTION: proportion or bounded; exchangeability  
COMPLEXITY: not stated  
DATA_AVAILABILITY: dataset-with-DOI-or-handle  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
