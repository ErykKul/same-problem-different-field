MECHANISM: The paper computes a sequential selection algorithm to maximize the cumulative influence spread in a network under full-bandit feedback. The algorithm maintains a priority queue of candidate nodes, each associated with marginal gain values relative to the current selected set. At each iteration, the node with the highest marginal gain is selected, leveraging submodularity to avoid redundant computations. If a node was not the best in the previous iteration, its marginal gain is not recomputed, as submodularity ensures it cannot exceed its previous value. If a node was the best previously, its marginal gain is recalculated with respect to the updated set. The algorithm alternates between exploration phases, where each selected node is repeatedly evaluated to estimate influence probabilities, and exploitation phases, where the best nodes are committed to. The exploration phase duration is determined by a parameter minimizing regret, while the exploitation phase uses the stored optimal nodes. The method ensures submodularity and monotonicity of the influence function, which guarantees a $(1-1/e)$ approximation ratio. The algorithm's complexity is linear in the number of nodes for storage and logarithmic per-round for updates. The process iterates over time steps, adapting to unknown edge probabilities through bandit feedback without prior network knowledge.  
DOMAIN: social network analysis  
STRUCTURE: other: greedy algorithm with priority queue  
DATA_OBJECT: graph or network  
INFERENCE: optimization only  
PROBLEM_FORM: optimization  
DISTRIBUTION: none  
COMPLEXITY: regret bound  
DATA_AVAILABILITY: public-benchmark-used  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
