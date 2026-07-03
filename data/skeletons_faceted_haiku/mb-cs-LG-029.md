MECHANISM: Generative flow networks sample from combinatorial spaces by learning forward and backward policies on directed acyclic graphs. The method establishes a connection between flow balance conditions and policy evaluation functions through a balance-based objective. For each state in the graph, a forward policy generates trajectories incrementally; a backward policy guides trajectory distribution matching. A unified evaluation function approximates the KL divergence between forward subtrajectory distributions and target backward distributions. The evaluation function is learned by optimizing a subtrajectory evaluation balance objective that compares flow-balance conditions at different trajectory lengths. The approach enables joint optimization of forward policy, evaluation function, and optionally a parameterized backward policy. The learned model generates objects with probabilities proportional to a reward function, enabling both online and offline training variants.
DOMAIN: Generative modeling on combinatorial spaces via flow networks
STRUCTURE: dynamic programming
DATA_OBJECT: graph or network
INFERENCE: optimization only
PROBLEM_FORM: simulation or generation
DISTRIBUTION: none
COMPLEXITY: convergence rate
