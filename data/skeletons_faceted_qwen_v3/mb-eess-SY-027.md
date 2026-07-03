MECHANISM: The paper computes a distributed adaptive synchronization framework for a network of heterogeneous second-order systems under unknown dynamics. It begins by reparameterizing the system's error dynamics to yield gradient-based updates, ensuring global asymptotic synchronization when the closed-loop system is strictly positive real (SPR). This involves constructing a Lyapunov function that guarantees bounded parameter estimates and convergence of synchronization errors under persistent excitation. For non-SPR cases, frequency shaping is applied to recover effective passivity, enabling stability guarantees via the Meyer-Kalman-Yakubovich (MKY) lemma. The framework operates on a graph structure, where each node exchanges position data with neighbors, and the synchronization error is defined as the deviation from the leader's trajectory. Adaptive laws update parameters based on the gradient of the error and its integral, while the control input combines terms derived from the estimated inertia and damping coefficients. The analysis distinguishes between SPR and non-SPR regimes, with the latter requiring additional shaping to ensure passivity. Simulations validate robustness to disturbances and parameter adaptation across various network topologies. The method relies on Lyapunov-based stability proofs and does not assume prior knowledge of the leader's dynamics or SPR properties.  
DOMAIN: control theory and distributed systems  
STRUCTURE: dynamic programming  
DATA_OBJECT: graph or network  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: control or test  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: mathematical-proof
