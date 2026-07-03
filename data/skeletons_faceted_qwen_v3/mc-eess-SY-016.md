MECHANISM: The paper computes a reinforcement learning algorithm that mitigates overestimation in value estimates by incorporating temporal aleatoric uncertainty. The method uses a distributional critic network to model the uncertainty in one-step returns, applying a pessimistic shift based on the variance of the estimated distribution. The critic network outputs a probability distribution over returns, and the Bellman backup operator is modified to include a variance-dependent penalty term. Policy evaluation involves minimizing the Kullback-Leibler divergence between the distributional Bellman backup and the current critic distribution. The actor network is updated using a gradient ascent on the expected value of the state-action return, adjusted by a logarithmic entropy term. Dropout is applied to both the critic and actor networks during training to regularize the model and reduce overfitting. The algorithm iteratively updates the critic and actor networks using off-policy samples, with the critic's distributional output guiding the pessimistic updates. The method avoids ensembling critics by relying on a single distributional critic, reducing computational and memory costs. The algorithm's design ensures that uncertainty from environment stochasticity and policy-induced variability is captured as temporal aleatoric uncertainty, which is directly used to scale pessimistic updates in both critic and actor networks. The training process involves minimizing a cross-entropy loss function derived from the distributional critic's predictions and the pessimistic Bellman targets. The method's theoretical guarantees include bounds on overestimation based on sub-Gaussian assumptions about the critic's distribution.  
DOMAIN: reinforcement learning, uncertainty modeling  
STRUCTURE: dynamic programming  
DATA_OBJECT: continuous function or field  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: estimation  
DISTRIBUTION: continuous; continuous  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
