MECHANISM: Decomposes grain size distribution data matrix into product of abundance and end-member matrices via nonnegative matrix factorization with row-sum-to-one constraints; formulates maximum volume constrained optimization by maximizing determinant of end-member covariance matrix subject to data reconstruction error; proves uniqueness theorem under sufficiently scattered condition constraints; solves via alternating projected fast gradient method (APFGM) that sequentially optimizes abundance rows (quadratic programming) and end-member rows (quadratic programming) with volume regularization; uses determinant of end-member Gram matrix as volume measure to identify maximally dispersed end-members in highly mixed distributions.
DOMAIN: End member analysis for sediment grain size distribution unmixing
STRUCTURE: sparse linear algebra
DATA_OBJECT: dense matrix or tensor
INFERENCE: deterministic or closed-form
PROBLEM_FORM: estimation
DISTRIBUTION: none
COMPLEXITY: polynomial iterative
