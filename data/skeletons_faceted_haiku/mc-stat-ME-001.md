MECHANISM: Decomposes spatial domain via 2D Haar wavelet basis into multi-resolution scaling and detail coefficients (horizontal, vertical, diagonal); expresses intensity function as sum over predictors and wavelet coefficients via wavelet expansion; transforms Poisson point process likelihood via Campbell's theorem; applies regularized intensity estimation using LASSO penalty on wavelet-expanded coefficients to select predictors at local resolution levels; enables variable selection that identifies both whether a covariate matters and where and at what spatial scale; extends classical variable selection methods (LASSO, Adaptive LASSO, SCAD) from global to multi-resolution local setting; evaluates predictions on spatial point patterns.
DOMAIN: Local variable selection for spatial point processes with wavelets
STRUCTURE: sparse linear algebra
DATA_OBJECT: point set
INFERENCE: frequentist point estimate
PROBLEM_FORM: estimation
DISTRIBUTION: continuous; continuous
COMPLEXITY: polynomial iterative
