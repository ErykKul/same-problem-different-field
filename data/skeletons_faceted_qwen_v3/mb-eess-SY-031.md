MECHANISM: The paper computes a nonlinear deterministic observer on the special orthogonal group SO(3) to estimate orientation (attitude) from scalar measurements while compensating for gyroscope bias. The algorithm defines a state vector consisting of an orientation estimate (a rotation matrix) and a bias estimate. The observer dynamics are governed by a kinematic equation that combines a prediction term based on angular velocity measurements with an innovation term derived from scalar measurements through a Riccati-based framework. The innovation term is computed using a continuous Riccati equation (CRE) that evolves a symmetric positive definite matrix P(t), which weights the measurement residuals to drive the state estimate toward the true value. The stability of the observer is analyzed via a Lyapunov function, showing local exponential convergence under uniform observability conditions. The observability conditions are derived from the persistence of excitation of the measurement directions, ensuring that the linearized system's observability Gramian satisfies a lower bound. The method avoids high-dimensional embeddings by operating directly on SO(3), and the bias is explicitly modeled as a time-varying parameter with a zero-derivative dynamic. The scalar measurements are processed as linear combinations of the rotation matrix and known inertial directions, with the output error used to update the innovation term. The algorithm guarantees uniform local exponential stability when the measurement directions satisfy specific rank conditions, and the computational steps involve solving the CRE, computing the innovation term, and updating the state estimate through the observer dynamics.  
DOMAIN: aerospace engineering  
STRUCTURE: other: nonlinear observer  
DATA_OBJECT: dense matrix or tensor  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: estimation  
DISTRIBUTION: none  
COMPLEXITY: convergence rate  
DATA_AVAILABILITY: dataset-with-DOI-or-handle  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
