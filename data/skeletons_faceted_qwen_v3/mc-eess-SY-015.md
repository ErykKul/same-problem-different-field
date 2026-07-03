MECHANISM: The paper computes a hybrid reinforcement learning framework that integrates policy gradient methods with swarm-based exploration. Multiple agents generate actions by combining policy-gradient outputs with particle-swarm optimization (PSO) proposals. Each agent's action is a weighted mix of its own policy's sampled action and a PSO-derived action, with the mixing coefficient determined by a fixed parameter. Novelty is quantified as the minimum distance between an agent's action and other swarm particles' positions, and this is added to the reward signal as an intrinsic bonus. The swarm's PSO parameters (inertia, cognitive, and social coefficients) are adaptively adjusted based on the variance of agent performance metrics. Periodically, the best-performing agent's policy parameters are broadcast to all agents, enabling synchronized exploitation. Policy updates are performed using proximal policy optimization (PPO) on augmented rewards, which include both environmental and novelty-based components. The PPO objective combines policy gradient terms, value function estimation, and entropy regularization. PSO particle positions and velocities are updated using standard velocity and position equations, with parameters modulated by performance variance. The system alternates between exploration (PSO-driven action mixing) and exploitation (broadcasted policy synchronization) in a cyclic training loop. The algorithm maintains independent actor-critic networks per agent, with shared backbone architectures and agent-specific heads. The novelty coefficient and mixing parameter are fixed hyperparameters, while the PSO coefficients are dynamically adjusted during training. The method ensures diversity through biased sampling of high-performing agents and controlled information sharing.
DOMAIN: reinforcement learning
STRUCTURE: other: hybrid gradient and swarm-based
DATA_OBJECT: policy parameters and action space
INFERENCE: deterministic or closed-form
PROBLEM_FORM: optimization
DISTRIBUTION: none
COMPLEXITY: not stated
DATA_AVAILABILITY: none
CODE_AVAILABILITY: none
PREREGISTRATION: none
EVIDENCE_BASIS: empirical-with-released-data
