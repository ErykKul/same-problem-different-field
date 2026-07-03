MECHANISM: A parametric multi-layer nonlinear map is fitted to transform each input array into a fixed-length output vector. The map is a cascade of local linear filterings interleaved with pointwise nonlinear rectification, downsampling, and normalization steps. For each category, a fixed target vector is assigned from the mutually orthogonal rows of a structured sign/binary matrix whose pairwise Hamming separation is maximal, so the targets sit as far apart as possible in the output space. Training adjusts only the filtering parameters by iteratively reducing the squared deviation between the produced output vector and the assigned target vector over labeled examples, using gradient-based updates. The downstream assignment stage is parameter-free: a new input is labeled by the target vector to which its output vector is nearest in squared Euclidean distance. A separability functional, the trace of the product of the inverse pooled within-group scatter matrix with the between-group scatter matrix, quantifies how compact and well-separated the groups are; the fixed orthogonal targets are chosen specifically to drive this ratio high. The depth of the cascade is grown incrementally until in-sample fitting exceeds a threshold. Performance is averaged over repeated random splits into fitting and held-out subsets.
DOMAIN: machine learning, signal and image classification
STRUCTURE: neural network
DATA_OBJECT: dense matrix or tensor
INFERENCE: deterministic optimization
PROBLEM_FORM: prediction or classification
DISTRIBUTION: continuous; none
COMPLEXITY: polynomial iterative
