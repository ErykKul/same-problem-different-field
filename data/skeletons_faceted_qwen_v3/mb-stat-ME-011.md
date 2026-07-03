MECHANISM: The paper computes an estimator for the overlapping coefficient of k≥2 normal distributions. The method involves three steps: (1) estimating parameters of each distribution using maximum likelihood estimators (MLEs) from sampled data, (2) transforming the integral of the minimum of density functions from the infinite real line to a finite interval via a logistic transformation, and (3) applying Simpson’s rule for numerical integration on the transformed interval. The integrand is the minimum of k estimated density functions, which is piecewise defined over intervals determined by pairwise intersections of densities. The estimator is derived by substituting MLEs into the density functions, transforming the integral domain, and approximating the integral using Simpson’s rule with evenly spaced subintervals. The method ensures consistency under standard regularity conditions by leveraging the convergence of MLEs and uniform convergence of the transformed integrand. The computational steps are independent of the specific application domain, relying only on the mathematical structure of normal densities and numerical integration.  
DOMAIN: statistics - normal distributions - overlapping coefficient  
STRUCTURE: other: numerical integration  
DATA_OBJECT: continuous function or field  
INFERENCE: frequentist point estimate  
PROBLEM_FORM: estimation  
DISTRIBUTION: continuous; normal  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: simulation-study
