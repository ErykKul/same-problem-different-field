MECHANISM: The paper computes a two-stage estimation procedure for the STARTS model by combining matrix decomposition factor analysis (MDFA) with structural equation modeling (SEM) principles. The first stage involves eigenvalue decomposition of a data matrix to extract latent factors, which are then used to initialize parameter estimates. The second stage refines these estimates using iterative least-squares optimization on the data space rather than the covariance space. The method reformulates the STARTS model within a factor-analytic framework, decomposing observed variables into stable trait components, autoregressive temporal deviations, and measurement errors. The algorithm ensures non-negative variance estimates by construction, avoiding improper solutions through the inherent properties of MDFA. The process iteratively minimizes a loss function derived from the sample covariance matrix, with constraints applied to maintain admissible parameter regions. The method does not require prior distributions, unlike Bayesian approaches, and mitigates instability by decoupling variance components during decomposition. The computational steps include matrix decomposition, initialization of latent factors, iterative parameter updates, and validation against empirical data. The approach is compared to maximum likelihood, constrained ML, and unweighted least squares estimators through simulation and real-world application. The method's effectiveness is evaluated by measuring the frequency of improper solutions, bias, and computational efficiency across different scenarios.

DOMAIN: psychology

STRUCTURE: spectral or transform

DATA_OBJECT: matrix

INFERENCE: deterministic or closed-form

PROBLEM_FORM: estimation

DISTRIBUTION: continuous; continuous

COMPLEXITY: not stated

DATA_AVAILABILITY: none

CODE_AVAILABILITY: none

PREREGISTRATION: none

EVIDENCE_BASIS: simulation-study
