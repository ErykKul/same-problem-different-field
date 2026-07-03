MECHANISM: The paper computes a nonparametric maximum likelihood estimator for a multivariate mixing distribution. The algorithm alternates between two steps: first, solving a convex optimization problem to find optimal weights for a given set of support points using a primal-dual interior-point method; second, refining the support points via an adaptive grid search. The likelihood function is maximized iteratively by condensing low-probability grid points and expanding high-probability regions. The process continues until convergence, ensuring the support points and weights jointly maximize the log-likelihood. The method does not assume any parametric form for the distribution, allowing arbitrary shapes for the parameters. The primal-dual interior-point method solves the convex subproblem for weights, while the adaptive grid method explores the parameter space to locate support points. The algorithm handles high-dimensional parameter spaces and complex conditional probability models derived from nonlinear differential-algebraic equations. The final estimator is discrete, with at most N support points corresponding to N observed entities. The method is applied to estimate population pharmacokinetic parameters without assuming normality or log-normality of the distribution.  
DOMAIN: population pharmacokinetics  
STRUCTURE: other: iterative optimization with grid search  
DATA_OBJECT: set or table  
INFERENCE: frequentist point estimate  
PROBLEM_FORM: estimation  
DISTRIBUTION: none  
COMPLEXITY: polynomial iterative  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
