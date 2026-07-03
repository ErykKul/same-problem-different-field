MECHANISM: A set of entities and their pairwise interaction outcomes are encoded as a weighted directed graph, where each entity is a node and a directed edge weight is a function of summary statistics of the recorded contests between the two entities. The weighted adjacency matrix is row-normalized into a stochastic transition matrix, and a uniform restart term scaled by a damping parameter is mixed in so that the resulting matrix is irreducible and aperiodic, guaranteeing a unique stationary distribution. The stationary distribution is the dominant left eigenvector of this transition matrix, which is computed by repeatedly multiplying a probability vector by the matrix until convergence. The stationary probabilities are interpreted as importance scores and used to order the entities. Several alternative edge-weighting functions built from the same summary counts are evaluated, and the induced orderings are scored against a reference ordering using a normalized count of pairwise inversions over the top-ranked entities. The dependence of this discrepancy on the damping parameter is examined to select its value.
DOMAIN: sports analytics, ranking national teams
STRUCTURE: graph traversal
DATA_OBJECT: graph or network
INFERENCE: deterministic or closed-form
PROBLEM_FORM: ranking or retrieval
DISTRIBUTION: none; none
COMPLEXITY: polynomial iterative
