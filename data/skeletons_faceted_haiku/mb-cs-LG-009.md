MECHANISM: A dual-learner framework maintains a fast learner and meta learner for sequential task learning in reinforcement learning. The fast learner rapidly adapts to new tasks using initialization or regularization from the meta learner. The meta learner consolidates knowledge by minimizing catastrophic forgetting, defined quantitatively through MDP distance and policy/Q-function divergence measures. Knowledge integration is achieved through incremental softmax meta learner updates that perform maximum likelihood estimation over a mixture of state-action distributions. An adaptive meta warm-up mechanism selects initialization strategy based on hypothesis testing of policy performance. The framework operates in both value-based (discrete actions) and policy-based (continuous actions) RL settings.

DOMAIN: reinforcement learning, continual learning, multi-task learning

STRUCTURE: dynamic programming

DATA_OBJECT: set or table

INFERENCE: optimization only

PROBLEM_FORM: control

DISTRIBUTION: not stated

COMPLEXITY: polynomial iterative
