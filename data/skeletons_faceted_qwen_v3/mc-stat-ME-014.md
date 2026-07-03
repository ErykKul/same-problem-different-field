MECHANISM: The paper computes a modified Bayesian Information Criterion (BIC) that incorporates the determinant of the Hessian matrix of the log-likelihood function. The method begins by maximizing the log-likelihood of a statistical model to obtain parameter estimates. It then computes the Hessian matrix of the log-likelihood at this maximum, which captures the local curvature of the likelihood surface. The determinant of this Hessian (or its approximation via the Fisher information matrix) is calculated and added to the standard BIC formula as a penalty term. This adjustment accounts for the geometric structure of the likelihood landscape, introducing a data-dependent penalty that depends on the number of parameters, sample size, and residual variance. The modified criterion, termed BIC_HES, is used to compare nested or non-nested models by evaluating the trade-off between model fit (via the log-likelihood) and complexity (via the determinant term). The method relies on asymptotic approximations for the determinant of the Fisher information matrix, which are derived analytically for specific model classes (e.g., mixed-effects models). The final criterion is applied to select the model with the highest BIC_HES value, which balances goodness-of-fit against the adjusted complexity penalty. The approach is validated through theoretical consistency guarantees and simulation studies that compare its performance against classical BIC and AIC.  
DOMAIN: Bayesian model selection  
STRUCTURE: dense linear algebra  
DATA_OBJECT: dense matrix  
INFERENCE: Bayesian posterior  
PROBLEM_FORM: model selection  
DISTRIBUTION: none  
COMPLEXITY: consistency  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: simulation-study
