MECHANISM: Quantize a high-dimensional vector embedding to discrete symbols using uniform scalar quantization. Allocate integer repetition counts to each dimension adaptively to protect against channel noise, subject to a fixed total redundancy budget. Train a policy via reinforcement learning (actor-critic) to assign repetitions based on semantic importance, minimizing a composite distortion metric balancing global embedding similarity and entity-level correctness. Use majority voting to decode repeated symbols and retrieve the nearest neighbor from a fixed knowledge base.
DOMAIN: Semantic communication with reinforcement learning and channel coding
STRUCTURE: other: adaptive resource allocation
DATA_OBJECT: dense matrix or tensor
INFERENCE: optimization only
PROBLEM_FORM: optimization
DISTRIBUTION: continuous; none
COMPLEXITY: convergence rate
