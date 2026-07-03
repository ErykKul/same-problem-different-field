MECHANISM: The paper computes a convergence criterion for self-consistently defined quantities in bipartite networks. The method iteratively updates two interdependent quantities, denoted as D and C, across two sets of nodes. Each iteration involves aggregating weighted contributions from the opposite set, followed by normalization to maintain scale invariance. The process repeats until convergence is detected, which depends on the structure of the network and the relative sizes of node groups. A critical condition for convergence is derived by analyzing the product of group sizes along diagonal links in a condensed bipartite network. If this product exceeds a threshold determined by the network's topology, the iteration diverges. To address non-convergence, the paper proposes three algorithms: removing nodes with vanishing measures, merging such nodes, or introducing a regularization parameter to stabilize the iteration. The regularization method modifies the update equations by adding a constant term, which adjusts the convergence condition to account for the regularization parameter. The analysis relies on mean-field approximations and algebraic manipulations of the iterative equations to derive the convergence criterion and algorithmic improvements.  
DOMAIN: network analysis, self-consistent measures  
STRUCTURE: other: iterative self-consistent update  
DATA_OBJECT: graph or network  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: proof or characterization  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: public-benchmark-used  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
