MECHANISM: The paper computes a penalized regression method called IPF-LASSO for integrating multiple omics data modalities (e.g., gene expression, methylation, copy number) to predict clinical outcomes. The method assigns distinct penalty factors to each data modality, which are optimized via cross-validation or practical considerations. The penalty factors scale the L1 regularization applied to variables from different modalities, allowing for differential feature selection across data types. The optimization problem is formulated as minimizing a loss function (e.g., squared error) plus a weighted sum of L1 penalties, where weights depend on the modality-specific penalty factors. The solution is computed using coordinate descent or similar iterative methods, with convergence criteria based on tolerance thresholds. The method is compared to standard LASSO and sparse group LASSO in simulations and applied to two real cancer datasets. The penalty factors are estimated by minimizing cross-validated prediction error, and the final model selects features based on the magnitude of their coefficients. The approach is implemented in the R package `ipflasso`, which includes functions for fitting the model, cross-validation, and prediction. The method is evaluated using metrics such as mean squared error, area under the ROC curve, and variable selection accuracy. The paper emphasizes reproducibility by releasing all data and code on a companion website.
DOMAIN: biostatistics and machine learning for multi-omics data
STRUCTURE: sparse linear algebra
DATA_OBJECT: set or table
INFERENCE: deterministic or closed-form
PROBLEM_FORM: prediction or classification
DISTRIBUTION: none
COMPLEXITY: not stated
DATA_AVAILABILITY: dataset-in-repository
CODE_AVAILABILITY: public-repository
PREREGISTRATION: none
EVIDENCE_BASIS: empirical-with-released-data
