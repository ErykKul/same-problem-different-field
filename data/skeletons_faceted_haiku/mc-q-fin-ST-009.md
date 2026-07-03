MECHANISM: The methodology employs a double-selection LASSO (DS-LASSO) framework with three stages: (1) LASSO regression of portfolio mean returns on traditional factor covariances to select a core control set; (2) LASSO regression of each target factor's covariance with returns on the full control universe to identify additional controls; (3) OLS regression of portfolio returns on combined controls and all target factors to assess incremental explanatory power. Heteroscedasticity-robust standard errors are computed. The approach is applied to test 191 short-term trading factors against S&P 500 constituent returns, comparing factor survival and coefficient stability across 3x2 and 5x5 portfolio constructions, with robustness checks using Elastic Net and PCA dimensionality reduction.
DOMAIN: Factor models and equity cross-section
STRUCTURE: sparse linear algebra
DATA_OBJECT: dense matrix or tensor
INFERENCE: frequentist point estimate
PROBLEM_FORM: estimation
DISTRIBUTION: none
COMPLEXITY: polynomial iterative
