MECHANISM: The paper computes an augmented inverse probability weighted (AIPW) score function for estimating the average dose-response function (ADRF) under a debiased machine learning (DML) framework. The method relies on defining a regular weighting function (RWF) and a uniform RWF to ensure local identification of the ADRF over subsets of the treatment space. The AIPW score is derived using semiparametric theory, incorporating a mixed-bias property that ensures its conditional expectation equals the ADRF. A cross-fitting algorithm is employed to compute the AIPW score, leveraging local linear kernel regression (LLKR) and empirical risk minimization for nonparametric and local estimation of the ADRF. The approach accommodates unmeasured confounding by enforcing an additive instrumental variable (AIV) condition, which ensures the treatment model satisfies a no-interaction assumption between the instrument and latent confounders. Hypothesis testing procedures are established to validate the RWF condition, and asymptotic properties such as convergence rates and normality are derived for the estimator. The method is applied to both simulated and empirical data to assess finite-sample performance.  
DOMAIN: causal inference with instrumental variables  
STRUCTURE: other: statistical estimation with machine learning  
DATA_OBJECT: set or table  
INFERENCE: frequentist point estimate  
PROBLEM_FORM: estimation  
DISTRIBUTION: continuous; continuous  
COMPLEXITY: not stated  
DATA_AVAILABILITY: public-repository  
CODE_AVAILABILITY: public-repository  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
