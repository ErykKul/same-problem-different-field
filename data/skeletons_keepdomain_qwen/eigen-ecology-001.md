MECHANISM: The paper introduces environ centrality, a method to quantify species importance in ecosystem networks by integrating direct, indirect, and boundary effects. The method constructs a directed graph where nodes represent species and edges represent energy–matter exchange interactions. Environ centrality is computed by aggregating the influence of each species across all paths in the network, weighted by the magnitude of their contributions to energy–matter flow. This involves calculating the sum of all indirect pathways originating from a species, normalized by the total network activity. The algorithm contrasts with traditional centrality metrics like degree or betweenness by explicitly accounting for indirect effects and boundary conditions (e.g., detritus recycling). The method is applied to 50 empirically-based ecosystem network models, where centrality distributions are compared to test two hypotheses: (1) that species importance follows a dominance–diversity curve, and (2) that indirect effects homogenize functional importance. The computation involves matrix operations on adjacency matrices representing the networks, with centrality scores derived from eigenvector-like decompositions. The results are validated by comparing the distribution of environ centrality values against observed ecological patterns, such as the prominence of detritus recyclers. The method is deterministic, relying on algebraic operations rather than probabilistic inference, and does not require sampling or optimization.  
DOMAIN: ecological network analysis  
STRUCTURE: other: network centrality computation  
DATA_OBJECT: graph or network  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: estimation  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-private-data
