MECHANISM: The paper describes a computational framework for processing sequences of tokens through two distinct operations: intra-token and inter-token processing. Intra-token processing transforms individual tokens by combining information across channels within each token, using transformations that depend only on the input token's features. This is exemplified by linear layers or feedforward networks, where each output channel is computed independently from the input token's features. Inter-token processing, in contrast, mixes information between different tokens in a sequence, operating on each channel independently. This is achieved through functions that aggregate information across all tokens, such as self-attention mechanisms in transformers or state-space dynamic updates. The framework leverages sparse activations, discrete-time event-driven processing, and recurrence to model temporal dependencies. For intra-token processing, a virtual time axis is used to simulate spiking dynamics, allowing for energy-efficient computation by reducing the number of active steps. For inter-token processing, the discrete time index corresponds to real-time or positional information, enabling context-aware aggregation of token features. The model incorporates reset mechanisms that adjust internal states based on outputs, creating nonlinear feedback loops. Training methodologies include surrogate gradients for backpropagation through spiking networks and local learning rules inspired by biological processes. The overall approach emphasizes sparsity, recurrence, and dynamic state management to achieve efficient computation.  
DOMAIN: neuromorphic computing  
STRUCTURE: other: recurrent state dynamics  
DATA_OBJECT: dense matrix or tensor  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: prediction or classification  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: review-or-position
