MECHANISM: The paper computes a modified PageRank centrality measure where the restart probability for a random walk on a graph depends on the node's properties. The algorithm defines a Markov chain with transition probabilities determined by the graph's adjacency matrix and a node-specific restart distribution. The stationary distribution of this chain is computed as the solution to a linear system involving the graph's transition matrix and a restart probability matrix. The method generalizes standard PageRank by allowing non-uniform restart probabilities, which are specified as input parameters. The computation involves iteratively updating the probability vector until convergence, using the graph's structure to determine neighbor transitions. The restart distribution is node-dependent, meaning each node has a unique probability of restarting the walk, which is incorporated into the transition matrix. The algorithm's output is a vector of node importances, where higher values indicate greater centrality under the modified restart rules. The method is applied to both directed and undirected graphs, with the restart probabilities adjusted based on the graph's topology. The paper derives the mathematical formulation of the stationary distribution and discusses its properties, including convergence guarantees. The approach is compared to standard PageRank and other variants, emphasizing the flexibility of node-dependent restarts in capturing different notions of importance. The implementation details focus on efficiently solving the linear system using sparse matrix representations and iterative solvers. The method's theoretical properties, such as uniqueness and convergence, are analyzed in the context of Markov chain theory.

DOMAIN: network analysis

STRUCTURE: sparse linear algebra

DATA_OBJECT: graph or network

INFERENCE: deterministic or closed-form

PROBLEM_FORM: estimation

DISTRIBUTION: continuous; continuous

COMPLEXITY: not stated

DATA_AVAILABILITY: none

CODE_AVAILABILITY: none

PREREGISTRATION: none

EVIDENCE_BASIS: mathematical-proof
