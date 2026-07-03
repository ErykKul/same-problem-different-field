MECHANISM: A two-stage framework performs random walks on multiple network types (protein-protein interaction, gene regulatory network, dynamic co-expression) to score mutated entities, then refines scores through hypergraph diffusion that incorporates cross-sample information. Stage 1 uses random walks with restart on patient-specific subnetworks to capture topological importance and expression perturbation. Stage 2 constructs hypergraphs where nodes are mutated entities and hyperedges link co-mutated entities across samples, then applies weighted random walk with restart to refine rankings at both individual and population levels.
DOMAIN: Cancer driver gene identification in precision oncology
STRUCTURE: graph traversal
DATA_OBJECT: graph or network
INFERENCE: deterministic or closed-form
PROBLEM_FORM: ranking or retrieval
DISTRIBUTION: none
COMPLEXITY: not stated
