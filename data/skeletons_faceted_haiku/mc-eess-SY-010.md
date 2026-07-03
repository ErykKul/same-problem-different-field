MECHANISM: Decompose the global optimal transport problem (Wasserstein distance minimization) into decentralized per-agent decision processes. Each agent receives target destination points from the global problem and determines its optimal final location using local information. A sequential weight-update rule constructs feasible local transport plans respecting marginal constraints. A memory-based correction mechanism handles intermittent communication by recording and correcting plans when communication is restored. Agents execute trajectories under local dynamics to reach assigned target positions while minimizing cumulative transport cost.
DOMAIN: Multi-agent control and optimal transport
STRUCTURE: other: decomposition of optimal transport with distributed optimization
DATA_OBJECT: point set
INFERENCE: deterministic or closed-form
PROBLEM_FORM: optimization
DISTRIBUTION: none
COMPLEXITY: convergence rate
