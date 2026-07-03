MECHANISM: The paper computes a method to generate counterfactual explanations for multivariate time-series data by integrating genetic algorithms with causal inference. The process begins by modeling each input variable with an auto-regressive model to forecast future values. Quantile regression is then used to estimate the distribution of each variable, capturing uncertainty through quantile-based predictions. Granger causality tests are applied to identify statistically significant causal relationships between variables, reducing the Rashomon space of feasible forecasts. A genetic algorithm is employed to search for interventions that produce future scenarios satisfying a target outcome within a specified error margin. The algorithm evolves a population of candidate solutions, each represented as a vector of quantiles for each variable at each time step. The fitness function combines three objectives: minimizing the distance between predicted and desired outcomes, maximizing similarity to the original data, and maximizing the likelihood of the counterfactual scenario under the observed data distribution. The method iteratively refines these solutions through selection, crossover, and mutation operations, ensuring plausibility and alignment with historical patterns. The final output is a set of interventions that approximate the desired counterfactual outcome while maintaining consistency with the observed data's temporal dynamics and causal structure.  
DOMAIN: multivariate time-series analysis  
STRUCTURE: genetic algorithm  
DATA_OBJECT: multivariate time-series  
INFERENCE: frequentist point estimate  
PROBLEM_FORM: optimization  
DISTRIBUTION: continuous; quantile-based  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-private-data
