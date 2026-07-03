MECHANISM: The paper computes a modified attention mechanism to improve focus allocation in sequence modeling. It begins by computing pairwise similarity scores between queries and keys, then applies positional discrimination across attention heads and dimensions to enhance token differentiation. This involves rotating query and key vectors using frequency-based transformations and adding learnable biases that depend on relative distances between tokens. Next, it computes attention weights using a modified softmax function called Elastic-Softmax, which introduces an offset to suppress attention on irrelevant tokens. The offset is learned per attention head and scales with the number of attended tokens. The mechanism ensures that attention weights remain non-negative while allowing zero weights for irrelevant tokens, reducing spurious focus. The process is applied iteratively across layers, with positional biases and offsets adjusted to maintain context-aware representations. The method avoids explicit normalization constraints that force attention weights to sum to one, instead allowing sparse distributions that emphasize semantically relevant tokens. The algorithm operates on sequences of tokens, transforming them through attention heads with learned parameters, and outputs sparse attention weights that guide subsequent computations. The design integrates both positional encoding strategies and normalization adjustments to address attention overload and underload, achieving sparsity without sacrificing performance.  
DOMAIN: neural attention mechanisms  
STRUCTURE: other: attention mechanism  
DATA_OBJECT: sequence or time-series  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: optimization  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: public-benchmark-used  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
