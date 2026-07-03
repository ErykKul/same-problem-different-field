MECHANISM: The paper introduces a computational method for estimating latent positions of legislators and bills in a Euclidean metric space using roll-call data. It adapts the Latent Space Item Response Model (LSIRM) to a bipartite network, where legislators and bills are nodes connected by voting records. The model enforces metric distances by ensuring triangle inequality holds, unlike conventional ideal point models that use non-metric Gaussian or quadratic utility functions. Parameters are optimized to minimize discrepancies between observed voting patterns and distances in the embedded Euclidean space. The method jointly estimates latent positions for both legislators and bills, allowing for clustering analysis of legislative behavior. Simulations validate the model's ability to recover latent coalition structures with superior cluster separation compared to existing methods. When applied to the 118th U.S. House data, the model improves vote prediction accuracy and generates bill embeddings that reveal cross-cutting issue alignments. The approach explicitly avoids non-metric distance violations, enhancing geometric interpretability of party cohesion and factional divisions. The algorithm iteratively refines latent positions through optimization, leveraging the bipartite structure of roll-call data to infer multidimensional legislative behavior.  
DOMAIN: political science and network modeling  
STRUCTURE: other: latent space modeling  
DATA_OBJECT: graph or network  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: estimation  
DISTRIBUTION: binary; continuous  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
