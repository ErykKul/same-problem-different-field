MECHANISM: The paper computes a generalized additive model (GAM) that combines interpretable predictors derived from a pre-trained foundation model with nonparametric functional estimation. Input data, represented as a multivariate time series, are first transformed through a deep neural network to extract latent predictors corresponding to clinically meaningful ECG diagnostic risks. These predictors, which represent calibrated risks for traditional ECG diagnoses, are then modeled using a GAM framework. The GAM employs B-spline bases to approximate unknown smooth functions that link each predictor to the binary outcome variable. The model's conditional mean response is defined via a link function applied to a linear combination of demographic covariates and the additive contributions of the predictors. Estimation proceeds through penalized logistic regression, incorporating $\ell_2$ regularization to control model complexity. The B-spline basis functions are selected with a fixed order and number of knots, and their coefficients are estimated by minimizing a loss function that balances prediction accuracy and smoothness constraints. The method ensures interpretability by allowing direct inspection of the estimated nonlinear effects of individual predictors on the outcome. The framework is evaluated using a large-scale benchmark dataset, and performance is measured through metrics like AUROC, AUPRC, and F1 score. The approach maintains transparency by avoiding end-to-end black-box modeling while achieving strong predictive performance through the integration of deep learning features with structured statistical modeling.  
DOMAIN: cardiology and biomedical signal processing  
STRUCTURE: other: generalized additive model  
DATA_OBJECT: sequence or time-series  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: prediction or classification  
DISTRIBUTION: binary; logistic  
COMPLEXITY: not stated  
DATA_AVAILABILITY: dataset-with-DOI-or-handle  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
