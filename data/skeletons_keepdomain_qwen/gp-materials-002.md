MECHANISM: The paper computes a cost-aware batch Bayesian optimization framework using deep Gaussian process (DGP) surrogates. The DGP is constructed by stacking multiple Gaussian process layers, where each layer models hierarchical relationships between high-dimensional compositional features and multiple target properties. Uncertainty is propagated through successive layers by combining predictive distributions from each GP layer. An upper-confidence-bound acquisition function is extended to incorporate evaluation costs, balancing exploration of under-characterized regions with exploitation of high-mean, low-variance predictions across correlated properties. Heterotopic querying selects small batches of candidates in parallel, leveraging correlations between properties to prioritize cost-effective evaluations. The framework iteratively updates the DGP surrogate with new data, refining predictions and reducing uncertainty in subsequent iterations. The optimization process terminates when the DGP converges to optimal formulations with minimal evaluation cost. The method is applied to refractory high-entropy alloys for high-temperature applications, demonstrating improved convergence compared to conventional Gaussian process-based Bayesian optimization. The computational steps involve probabilistic modeling of hierarchical relationships, cost-integrated acquisition function design, and parallel candidate selection based on uncertainty and cost trade-offs.  
DOMAIN: materials design for high-temperature applications  
STRUCTURE: graphical models  
DATA_OBJECT: set or table  
INFERENCE: Bayesian posterior  
PROBLEM_FORM: optimization  
DISTRIBUTION: continuous; Gaussian  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-private-data
