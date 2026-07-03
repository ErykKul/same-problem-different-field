MECHANISM: The paper computes a distributed routing protocol that dynamically adjusts transmission parameters and route selection based on real-time network conditions. The process begins by generating non-periodic frequency sequences using a logistic chaotic map to avoid predictable patterns, enhancing resistance to interference. Transmission power is adjusted iteratively based on instantaneous signal-to-noise ratio (SNR) measurements and residual node energy, maintaining a target SNR threshold while conserving energy. Routing decisions are made using a composite cost function that combines link reliability (derived from SNR) and node energy levels, favoring paths with higher success probabilities and balanced energy consumption. When direct transmission fails, neighboring nodes probabilistically participate in cooperative relaying, selecting the relay with the highest SNR to the destination. Time-reversal channel focusing is applied to exploit multipath components, improving SNR through constructive interference. All computations are performed locally at each node without centralized coordination, enabling self-organizing behavior. The protocol operates on a heterogeneous network model represented as a graph, with connectivity determined by Euclidean distance and communication radius. Link quality is modeled using a log-distance path loss formula with shadowing, and packet success probabilities are calculated using the complementary error function of SNR. Energy consumption is tracked per hop using a fixed-cost model, and relay activation probabilities are applied to manage spatial diversity. The system's performance is evaluated through Monte Carlo simulations, measuring packet delivery ratios, latency, and SNR under varying channel conditions and adversarial interference.  
DOMAIN: communication protocols and network optimization  
STRUCTURE: other: distributed routing algorithm  
DATA_OBJECT: graph or network  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: optimization  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: simulation-study
