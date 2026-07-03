MECHANISM: An incomplete matrix is formed where rows index entities, columns index periods, and entries are partially observed quantities. The observed entries are used to reconstruct the missing entries by solving a regularized optimization. A candidate matrix is found that minimizes the reconstruction error on observed entries plus a penalty proportional to the sum of its singular values, which induces low-rank structure. The optimization is a convex program, and the regularization weight is chosen by cross-validation on held-out observed entries. The estimated missing entries are the imputed quantities for the unobserved cases. This objective nests additive row-plus-column factor models and weighted-combination estimators as special cases, differing only in how identification is achieved.
DOMAIN: causal inference
STRUCTURE: dense linear algebra
DATA_OBJECT: dense matrix or tensor
INFERENCE: optimization only
PROBLEM_FORM: estimation
DISTRIBUTION: none
COMPLEXITY: polynomial iterative
DATA_AVAILABILITY: public-benchmark-used
CODE_AVAILABILITY: public-repository
PREREGISTRATION: none
EVIDENCE_BASIS: simulation-study
