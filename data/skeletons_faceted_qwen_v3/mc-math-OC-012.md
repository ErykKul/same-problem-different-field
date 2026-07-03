MECHANISM: The paper computes an optimization of energy efficiency (EE) in a MIMO system with two reconfigurable metasurfaces (WsRHSs) by jointly optimizing the transmit covariance matrix and the reflection matrices of the WsRHSs. The algorithm uses sequential fractional programming to iteratively improve the EE value, reformulating the problem to handle unit-rank constraints without semidefinite relaxation. The method guarantees convergence to a first-order optimal point of the EE maximization problem. In special cases (single-antenna or single-stream transmission), closed-form expressions for the reflection matrices and transmit power are derived. The optimization is subject to power constraints at the transmitter and global reflection constraints at the WsRHSs, which enforce that the total reflected power does not exceed the incident power. The system model involves channel matrices between the transmitter, WsRHSs, and receiver, with near-field propagation modeled via spherical wave equations and far-field propagation via Ricean fading. The EE is defined as the ratio of system capacity (derived from the log-determinant of a channel matrix) to total power consumption, which includes static and active power terms from the transmitter, receiver, and WsRHSs. Numerical simulations validate the performance gains of the proposed method compared to fully digital beamforming.  
DOMAIN: wireless communications  
STRUCTURE: other: constrained optimization  
DATA_OBJECT: matrix  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: optimization  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: simulation-study
