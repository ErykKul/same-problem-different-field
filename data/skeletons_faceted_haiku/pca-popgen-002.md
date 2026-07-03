MECHANISM: Principal component analysis (eigen-decomposition) is applied to an uncentered sample covariance matrix CC^T of genotype data, where C is an M×N matrix (M individuals, N markers; entries are counts of variant alleles: 0, 1, or 2). The eigenvalues of this matrix are extracted in decreasing order. The number of subpopulations K is estimated by counting eigenvalues that exceed a threshold t' = ((1+F)/2)(sqrt(M)+sqrt(N))^2, where F is a maximum inbreeding parameter. The method relies on a mathematical model showing that: (1) K large eigenvalues arising from population structure are separated by a factor proportional to M from (2) a bulk of smaller eigenvalues corresponding to random individual variation. Detection power depends on M (number of individuals) more than N (number of markers).
DOMAIN: Population genetics
STRUCTURE: dense linear algebra
DATA_OBJECT: dense matrix or tensor
INFERENCE: deterministic or closed-form
PROBLEM_FORM: estimation
DISTRIBUTION: binary; binomial
COMPLEXITY: not stated
