MECHANISM: The paper computes a reinforcement learning policy that dynamically allocates discrete repetition counts to individual dimensions of a quantized embedding vector to minimize a composite distortion metric. The process begins by mapping a discrete message to a continuous vector representation through a frozen embedder. Each dimension is normalized and quantized to a discrete symbol using a fixed-bit signed integer scheme. The quantized symbols are then transmitted with repetition counts determined by a learned policy, subject to a total budget constraint. At the receiver, majority voting decodes the repeated symbols, followed by dequantization to reconstruct the embedding. A closed-vocabulary retrieval policy selects the best-matching knowledge-base entry based on cosine similarity between the reconstructed and original embeddings. The composite distortion metric combines global embedding alignment (via cosine similarity) with entity-level correctness (via weighted presence of critical entities). The policy is optimized using an actor-critic algorithm with entropy regularization, where the reward is the negative of the distortion metric minus a penalty for exceeding the repetition budget. The optimization balances exploration and exploitation through a Lagrangian relaxation with an entropy bonus. The algorithm uses a straight-through estimator to handle the discrete allocation space, combining deterministic forward passes with differentiable relaxed sampling during gradient computation. The policy is trained under a fixed channel model and quantization level, then evaluated across varying conditions. The method guarantees convergence under standard assumptions about bounded rewards, Lipschitz continuity, and step size conditions.  
DOMAIN: semantic communication and reinforcement learning  
STRUCTURE: map-reduce or embarrassingly-parallel  
DATA_OBJECT: dense matrix or tensor  
INFERENCE: optimization only  
PROBLEM_FORM: optimization  
DISTRIBUTION: continuous and proportion or bounded  
COMPLEXITY: convergence rate  
DATA_AVAILABILITY: dataset-with-DOI-or-handle  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
