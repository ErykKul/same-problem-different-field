MECHANISM: Transform observed outcome into its empirical CDF value, then fit a beta regression model with mean and precision parameters. The mean structure links covariates to the CDF-transformed response via logit link; the precision structure models dispersion via log link. Map fitted CDF values back to original scale using empirical quantile function. Inference uses bootstrap resampling that recalculates both CDF and refits beta model on each replicate. Prediction intervals are generated on CDF scale via beta quantiles, then mapped to original outcome scale.
DOMAIN: Heteroscedastic regression with non-normal errors
STRUCTURE: other: distribution-centric likelihood maximization
DATA_OBJECT: dense matrix or tensor
INFERENCE: bootstrap or resampling
PROBLEM_FORM: estimation
DISTRIBUTION: continuous measured; beta assumed on transformed scale
COMPLEXITY: not stated
