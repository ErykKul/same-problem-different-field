MECHANISM: Each federated agent performs Maximum Entropy inverse reinforcement learning (MaxEnt IRL) locally on expert demonstration trajectories to estimate a reward function under linear function approximation. Convert each locally learned reward function to a probability distribution over state-action support via shift-and-normalize. Aggregate reward functions across agents by computing an entropically regularized Wasserstein barycenter over these normalized measures using the Sinkhorn algorithm. Project the fused measure back to parameters via least squares in the shared feature basis to obtain a global reward function.
DOMAIN: Reinforcement learning, multi-agent systems, federated learning
STRUCTURE: other: optimal transport and barycenter computation
DATA_OBJECT: set or table
INFERENCE: optimization only
PROBLEM_FORM: optimization
DISTRIBUTION: none
COMPLEXITY: not stated
