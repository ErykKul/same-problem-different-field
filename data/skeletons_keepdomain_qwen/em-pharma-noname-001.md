MECHANISM: The paper computes a nonparametric maximum likelihood (NPML) estimator for multivariate mixing distributions in population pharmacokinetics. The method begins by formulating the infinite-dimensional NPML problem as a finite-dimensional optimization task, where the support points (representing patient-specific parameter sets) are determined through an adaptive grid search. The probabilities assigned to these support points are optimized using a primal-dual interior-point method, which solves a constrained convex optimization problem. The algorithm iteratively refines the locations of support points by evaluating the likelihood function over a discretized parameter space, with the number of support points bounded by the number of observed subjects. The method does not assume a parametric form for the mixing distribution, allowing it to capture arbitrary shapes of the underlying parameter distribution. The optimization process enforces constraints to ensure the estimated distribution remains a valid probability measure. The approach is applied to high-dimensional pharmacokinetic parameters, with each support point corresponding to a patient's parameter set. The algorithm's steps include: (1) initializing an adaptive grid over the parameter space, (2) solving the dual problem to find optimal probabilities, (3) updating support point locations based on the dual solution, and (4) iterating until convergence. The method is validated through empirical applications in pharmacometric studies, demonstrating its ability to handle complex, high-dimensional mixture models without distributional assumptions.  
DOMAIN: population pharmacokinetics, nonparametric estimation  
STRUCTURE: optimization-based  
DATA_OBJECT: point set  
INFERENCE: frequentist point estimate  
PROBLEM_FORM: estimation  
DISTRIBUTION: continuous; discrete  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
