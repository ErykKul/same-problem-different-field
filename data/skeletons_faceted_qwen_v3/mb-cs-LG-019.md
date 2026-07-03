MECHANISM: The paper computes a hybrid algorithm selection framework that integrates supervised learning and reinforcement learning (PPO) to recommend optimal DSE algorithms. The process begins by encoding benchmark features into a graph representation using a pre-trained graph neural network (GNN). This graph is then processed by a supervised model with an MLP head, which outputs algorithm recommendation probabilities via softmax. These probabilities initialize the state of a PPO agent, which interacts with an environment to refine recommendations. The agent's policy is updated using generalized advantage estimation (GAE) and clipped policy gradients, balancing exploration and exploitation. The environment provides rewards based on the deviation of an algorithm's ADRS metric from the best-performing algorithm's ADRS. The final recommendation combines the supervised model's initial probabilities with the PPO agent's optimized policy. The framework iteratively refines algorithm selection through feedback loops, leveraging both deterministic supervised predictions and stochastic reinforcement learning updates to maximize recommendation accuracy under limited data conditions.  
DOMAIN: electronic design automation  
STRUCTURE: other: hybrid supervised-reinforcement learning  
DATA_OBJECT: graph or network  
INFERENCE: sampling or Monte-Carlo  
PROBLEM_FORM: optimization  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: public-repository  
CODE_AVAILABILITY: public-repository  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
