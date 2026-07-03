MECHANISM: A parallel imaging reconstruction solves an analysis-sparse model enforcing weighted L1 constraints on tight frame coefficients in both time and spatial dimensions. The model minimizes data consistency loss plus weighted sparsity penalties. A modified projected fast iterative soft-thresholding (pFISTA) algorithm applies soft-thresholding with weighting to solve the convex L1 problem. The weighting parameters balance temporal versus spatial sparsity, allowing flexible prioritization. Convergence is guaranteed when step size is appropriately bounded.
DOMAIN: Medical imaging - dynamic contrast-enhanced MRI reconstruction
STRUCTURE: sparse linear algebra
DATA_OBJECT: sparse matrix
INFERENCE: optimization only
PROBLEM_FORM: reconstruction or denoising
DISTRIBUTION: none
COMPLEXITY: polynomial iterative
