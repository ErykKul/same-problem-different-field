MECHANISM: Trains three regression models (XGBoost via sequential tree ensemble gradient boosting, EBM via additive gradient boosting with per-feature shape functions, and stacked EBM+XGBoost meta-learner) on historical time-series features; XGBoost optimizes loss plus regularization via second-order gradients; EBM learns additive contributions of each feature via gradient boosting with smooth function approximation, maintaining feature independence; stacking uses EBM residuals as targets for XGBoost meta-learner; evaluates all models on test set using regression metrics; extracts per-feature contributions from EBM for interpretability.
DOMAIN: Energy balancing market price forecasting with interpretability
STRUCTURE: other: gradient boosting ensemble
DATA_OBJECT: sequence or time-series
INFERENCE: frequentist point estimate
PROBLEM_FORM: prediction or classification
DISTRIBUTION: continuous; continuous
COMPLEXITY: polynomial iterative
