MECHANISM: The paper computes a nonparametric statistical test for comparing multivariate distributions across spatially correlated data. The method begins by transforming raw measurements into pooled componentwise ranks to eliminate sensitivity to marginal distributional form. These ranks are then smoothed using a spatial kernel that weights observations based on proximity to a reference location, creating a kernel-smoothed empirical distribution function (EDF). The smoothed EDFs from each field are combined into a pooled EDF, and a contrast process is constructed by subtracting each field's smoothed EDF from the pooled version. A quadratic test statistic is computed as the weighted sum of squared deviations of the contrast process over discrete thresholds, with weights approximating the underlying distribution's density. Under fixed-domain infill asymptotics and polynomial α-mixing conditions, the normalized contrast process converges weakly to a mean-zero Gaussian process. The test statistic converges in distribution to a weighted sum of chi-squared random variables, with eigenvalues determined by the spatial covariance operator induced by the kernel. For practical inference, the limiting distribution is approximated using a Satterthwaite-type moment-matching approach, which estimates eigenvalues from an exact discrete covariance operator evaluated on a finite grid. The procedure avoids resampling by directly computing p-values from the approximated distribution. The method is extended to multivariate outcomes by evaluating joint indicator functions over a multivariate grid and applying the same asymptotic theory with adjustments for higher-dimensional covariance structures.  
DOMAIN: spatial statistics  
STRUCTURE: other: kernel-smoothed empirical copula  
DATA_OBJECT: continuous function or field  
INFERENCE: frequentist point estimate  
PROBLEM_FORM: decision or test  
DISTRIBUTION: continuous; Gaussian  
COMPLEXITY: convergence rate  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: simulation-study
