MECHANISM: The paper computes a ranking of entities based on a graph constructed from pairwise interactions. Each entity is a node, and edges between nodes are weighted using metrics derived from aggregated quantities associated with their interactions. The weight of an edge from node i to node j is determined by a function that combines multiple statistics, such as the number of interactions, outcomes (wins, losses, draws), and scored/conceded quantities. The graph is transformed into a transition probability matrix by normalizing adjacency weights and incorporating a damping factor, which introduces a probability of jumping to a random node. The ranking is derived by solving for the stationary distribution of a Markov chain defined by this matrix, using an iterative method to approximate the dominant eigenvector. The damping factor ensures convergence and adjusts the influence of nodes with limited connectivity. The algorithm iteratively updates node scores until they stabilize, with higher scores indicating greater influence based on both direct and indirect connections. The method emphasizes the strength of opponents defeated, as higher scores are assigned to nodes that have strong connections to other high-scoring nodes. The process is deterministic and does not involve probabilistic inference or uncertainty modeling. The final ranking reflects a balance between direct performance metrics and the relative strength of connected entities.  
DOMAIN: sports ranking  
STRUCTURE: graph traversal  
DATA_OBJECT: graph or network  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: ranking or retrieval  
DISTRIBUTION: none  
COMPLEXITY: polynomial iterative  
DATA_AVAILABILITY: dataset-in-repository  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
