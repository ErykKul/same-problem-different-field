MECHANISM: A two-sample hypothesis test compares multivariate distributions across spatial locations. Observations are transformed to ranks to remove dependence on marginal distributions. An empirical copula process is constructed from the ranks, capturing joint distributional structure. Spatial kernel weights are applied based on inter-location distances to account for autocorrelation. The copula process is smoothed via kernel averaging. A quadratic test statistic is computed by integrating the squared smoothed copula process over the domain. Under spatial mixing conditions, the limiting distribution of the test statistic is derived as a weighted chi-squared. Inference uses a Satterthwaite approximation calibrated by a Gaussian copula model to compute critical values.
DOMAIN: spatial statistics and hypothesis testing
STRUCTURE: other: kernel smoothing with rank statistics
DATA_OBJECT: dense matrix or tensor
INFERENCE: frequentist point estimate
PROBLEM_FORM: decision or test
DISTRIBUTION: continuous
COMPLEXITY: polynomial iterative
