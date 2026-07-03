MECHANISM: Factor non-negative data as Y = X(ΘA+U)+E where X is learned basis, Θ captures covariate effects, U is random deviation. Alternate ridge-type closed-form updates for U with multiplicative non-negative updates for X and Θ. Monitor effective degrees of freedom and enforce cap to prevent saturation. Conduct inference on Θ via asymptotic linearization, one-step Newton update, and wild bootstrap. Measurement-side variable selection from non-negativity; covariate-side selection from significance tests.
DOMAIN: Non-negative matrix factorization with covariates
STRUCTURE: other: block-wise multiplicative updates
DATA_OBJECT: dense matrix or tensor
INFERENCE: bootstrap or resampling
PROBLEM_FORM: estimation
DISTRIBUTION: none
COMPLEXITY: not stated
