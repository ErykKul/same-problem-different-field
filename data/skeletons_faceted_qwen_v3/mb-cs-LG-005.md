MECHANISM: The paper computes a method for generating discrete sequences through iterative refinement guided by variational objectives. It reformulates KL divergence minimization to operate on conditional endpoint distributions along a flow path, avoiding intractable marginal likelihoods. The process involves defining a time-dependent probability path that interpolates between a source and target distribution, using a conditional probability path for each training pair. A continuous-time Markov chain with time-dependent rate matrices evolves samples along this path, with velocity fields derived from posterior distributions. The posterior is approximated by a parameterized neural network trained to minimize cross-entropy between predicted and true targets. Importance sampling with self-normalized weights is used to estimate expectations over conditional distributions, enabling gradient-based optimization of the flow model. The method balances exploration and exploitation by adjusting the scheduler and incorporating a mixture proposal for sampling. Theoretical guarantees ensure that minimizing the forward-KL objective recovers the target distribution under standard assumptions. The algorithm iteratively updates sequences using parallel, categorical transitions based on velocity fields, maintaining diversity while concentrating probability on high-fitness regions.  
DOMAIN: generative modeling and optimization  
STRUCTURE: dynamic programming  
DATA_OBJECT: sequence or time-series  
INFERENCE: variational  
PROBLEM_FORM: optimization  
DISTRIBUTION: none  
COMPLEXITY: polynomial iterative  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-private-data
