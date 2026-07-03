MECHANISM: Given an initial parameter estimate, missing values in a sequence are iteratively imputed by sampling from conditional distributions determined by reconstructing a learned systematic component. The systematic component is updated at each step using observed values and imputed values. Parameters are re-estimated using each completed sequence. This procedure repeats multiple times, with parameter estimates pooled to yield a final estimate. The operation forms a dynamical system that converges almost surely to true parameters.
DOMAIN: Time series, statistical inference, missing data imputation
STRUCTURE: dynamic programming
DATA_OBJECT: sequence or time-series
INFERENCE: sampling or Monte-Carlo
PROBLEM_FORM: estimation
DISTRIBUTION: continuous measured distribution, continuous assumed distribution
COMPLEXITY: consistency
