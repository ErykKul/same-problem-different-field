MECHANISM: The paper computes an event-driven control strategy that integrates Control Barrier Functions (CBFs) and Control Lyapunov Functions (CLFs) to ensure safety and resilience under adversarial inputs. The method begins by defining safety constraints as ellipsoidal regions derived from vehicle states, ensuring forward invariance of safe sets through Lie derivative conditions. To handle unknown Human-Driven Vehicle (HDV) dynamics, adaptive estimation updates the model using real-time sensor measurements, adjusting control barrier functions to account for estimation errors. The control problem is formulated as an optimal control task minimizing maneuver time and control effort while satisfying safety constraints, speed regulation, and collision avoidance. Event-driven Quadratic Programs (QPs) are solved at discrete time instants determined by thresholds on estimation errors or state deviations, reducing computational load. The QP incorporates both hard safety constraints (via CBFs) and soft performance objectives (via CLFs), with relaxation terms ensuring feasibility. Adaptive updates refine the HDV dynamics model, reducing conservativeness by resetting estimated states to measured values. The solution guarantees uniform ultimate boundedness of speed regulation errors under exponentially unbounded false data injection (EU-FDI) attacks, ensuring collision-free maneuvers and stable velocity regulation. The method explicitly addresses the breakdown of traditional event-driven CBFs under EU-FDI by redesigning the safety mechanism to remain valid despite adversarial inputs corrupting acceleration channels. The framework combines adaptive estimation, event-triggered QP solving, and robust constraint handling to achieve resilience without requiring explicit identification of compromised components.  
DOMAIN: vehicle control under adversarial attacks  
STRUCTURE: other: event-driven quadratic programming  
DATA_OBJECT: sequence or time-series  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: control  
DISTRIBUTION: none  
COMPLEXITY: polynomial iterative  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: simulation-study
