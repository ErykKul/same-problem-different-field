MECHANISM: The paper computes two accuracy metrics for a network of nodes exchanging information based on timeliness. It models the source as a continuous-time Markov chain (CTMC) with $M$ states, where each state transition generates a new information version. Nodes accept incoming packets only if they are fresher than their local copy, leading to potential discrepancies between the freshest packet and the current source state. The system is analyzed using a stochastic hybrid systems (SHS) framework, which combines discrete CTMC states with continuous variables tracking node accuracy ($C_i(t)$) and version age ($X_i(t)$). The SHS framework derives steady-state balance equations and matrix-valued recursions to quantify the expected fraction of nodes with accurate information (average accuracy) and the accuracy of the freshest node in any subset (freshness-based accuracy). Transitions between CTMC states and gossip events are modeled as discrete jumps in the hybrid state, with reset rules updating accuracy and version age based on source pushes or gossip exchanges. The analysis extends to multi-state CTMCs using a joint CTMC approach, and the paper quantifies how source push rates and gossip rates influence the fraction of nodes with accurate information. The solution involves solving matrix recursions to compute steady-state probabilities of accuracy metrics, leveraging the stationary distribution of the CTMC to determine long-term behavior.  
DOMAIN: information networks and Markov processes  
STRUCTURE: other: stochastic hybrid systems  
DATA_OBJECT: set or table  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: estimation  
DISTRIBUTION: binary; CTMC  
COMPLEXITY: polynomial iterative  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: mathematical-proof
