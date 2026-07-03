MECHANISM: The paper computes a decentralized control strategy to align a set of entities' terminal positions with a target distribution using optimal transport principles. The process begins by defining a discrete Wasserstein distance between the current empirical distribution of entities and a target distribution represented as weighted sample points. This distance is reformulated as a per-entity optimization problem, where each entity independently determines its target locations by greedily allocating its mass to the nearest available sample points, subject to capacity constraints. A sequential update rule adjusts the residual capacities of sample points after each entity's allocation, ensuring capacity-disjoint assignments. Subsequently, each entity computes control inputs over a fixed horizon to minimize the local Wasserstein distance associated with its assigned sample points, using either linear or nonlinear dynamics. The control inputs are derived by solving a constrained minimum-norm problem, leveraging the system's reachability matrix to express the terminal state as a function of control actions. A memory-based correction mechanism is incorporated to handle intermittent communication, and convergence guarantees are established by showing cycle-wise reduction in a surrogate transport cost under both linear and nonlinear dynamics. The method avoids global coordination by decomposing the problem into local decisions and parallel execution phases, ensuring scalability and robustness under communication limitations.

DOMAIN: multi-agent control

STRUCTURE: other: decentralized optimization

DATA_OBJECT: point set

INFERENCE: deterministic or closed-form

PROBLEM_FORM: optimization

DISTRIBUTION: none

COMPLEXITY: not stated

DATA_AVAILABILITY: none

CODE_AVAILABILITY: none

PREREGISTRATION: none

EVIDENCE_BASIS: simulation-study
