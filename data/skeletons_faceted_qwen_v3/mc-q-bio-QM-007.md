MECHANISM: The paper computes a two-stage algorithm to identify driver entities by integrating topological and expression-based signals. In the first stage, for each entity, a subnetwork is constructed from static and dynamic data sources. Static subnetworks are derived from precomputed interactions (e.g., protein-protein or regulatory relationships), while dynamic subnetworks are inferred from expression differences between tumor and normal states. A random walk with restart is performed independently on each subnetwork to compute a steady-state distribution reflecting the entity's prominence within the network and its association with expression perturbations. These distributions are aggregated into an initial score for each entity. In the second stage, cross-sample information is integrated via a hypergraph structure, where nodes represent entities and hyperedges link entities across samples. Node weights are initialized using first-stage scores, and a hypergraph-based random walk with restart is applied to refine scores by propagating information across samples. This process prioritizes entities with high connectivity in both individual and aggregated contexts. The algorithm combines network diffusion on static structures, perturbation-aware diffusion on dynamic data, and hypergraph-based aggregation to produce final rankings. No explicit probabilistic modeling is used; instead, scores are derived from diffusion dynamics. The method is unsupervised, relying solely on network topology and expression data without requiring labeled examples.  
DOMAIN: cancer genomics and network biology  
STRUCTURE: graph traversal  
DATA_OBJECT: graph or network  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: estimation  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: dataset-with-DOI-or-handle  
CODE_AVAILABILITY: public-repository  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
