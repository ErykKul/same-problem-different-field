MECHANISM: Combine policy-gradient reinforcement learning with swarm-based exploration in action space. Run M parallel actor-critic agents, each maintaining independent policy and value-function parameters. At each step, generate two action proposals per agent: standard RL policy sample and particle swarm optimization action derived from particle position and velocity. Mix the two proposals with coefficient alpha to produce final action. Augment rewards with a novelty bonus based on minimum Euclidean distance from agent's action to other particles' positions. Periodically broadcast the best-performing agent's policy weights to all agents with controlled mixing to enable information sharing. Update each agent via standard on-policy PPO using only its own trajectory buffer.
DOMAIN: Reinforcement learning and exploration
STRUCTURE: other: policy gradient with swarm coordination
DATA_OBJECT: continuous function or field
INFERENCE: deterministic or closed-form
PROBLEM_FORM: optimization
DISTRIBUTION: none
COMPLEXITY: not stated
