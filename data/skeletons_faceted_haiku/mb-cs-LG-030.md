MECHANISM: Causal discovery refines partially oriented causal graphs by resolving ambiguous edge directions through differentiable optimization. Discrete variables are expanded to state-level representations using one-hot encoding, creating a block-structured weight matrix where blocks parameterize state-to-state causal influences. Hard structural constraints derived from the input partial ancestral graph define the feasible parameter space, ensuring consistency with the equivalence class. A unified objective optimizes jointly: reconstruction loss quantifies directional preference through data likelihood, sparsity regularization suppresses weak connections, a cycle penalty discourages bidirectional activations, and a skeleton-preservation term prevents unintended edge removal. Asymmetry is introduced via soft priors (random or LLM-based initialization) to escape symmetric critical points. The optimized adjacency matrix is extracted via block-max thresholding and post-hoc cycle elimination if needed, yielding a fully oriented directed acyclic graph.
DOMAIN: Causal structure learning and refinement
STRUCTURE: other: differentiable graph refinement with block-structured optimization
DATA_OBJECT: graph or network
INFERENCE: deterministic or closed-form
PROBLEM_FORM: decision or test
DISTRIBUTION: none
COMPLEXITY: polynomial iterative
