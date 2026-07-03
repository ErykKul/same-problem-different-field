MECHANISM: High-dimensional regression selects variables from groups using a convex optimization approach. The Sorted L-One Penalized Estimation (SLOPE) framework applies L1 penalties with decreasing regularization coefficients on sorted regression coefficients. Stepdown rules from hypothesis testing are embedded by modifying the penalty sequence such that if one coefficient is rejected as zero, all smaller coefficients (in absolute value) are also rejected. The algorithm minimizes a penalized loss function where the penalty sequence is chosen to control group-level error rates. For orthogonal designs, closed-form penalty sequences are derived. For general designs, a data-driven calibration uses Gaussian approximation and Monte Carlo correction. The optimization is solved via coordinate descent or proximal gradient algorithms.
DOMAIN: high-dimensional regression and variable selection
STRUCTURE: other: proximal gradient optimization
DATA_OBJECT: sparse matrix
INFERENCE: frequentist point estimate
PROBLEM_FORM: prediction or classification
DISTRIBUTION: none
COMPLEXITY: polynomial iterative
