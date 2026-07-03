MECHANISM: The paper computes the convergence rates and finite-sample guarantees of the expectation-maximization (EM) algorithm under distributional misspecification and nonidentifiability induced by group actions. It defines a population EM map and a sample EM map, where the population map is analyzed for contraction properties using the spectral radius of its linearization on a local slice of the quotient parameter space. The sample map is treated as a perturbation of the population map, with deviations controlled via generic chaining and entropy bounds on EM-induced empirical processes. The algorithm iteratively computes a sequence of parameter estimates by maximizing a surrogate objective derived from the observed log-likelihood, and the error is measured using an arbitrary integral probability metric (IPM) over the quotient space. The analysis derives sharp local linear convergence rates for the population EM, tight finite-sample bounds for the sample EM, and transfers these results to distributional error metrics via regularity conditions on the model map. The method ensures orbit-invariance by working on the quotient space and avoids dependence on arbitrary parameter choices by focusing on the KL projection set as the target. The computational steps include linearizing the EM map, bounding perturbations, and applying complexity control through entropy and chaining techniques.  
DOMAIN: statistical inference, latent variable models, EM algorithm  
STRUCTURE: spectral or transform  
DATA_OBJECT: set or table  
INFERENCE: frequentist point estimate  
PROBLEM_FORM: estimation  
DISTRIBUTION: none  
COMPLEXITY: finite-sample bound  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: mathematical-proof
