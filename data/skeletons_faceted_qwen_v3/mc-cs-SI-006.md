MECHANISM: The paper computes a graph-based community search algorithm that disentangles multi-hop and multi-frequency signals to handle both homophilic and heterophilic graphs. The process begins by extracting exact-k hop neighborhoods through adaptive masking, ensuring each channel contains only information from nodes at a fixed distance. These hop-specific features are then filtered into low-pass (smooth, homophilic) and high-pass (non-smooth, heterophilic) components using a frequency-aware filter. A lightweight two-dimensional channel mixer fuses these hop and frequency channels into compact node embeddings, preserving both local detail and long-range context. To improve scalability, a memory-efficient low-rank optimization computes all hop-specific features in latent space, avoiding explicit high-order adjacency materialization. During online search, a Signed Community Search (SCS) constructs a positive graph from learned embeddings, while an Adaptive Community Score (ACS) dynamically balances embedding-based similarity and topological relations based on the graph’s approximated homophily ratio. The method mitigates the "Flip Effect" by processing multi-hop signals independently and avoids semantic inversion along even-hop paths. The algorithm combines structural cohesiveness with semantic consistency through a low-rank optimization and adaptive scoring, enabling robust community search on heterophilic graphs without relying on explicit edge signs or labels.  
DOMAIN: graph community search  
STRUCTURE: other: graph-based processing  
DATA_OBJECT: graph or network  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: search  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: public-benchmark-used
