MECHANISM: Embed a collection of scalar measurements (treatment, covariates, outcome) into a reproducing kernel Hilbert space via a kernel function, mapping the nonlinear regression problem into a linear one on the feature space. Compute two weighted least-squares estimators by minimizing squared regression error: one with uniform weights and one with weights proportional to squared norm of the covariate vector. Express each estimator as a coefficient vector in the kernel feature space. Compare the coefficient vectors coordinate-wise and test whether their differences are statistically significant relative to their sampling variability, which follows an asymptotic normal distribution.
DOMAIN: Causal inference and confounder detection
STRUCTURE: spectral or transform
DATA_OBJECT: dense matrix or tensor
INFERENCE: frequentist point estimate
PROBLEM_FORM: decision or test
DISTRIBUTION: continuous; continuous
COMPLEXITY: polynomial iterative
