MECHANISM: This paper computes a quadratic unconstrained binary optimization (QUBO) formulation for training binary neural networks (BNNs). The process begins by encoding the activation function of each neuron as a binary constraint, transforming the pre-activation value into a binary expansion where the most significant bit indicates the neuron's activation state. For each neuron, the sum of bipolar inputs is converted into a binary representation using auxiliary variables and integer parameters derived from the number of predecessors. These constraints are then linearized by introducing auxiliary binary variables to represent products of weight and activation variables. The training problem is formulated as a non-linear feasibility problem with quadratic constraints, which is subsequently transformed into a QUBO problem by eliminating higher-order terms through substitution and rearrangement. Regularization is incorporated via two methods: a quadratic penalty term that maximizes neuron margins by increasing the magnitude of pre-activation values, and an iterative dropout-inspired scheme that modifies network topology by randomly removing subnetworks and adjusting linear penalties on parameters. The QUBO formulation is solved using a GPU-based Ising machine, and computational experiments validate the effectiveness of the regularization techniques in improving classification accuracy on unseen data. The method does not rely on gradient-based optimization or probabilistic inference, instead focusing on exact discrete optimization through QUBO relaxation.  
DOMAIN: binary neural networks and optimization  
STRUCTURE: quadratic unconstrained binary optimization  
DATA_OBJECT: binary variables and QUBO matrix  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: optimization  
DISTRIBUTION: none  
COMPLEXITY: combinatorial or NP-hard  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-private-data
