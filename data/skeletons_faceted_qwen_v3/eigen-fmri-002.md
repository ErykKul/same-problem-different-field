MECHANISM: The paper computes a centrality measure for nodes in a graph by solving an eigenvalue problem on a symmetric similarity matrix. Each node's centrality is determined by its connections to other nodes, with higher centrality assigned to nodes connected to many other highly central nodes. The similarity matrix is constructed from pairwise measures between entities, which can be linear correlations or spectral coherence values. The matrix is normalized to ensure non-negative entries, and the principal eigenvector corresponding to the largest eigenvalue is computed using iterative methods like power iteration. This eigenvector provides a centrality score for each node, reflecting its influence within the network. The method avoids thresholding similarity values, allowing analysis of large node sets. The computation is deterministic and does not involve probabilistic inference. The similarity matrix is derived from time-series data, with entries representing pairwise relationships between entities. The final centrality map is used to identify regions of high influence in the network, enabling comparisons across different states or conditions.  
DOMAIN: neuroimaging and network analysis  
STRUCTURE: spectral or transform  
DATA_OBJECT: dense matrix  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: estimation  
DISTRIBUTION: none  
COMPLEXITY: polynomial iterative  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-private-data
