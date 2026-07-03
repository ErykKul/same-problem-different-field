MECHANISM: The paper computes a statistical model that factorizes a non-negative data matrix into a shared non-negative basis matrix, a covariate-effect matrix, and unit-specific random effects. The algorithm alternates between closed-form ridge updates for the random effects and multiplicative non-negative updates for the basis and covariate matrices. For inference on the covariate matrix, it conditions on estimated basis and random effects, applies asymptotic linearization, performs a one-step Newton update, and uses a multiplier bootstrap to quantify uncertainty. The model enforces non-negativity constraints and monitors effective degrees of freedom to prevent overfitting. The random effects act as a penalty mechanism, with their complexity controlled via a diagnostic cap on degrees of freedom. The method avoids repeated constrained optimization by leveraging post-regularization techniques. The non-negativity constraints induce sparse, parts-based loadings, while inference identifies which covariates influence which components. The algorithm scales to moderate and large matrices through block-wise updates and numerical stabilization.  
DOMAIN: statistical modeling  
STRUCTURE: other: alternating updates  
DATA_OBJECT: dense matrix  
INFERENCE: sampling or Monte-Carlo  
PROBLEM_FORM: estimation  
DISTRIBUTION: continuous; continuous  
COMPLEXITY: not stated  
DATA_AVAILABILITY: public-repository  
CODE_AVAILABILITY: public-repository  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
