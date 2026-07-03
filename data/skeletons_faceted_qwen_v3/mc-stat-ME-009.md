MECHANISM: The paper computes a policy optimization under fairness and cost constraints in a bipartite network interference setting. It begins by defining an exposure mapping that linearly combines treatment assignments at intervention units with weights determined by a bipartite adjacency matrix. Potential outcomes are modeled as a linear function of exposure levels and covariates, with additive treatment effects. A welfare function quantifies subgroup-specific benefits of interventions, defined as the expected difference in potential outcomes when treating an intervention unit, weighted by the policy's probability of treatment. The method then formulates an optimization problem to maximize welfare while ensuring Pareto efficiency and fairness constraints. This involves estimating model parameters via regression on observed outcomes, constructing a welfare function that aggregates subgroup impacts, and solving a constrained optimization to find policies on the Pareto frontier. The solution balances trade-offs between cost, fairness, and health outcomes using Monte Carlo simulations to validate finite-sample performance. The algorithm iteratively refines policy parameters to minimize regret bounds, ensuring that no subgroup is harmed while maximizing overall welfare under budget limits. The method explicitly accounts for interference by incorporating the bipartite adjacency matrix into exposure calculations and uses asymptotic properties to derive theoretical guarantees for the optimization's convergence and regret rates.  
DOMAIN: causal inference and policy optimization  
STRUCTURE: other: constrained optimization  
DATA_OBJECT: dense matrix or tensor  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: optimization  
DISTRIBUTION: continuous; continuous  
COMPLEXITY: regret bound  
DATA_AVAILABILITY: dataset-with-DOI-or-handle  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
