MECHANISM: The paper computes a dual-stage process for virtual cell modeling under semantic and distribution shifts. First, it maps heterogeneous metadata schemas into a canonical interface using a frozen large language model (LLM) to infer a JSON mapping specification, resolving schema inconsistencies through dynamic logic expressions. Second, it employs an adaptive Monte Carlo Tree Search (MCTS) engine operating over a hierarchical action space to synthesize model architectures with optimal statistical inductive biases. The MCTS process iterates through four phases: (1) selection via optimistic UCT to prioritize high-potential branches, balancing maximum and average rewards; (2) expansion by instantiating code templates biased toward refining retrieved structures or exploring new strategies; (3) high-fidelity simulation evaluating multi-objective rewards combining validation performance (DeltaPCC) and computational efficiency (execution time); and (4) backpropagation updating statistics to refine the agent’s belief about optimal architectural paths. The hierarchical action space decomposes model design into three levels: (1) modeling paradigm (generative vs. discriminative), (2) architectural backbone (e.g., ResNet, Transformers), and (3) optimization refinement (loss functions, hyperparameters). The method dynamically adjusts to distribution shifts by either warm-starting with historical priors or initiating ab initio exploration, ensuring statistical alignment with biological data properties.  
DOMAIN: computational biology, single-cell perturbation modeling  
STRUCTURE: other: hierarchical action space  
DATA_OBJECT: set or table  
INFERENCE: sampling or Monte-Carlo  
PROBLEM_FORM: prediction or classification  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: public-benchmark-used  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
