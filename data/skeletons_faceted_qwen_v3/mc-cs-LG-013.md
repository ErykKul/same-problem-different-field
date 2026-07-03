MECHANISM: The paper computes a statistical test for unobserved confounders in nonlinear observational data using kernel methods. It maps treatment, outcome, and covariate variables into a reproducing kernel Hilbert space (RKHS), enabling linear inner-product representations of nonlinear relationships. Two kernel regressions are performed: a standard regression and a higher-order regression weighted by the squared norm of the input variables. The difference between the resulting regression coefficients is normalized and tested against a null hypothesis of no unobserved confounders. Under the null hypothesis, the coefficients coincide exactly in infinite samples, and their finite-sample difference converges to a zero-mean Gaussian distribution with tractable variance. The method constructs a hypothesis test by comparing the normalized coefficient differences across all dimensions of the RKHS basis. Theoretical guarantees ensure that significant deviations from zero indicate unobserved confounding. The algorithm involves solving regularized empirical risk minimization problems in a finite-dimensional subspace of the RKHS, deriving closed-form solutions for the regression coefficients, and applying asymptotic normality to construct the test statistic. The computational steps include kernel matrix construction, inversion of regularized matrices, and hypothesis testing based on the asymptotic distribution of the coefficient differences. The method does not assume linearity, parametric forms, or multiple environments, making it applicable to general nonlinear single-environment settings.  
DOMAIN: causal inference  
STRUCTURE: other: kernel regression-based method  
DATA_OBJECT: dense matrix or tensor  
INFERENCE: sampling or Monte-Carlo  
PROBLEM_FORM: decision or test  
DISTRIBUTION: continuous; Gaussian  
COMPLEXITY: polynomial iterative  
DATA_AVAILABILITY: public-benchmark-used  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
