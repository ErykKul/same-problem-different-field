MECHANISM: The paper computes a data-driven reachability analysis for unknown nonlinear dynamics using Koopman operators. It begins by learning a linear approximation of the dynamics in a lifted state space via a neural network (NN) lifting function. This lifted space allows for efficient computation of closed-loop reachable sets using linear controllers. The method then maps these reachable sets back to the original state space using NN verification tools. To account for model mismatch between the Koopman dynamics and the true system, conformal prediction is applied to derive statistically valid error bounds that inflate the reachable sets, ensuring containment of true trajectories with a user-specified probability. These bounds are calibrated across a distribution of reference trajectories, enabling reuse without recomputation. The process involves training a Koopman model with a composite loss that enforces autoencoder accuracy and latent consistency, followed by designing a linear quadratic regulator (LQR) in the lifted space to track reference trajectories. Reachability analysis is performed on the linearized dynamics, and conformal prediction is used to inflate the reachable sets for probabilistic guarantees. The method is evaluated on high-dimensional robotic systems, demonstrating improved coverage, efficiency, and conservativeness compared to existing methods.  
DOMAIN: robotics safety verification  
STRUCTURE: dynamic programming  
DATA_OBJECT: sequence or time-series  
INFERENCE: sampling or Monte-Carlo  
PROBLEM_FORM: estimation  
DISTRIBUTION: continuous; linear  
COMPLEXITY: not stated  
DATA_AVAILABILITY: public-benchmark-used  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
