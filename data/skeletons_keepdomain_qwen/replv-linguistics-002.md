MECHANISM: The paper computes the dynamics of linguistic convergence and divergence using a multi-population extension of the replicator–mutator equation, which models how individuals adjust their language use based on ingroup and outgroup interactions. The system is represented as a set of differential equations describing population state variables over time, with mutation rates parameterizing the deviation from pure replicator dynamics. Linearization techniques are applied to analyze the stability of equilibria in the symmetric two-population case, identifying conditions under which equilibria are stable or unstable. The model is then calibrated to an empirical dataset from adolescent sociolinguistic behavior, comparing observed population states to predicted equilibria under varying mutation rate parameters. For the asymmetric three-population extension, numerical solution methods (e.g., Euler or Runge-Kutta integration) are used to simulate trajectories and determine convergence to specific equilibria. The analysis involves solving for fixed points of the system, evaluating Jacobian matrices at those points, and interpreting eigenvalues to classify stability. The paper does not implement sampling or probabilistic inference but relies on deterministic simulation of the differential equations. The computational steps include parameter estimation from empirical data, numerical integration of the equations, and comparison of simulated outcomes to observed linguistic patterns. The model assumes continuous, differentiable dynamics without explicit stochastic components. The primary output is a mapping between parameter values and the stability of equilibria, with implications for sociolinguistic identity maintenance.  
DOMAIN: evolutionary game theory and dynamical systems  
STRUCTURE: other: differential equations  
DATA_OBJECT: continuous function or field  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: simulation or generation  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-private-data
