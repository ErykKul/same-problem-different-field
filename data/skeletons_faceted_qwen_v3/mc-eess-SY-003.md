MECHANISM: The paper computes a multi-timescale trajectory optimization framework for autonomous entities operating in constrained environments. It integrates semantic feature extraction from environmental data with real-time signal quality feedback to guide decision-making. A centralized critic model evaluates long-term rewards based on collision avoidance, quality-of-service constraints, and mission-specific objectives. Decentralized actors compute localized trajectory adjustments using reinforcement learning, where each entity's action vector optimizes a joint reward function incorporating spatial safety margins, target proximity, and energy efficiency. Semantic features are extracted via hierarchical convolutional networks and fused with low-level signal metrics through confidence-gated fusion. The system employs a dual-timescale control loop: short-term adjustments via near-real-time signal feedback and long-term policy updates derived from historical data and semantic maps. Trajectory planning is formulated as a constrained Markov decision process, solved using a multi-agent deep deterministic policy gradient algorithm with centralized training and decentralized execution. The framework dynamically balances exploration and exploitation through reward shaping that penalizes unnecessary altitude changes and mission-area violations. Environmental uncertainty is modeled through confidence metrics on semantic features, with fallback to purely signal-based guidance when confidence thresholds are breached. The optimization process iteratively refines policies through experience replay and policy gradient updates, ensuring convergence to collision-free, QoS-compliant paths.
DOMAIN: low-altitude economy, O-RAN, AI orchestration
STRUCTURE: graphical models
DATA_OBJECT: dense matrix or tensor
INFERENCE: optimization only
PROBLEM_FORM: optimization
DISTRIBUTION: none
COMPLEXITY: not stated
DATA_AVAILABILITY: public-benchmark-used
CODE_AVAILABILITY: none
PREREGISTRATION: none
EVIDENCE_BASIS: empirical-with-released-data
