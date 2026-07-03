MECHANISM: The paper computes a spacecraft attitude estimation algorithm using the SE(3) matrix Lie group. It formulates the spacecraft's attitude and gyroscope bias as elements of the special Euclidean group SE(3), which represents rigid-body motions in three dimensions. The algorithm derives an extended Kalman filter (EKF) tailored to the SE(3) structure, leveraging Lie group theory to handle the nonlinearities inherent in attitude dynamics. The filter's state transition and measurement models are expressed in terms of SE(3) elements, with the error terms defined using the Lie algebra so(3) corresponding to SE(3). The paper shows that this SE(3)-EKF is equivalent to the geometric EKF (GEKF) previously derived, but framed through the SE(3) representation rather than frame errors. A variant of the SE(3)-EKF is also derived using reference frame attitude error, which aligns closely with the right-invariant EKF formulation. The algorithm iteratively updates the attitude estimate and gyroscope bias using the EKF's prediction and correction steps, incorporating measurements from vector observations. The computational core involves matrix exponentiation and logarithm operations on SE(3) elements, as well as the propagation of uncertainty through the nonlinear dynamics. The method avoids singularities and maintains the geometric integrity of the attitude representation by operating directly on the Lie group rather than parameterizing it with Euler angles or quaternions. The paper validates the algorithm's correctness through mathematical derivation and comparison with existing methods, emphasizing its geometric consistency and computational efficiency.  
DOMAIN: spacecraft attitude estimation  
STRUCTURE: dynamic programming  
DATA_OBJECT: dense matrix or tensor  
INFERENCE: Bayesian posterior  
PROBLEM_FORM: estimation  
DISTRIBUTION: continuous; continuous  
COMPLEXITY: polynomial iterative  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: mathematical-proof
