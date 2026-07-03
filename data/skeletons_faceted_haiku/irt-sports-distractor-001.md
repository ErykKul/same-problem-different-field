MECHANISM: Construct a directed graph where nodes are entities (teams) and edges represent pairwise interactions (matches). Assign edge weights based on quantitative metrics from the interactions (win ratio, goal differential, game count). Compute the dominant eigenvector of the row-normalized weighted adjacency matrix via power iteration with a damping factor, where the damping parameter ensures convergence by allowing random jumps to any node. The resulting steady-state vector (stationary distribution) assigns a scalar score to each node representing its centrality in the weighted graph structure.
DOMAIN: Sports team ranking and network-based rating systems.
STRUCTURE: spectral or transform
DATA_OBJECT: graph or network
INFERENCE: deterministic or closed-form
PROBLEM_FORM: ranking or retrieval
DISTRIBUTION: none
COMPLEXITY: polynomial iterative
