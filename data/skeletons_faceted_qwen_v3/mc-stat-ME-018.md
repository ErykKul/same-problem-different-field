MECHANISM: This paper computes the iterative updates of a parameter vector using stochastic gradient descent (SGD) under temporally dependent data. The algorithm processes a sequence of data points, each consisting of a covariate vector and a scalar response, and updates the parameter estimate using a stepsize schedule. The update rule subtracts a scaled gradient of the loss function, computed from the current data point and the current parameter estimate. The stepsize is chosen to ensure convergence, with conditions on its decay rate. The analysis derives non-asymptotic bounds on the estimation error and regret, showing that the final iterate of SGD achieves optimal rates even under dependent data. The method accommodates both martingale-type dependence in covariates and noise, as well as dependence induced by sequential decision making. The paper establishes that the iterates converge to a Gaussian distribution asymptotically, with a remainder term decaying as $O(1/\sqrt{t})$. A conic approximation of the decision region is introduced to handle unbounded covariates, and a sparse regression algorithm is proposed with storage cost $d$ and per-iteration computation $O(d)$. The analysis leverages conditional Orlicz norms to generalize results beyond independent and identically distributed data, ensuring robustness to non-stationary and non-mixing processes. Tail bounds are derived for the estimation error, demonstrating that the performance matches idealized i.i.d. Gaussian settings under mild regularity conditions. The method is validated through theoretical guarantees, including finite-sample bounds and convergence rates, without requiring explicit knowledge of the underlying dependence structure.  
DOMAIN: statistical learning theory  
STRUCTURE: polynomial iterative  
DATA_OBJECT: sequence or time-series  
INFERENCE: frequentist point estimate  
PROBLEM_FORM: estimation  
DISTRIBUTION: continuous; gaussian  
COMPLEXITY: finite-sample bound  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: mathematical-proof
