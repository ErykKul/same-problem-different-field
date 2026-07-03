MECHANISM: The paper computes a differentiable refinement process to convert a partially oriented graph into a fully directed acyclic graph (DAG). It begins by expanding discrete variables into state-level representations using one-hot encoding, enabling fine-grained modeling of interactions between individual states. Structural constraints derived from the input graph's skeleton and v-structures define a feasible adjacency space, while soft priors introduce asymmetry to avoid symmetric saddle points. A unified differentiable objective is formulated, jointly optimizing data reconstruction likelihood and structural regularization. The objective includes a cross-entropy loss for reconstructing observed states, a block-wise sparsity penalty to suppress weak connections, a cycle penalty to discourage bidirectional activation, and a skeleton-preservation term to maintain adjacencies from the input graph. The final DAG is obtained by aggregating optimized adjacency matrices and enforcing acyclicity through post-hoc checks. Directional preferences emerge implicitly from the shared reconstruction objective, with structural regularizers ensuring sparsity and asymmetry. Unresolved edges are resolved by thresholding state-level block strengths, and symmetry-breaking priors are applied at initialization to escape balanced equilibria. The method combines gradient-based optimization with explicit constraints to achieve a DAG consistent with the input graph's equivalence class.  
DOMAIN: causal discovery  
STRUCTURE: other: differentiable optimization with structural constraints  
DATA_OBJECT: graph or network  
INFERENCE: optimization only  
PROBLEM_FORM: estimation  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: public-benchmark-used  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
