MECHANISM: Classify a benchmark (hardware design) into an algorithm category using features extracted from its code graph. First, encode a benchmark feature graph using a pre-trained GNN encoder to obtain a vector representation. Pass this through an MLP head with softmax to predict per-algorithm probabilities. Refine predictions using a PPO reinforcement learning agent initialized with the supervised probabilities, which learns to select the algorithm that minimizes a performance metric.
DOMAIN: Hardware design automation, algorithm selection, design space exploration, multi-objective optimization
STRUCTURE: graph traversal
DATA_OBJECT: graph or network
INFERENCE: frequentist point estimate
PROBLEM_FORM: classification
DISTRIBUTION: none
COMPLEXITY: polynomial iterative
