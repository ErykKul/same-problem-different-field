MECHANISM: Represent loss sequences satisfying weakly-hard (WH) constraints (which bound the number of control input failures within a time window) as paths in a directed graph. Construct a graph where nodes encode loss history and edges are labeled with loss patterns. Define graph-based barrier functions (GBFs): a collection of barrier functions (one per graph node) that satisfy algebraic conditions based on edge relationships. These conditions ensure that if a state satisfies the barrier at one node, it remains safe after transitioning according to system dynamics and edge constraints. For verification: check existence of GBFs satisfying the conditions; for synthesis: optimize over controller parameters subject to GBF conditions.
DOMAIN: Control theory, networked systems, real-time systems
STRUCTURE: dynamic programming
DATA_OBJECT: graph or network
INFERENCE: deterministic or closed-form
PROBLEM_FORM: control
DISTRIBUTION: none
COMPLEXITY: not stated
