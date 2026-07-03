MECHANISM: Address overestimation in off-policy actor-critic learning by modeling temporal aleatoric uncertainty directly. Train a single distributional critic network to output a probability distribution over state-action values conditioned on the input, capturing one-step return uncertainty from stochastic transitions, rewards, and policy-induced variability. Apply dropout regularization to both critic and actor networks. Use the critic's mean and variance estimates to compute a pessimistic temporal-difference target by subtracting a variance-scaled term. Update the critic to minimize KL divergence between the target and predicted distribution. Update the actor via maximum entropy policy improvement using pessimistic value estimates.
DOMAIN: Reinforcement learning and value estimation
STRUCTURE: other: distributional learning with uncertainty
DATA_OBJECT: continuous function or field
INFERENCE: Bayesian posterior
PROBLEM_FORM: optimization
DISTRIBUTION: continuous; distributional assumption sub-Gaussian
COMPLEXITY: convergence rate
