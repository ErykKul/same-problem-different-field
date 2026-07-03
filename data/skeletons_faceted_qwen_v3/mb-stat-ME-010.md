MECHANISM: The paper computes a constrained maximum likelihood estimator (CMLE) that integrates individual participant data (IPD) with aggregate data (AD) under dataset shift. The method formulates a likelihood function combining IPD and AD constraints, where AD is treated as estimates of parameters satisfying unbiased population estimating equations. These constraints are imposed as equality conditions on the likelihood derived from IPD. To handle uncertainty in AD, the method assumes the summary estimates are approximately normal and incorporates their likelihood contribution. The CMLE is solved via Lagrange multipliers, with the solution expressed as a function of the observed data and constraints. The algorithm is extended to accommodate dataset shift by introducing a general density ratio model linking the data-generating mechanisms of IPD and AD. This model derives unbiased estimating equations for AD and develops unified CMLE procedures valid under shifts like covariate shift and prior probability shift. A non-iterative algorithm is proposed to improve numerical stability and scalability, particularly when AD includes high-dimensional constraints. The method is applied to two empirical examples involving income and housing data under different shift scenarios. The computational steps involve: (1) defining the parametric model for the conditional density of the outcome given covariates; (2) formulating the constrained likelihood with AD constraints; (3) solving the optimization problem via Lagrange multipliers; (4) adjusting for AD uncertainty using a normal approximation; (5) extending the framework to handle dataset shift through density ratio modeling; (6) implementing a non-iterative algorithm to compute the estimator efficiently. The method retains theoretical advantages of CMLE while addressing computational challenges in high-dimensional settings.  
DOMAIN: statistical data integration  
STRUCTURE: other: constrained maximum likelihood estimation  
DATA_OBJECT: set or table  
INFERENCE: frequentist point estimate  
PROBLEM_FORM: estimation  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: simulation-study
