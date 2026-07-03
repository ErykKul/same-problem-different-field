MECHANISM: The paper computes a weighted aggregation of causal effect estimates from multiple candidate models, where each model's contribution is modulated by a data-driven measure of its validity. The validity measure is derived from testable implications of each model's identifying assumptions, such as conditional independence or generalized equality constraints. These implications are encoded as observed data parameters, which are estimated from the data. A Gaussian kernel function is applied to these parameters to create smooth weights, avoiding abrupt model selection. The weighted sum forms a triangulation functional that approximates the true causal parameter. The method provides a bound on the distance between the functional and the true parameter, depending on the maximal bias of incorrect models and the separation of correct and incorrect models using observed data. The bound is derived under assumptions of faithfulness and causal ordering. The estimator is consistent for the weighted triangulation functional, and valid statistical inference is derived for it. The approach avoids explicit model selection and post-selection inference problems by using smooth weights. The method is robust to misspecification of some models as long as at least one model is correct and testable. The computational steps involve estimating model-specific functionals, computing validity measures, applying kernel weights, and aggregating estimates into a single functional with theoretical guarantees on its accuracy.
DOMAIN: causal inference
STRUCTURE: other: model combination with kernel weights
DATA_OBJECT: set or table
INFERENCE: frequentist point estimate
PROBLEM_FORM: estimation
DISTRIBUTION: none
COMPLEXITY: finite-sample bound
DATA_AVAILABILITY: none
CODE_AVAILABILITY: none
PREREGISTRATION: none
EVIDENCE_BASIS: simulation-study
