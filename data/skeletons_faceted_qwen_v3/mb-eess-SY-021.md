MECHANISM: The paper computes a data-driven safety certification framework for discrete-time stochastic systems with unknown disturbance distributions. It constructs barrier functions that ensure finite-time safety guarantees with probabilistic confidence. The process begins by collecting a finite set of independent and identically distributed (i.i.d.) disturbance samples. These samples are used to derive constraints for an optimization problem that searches for a barrier function satisfying specific inequalities. The barrier function must be non-positive outside the safe set and contractively evolve within the safe set under system dynamics. The optimization problem is reformulated using scenario-based constraints derived from the sampled disturbances, replacing universal constraints over all possible disturbances. To ensure generalization from finite samples, the paper applies tools from statistical learning theory, including VC dimension, scenario optimization, and Rademacher complexity. These tools provide PAC-style generalization bounds that quantify the trade-offs between sample size, model complexity, and safety tolerance. The method guarantees that, with high confidence over the sampled disturbances, the computed barrier function ensures the system remains within the safe set over a finite horizon. The derived bounds explicitly relate the number of disturbance samples to the complexity of the barrier functions and the desired safety and confidence thresholds. The framework is demonstrated using semidefinite programming to synthesize barrier functions directly, avoiding transformations into chance-constrained optimization problems. The approach is applicable to general nonlinear dynamics without requiring prior knowledge of disturbance distributions or structural assumptions on system dynamics.  
DOMAIN: stochastic systems safety verification  
STRUCTURE: scenario optimization  
DATA_OBJECT: set or table  
INFERENCE: sampling or Monte-Carlo  
PROBLEM_FORM: safety  
DISTRIBUTION: continuous; continuous  
COMPLEXITY: finite-sample bound  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: mathematical-proof
