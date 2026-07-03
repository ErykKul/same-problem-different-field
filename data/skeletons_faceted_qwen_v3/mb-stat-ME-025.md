MECHANISM: The paper computes a semi-partitioned Generalized Method of Moments (GMM) estimator for longitudinal data with time-dependent covariates. The method begins by defining moment conditions as functions of observed covariates and parameters, which are averaged across subjects to form a sample analog. These moment conditions are structured to distinguish contemporaneous (lag-0) effects from lagged effects, grouping the latter into predefined blocks (e.g., near vs. distant lags). The estimator minimizes a quadratic form of the sample moment vector, weighted by a positive semi-definite matrix, to obtain parameter estimates. For continuous outcomes, the model uses an identity link function; for binary outcomes, a logistic link function is applied. The weighting matrix is optimized in two steps, with the second step using a consistent estimate of the long-run covariance matrix. The BFGS algorithm is employed for numerical optimization, which iteratively updates parameter estimates by approximating the Hessian matrix. Moment conditions are partitioned based on the validity of covariate types (Type I, II, III) and their temporal relationships. The grouping of lagged effects reduces dimensionality by imposing equality constraints within blocks, allowing for interpretable lag-group effects while maintaining flexibility in the marginal mean structure. The method accommodates feedback dynamics by allowing outcomes to influence future covariate structures, and it avoids over-parameterization by limiting the number of parameters relative to fully partitioned models. Estimation is validated through simulations and applied to real-world datasets with both continuous and binary outcomes.
DOMAIN: longitudinal marginal modeling
STRUCTURE: other: optimization-based
DATA_OBJECT: set or table
INFERENCE: deterministic or closed-form
PROBLEM_FORM: estimation
DISTRIBUTION: continuous and binary; logistic and identity
COMPLEXITY: not stated
DATA_AVAILABILITY: none
CODE_AVAILABILITY: none
PREREGISTRATION: none
EVIDENCE_BASIS: simulation-study
