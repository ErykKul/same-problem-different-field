MECHANISM: The paper computes a probabilistic embedding of two node types (entities) into a shared Euclidean metric space, where pairwise distances between nodes determine voting behavior. The method begins by initializing latent positions for each entity in a K-dimensional space. For each pair of entities (one from each node type), the Euclidean distance between their latent positions is calculated. This distance is then used in a monotonic link function to model the probability of a binary outcome (e.g., "Yea" or "Nay" vote). The model incorporates baseline parameters for each entity to account for non-spatial influences on the outcome. The full likelihood is maximized via iterative optimization, adjusting latent positions and parameters to better align observed outcomes with predicted probabilities. The algorithm ensures metric consistency by enforcing Euclidean distance properties (triangle inequality, symmetry). The embedding process is repeated until convergence, producing latent positions that reflect both spatial proximity and baseline tendencies. The method enables clustering of entities based on their latent positions, with cluster quality assessed using silhouette coefficients. The model is applied to a bipartite network, where one node type represents entities (e.g., legislators) and the other represents items (e.g., bills), with edges indicating observed outcomes. The latent positions of items serve as interpretive anchors for the dimensions of the embedding space. The approach is validated through simulations and empirical analysis on legislative data, demonstrating improved cluster separation and predictive accuracy compared to non-metric alternatives.  
DOMAIN: political methodology  
STRUCTURE: graphical models  
DATA_OBJECT: graph or network  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: estimation  
DISTRIBUTION: binary; logistic  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-private-data
