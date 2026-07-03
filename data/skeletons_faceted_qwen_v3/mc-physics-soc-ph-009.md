MECHANISM: The paper computes a dynamic network model where node degrees evolve as a state-dependent random walk with variable diffusion coefficients. The process begins by defining a state space of possible degrees for each node. Degree changes are modeled as transitions between states, with probabilities determined by the current degree. To handle the handshake theorem, a matching queue is introduced as an intermediate step: when a node's degree changes, it is added to the queue, and connections are formed only when compatible nodes are matched. The model ensures no multiple edges or self-loops by enforcing boundary conditions (degrees remain between 1 and n-1). In discrete time, transitions are governed by a Markov matrix with probabilities derived from a stay probability function S(k), leading to a stationary degree distribution. In continuous time, degree changes follow a non-homogeneous Poisson process with rate λ(k) dependent on the current degree. The stationary distribution is derived using balance equations, showing convergence to a power-law form under specific conditions. The model's parameters (e.g., S(k) or λ(k)) control the diffusion coefficient and stability of the degree distribution. Simulations validate the theoretical results, demonstrating convergence to scale-free properties without relying on growth or preferential attachment. The mechanism is mathematically described through transition matrices, Poisson processes, and balance equations, with explicit formulas for stationary distributions in both discrete and continuous time.  
DOMAIN: network modeling  
STRUCTURE: graph traversal  
DATA_OBJECT: set or table  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: estimation  
DISTRIBUTION: continuous; power-law  
COMPLEXITY: consistency  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: simulation-study
