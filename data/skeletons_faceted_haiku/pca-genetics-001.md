MECHANISM: Principal component analysis (PCA) is applied to a genotype matrix to decompose it into a low-rank product (top k principal components times loadings), and the quality of this factorization is assessed by computing residuals (observed minus predicted genotypes). The method calculates two correlation matrices of the residuals: an empirical covariance/correlation matrix and a model-based estimated version. When the model is correct, these two matrices should agree (their difference approaches zero as sample size grows). Deviations between the matrices signal model misfit. The procedure is tested on three PCA variants (unnormalized, mean-centered, mean-and-variance-normalized data) and on ADMIXTURE software output, using theoretical results to characterize when agreement should occur.
DOMAIN: Genetics and population structure analysis
STRUCTURE: dense linear algebra
DATA_OBJECT: dense matrix or tensor
INFERENCE: deterministic or closed-form
PROBLEM_FORM: estimation
DISTRIBUTION: binary; binomial
COMPLEXITY: not stated
