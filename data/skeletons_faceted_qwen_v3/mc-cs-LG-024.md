MECHANISM: The paper computes a method to estimate the correct labels of original inputs from adversarial examples (AEs) by re-attacking them. The process begins with an input perturbed to create an AE, which is assumed to lie near the decision boundary in the feature space. The method applies iterative gradient-based perturbations to the AE, reducing the confidence of the misclassified category while increasing the confidence of the correct category. Each iteration adjusts the input along the gradient direction that maximizes the change in classification confidence. The process continues until the model's output changes to the correct label. The method does not require prior training or parameter adjustments, as it operates under the assumption that all inputs are AEs. It leverages the fragility of AEs, which are susceptible to small perturbations that alter their classification. The algorithm iteratively computes gradients, applies them to the AE, and evaluates the resulting classification. This is repeated until the classification result aligns with the original input's label. The method is effective for both white-box and black-box attacks, though black-box scenarios may require additional steps due to the absence of gradient information. The process is deterministic, relying on gradient descent to move the AE beyond the decision boundary. The method's success depends on the AE's proximity to the decision boundary and the effectiveness of gradient-based perturbations in correcting misclassification.  
DOMAIN: adversarial machine learning  
STRUCTURE: optimization only  
DATA_OBJECT: point set  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: estimation  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
