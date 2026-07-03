MECHANISM: A family of j-neighborhood centrality measures is defined based on the Laplacian matrix of a graph. For each node and distance j, a characteristic function identifies all nodes at exactly distance j. The j-neighborhood centrality computes the ratio of outgoing edges from this set to the cardinality of the set. The definition generalizes degree (j=0) and ksi-centrality (j=1). An algorithm iteratively computes characteristic matrices and Laplacian bilinear forms for each distance j. Distributions of these centralities are then compared across real networks and synthetic models using Weibull fitting and Pearson skewness measurement to classify networks as real or artificial.
DOMAIN: Network science and graph centrality measures
STRUCTURE: sparse linear algebra
DATA_OBJECT: graph or network
INFERENCE: deterministic or closed-form
PROBLEM_FORM: ranking or retrieval
DISTRIBUTION: none
COMPLEXITY: polynomial iterative
