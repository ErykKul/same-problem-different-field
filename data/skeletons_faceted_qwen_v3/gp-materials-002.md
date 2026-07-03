MECHANISM: The paper computes a hierarchical Bayesian optimization framework using deep Gaussian processes (DGPs) to model complex, multi-output relationships. The method constructs a stack of Gaussian process layers, where each layer transforms input features into latent representations, enabling the model to capture nonstationary and hierarchical patterns. The DGP integrates uncertainty across layers through probabilistic inference, with each layer's output serving as input to the next. A cost-aware acquisition function extends the q-Expected Hypervolume Improvement (q-EHVI) criterion by incorporating evaluation costs, balancing exploration of high-uncertainty regions and exploitation of high-mean predictions. The framework alternates between single-objective heterotopic queries (using Upper Confidence Bound) and multi-objective batch selections (using q-EHVI), dynamically adjusting the number of candidates based on cost-weighted utility. The DGP's predictive distribution is approximated via variational inference, optimizing a doubly stochastic evidence lower bound (ELBO) over inducing points. The method operates on a set of observations with multiple correlated outputs, leveraging property-property correlations to improve predictions even when data are incomplete or heterotopic. The optimization goal is to maximize hypervolume improvement in the Pareto front, with the convexity ratio of the front used as a diagnostic metric for geometric complexity. The algorithm iteratively refines candidate solutions by evaluating batches of points, with uncertainty quantification guiding the selection of next experiments.  
DOMAIN: materials design  
STRUCTURE: other: hierarchical Gaussian process  
DATA_OBJECT: set or table  
INFERENCE: Bayesian posterior  
PROBLEM_FORM: optimization  
DISTRIBUTION: continuous; Gaussian  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-private-data
