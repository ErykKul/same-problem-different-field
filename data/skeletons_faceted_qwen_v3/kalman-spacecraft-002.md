MECHANISM: The paper computes an estimator for a state vector composed of elements from a matrix Lie group, using a filter that linearizes the system dynamics and measurement model around the current estimate. The state includes a transformation matrix and a bias term, with errors defined through the Lie group structure. The algorithm iteratively predicts the state, computes the Kalman gain based on the covariance of the state and measurement noise, updates the state estimate using the measurement residual, and propagates the covariance forward. The error dynamics are derived using the exponential map of the Lie algebra associated with the matrix Lie group, ensuring invariance properties. The measurement model linearizes the relationship between the state and observations, incorporating the Lie group structure to handle nonlinearities. The filter updates the state estimate and covariance in a closed-loop manner, with the error terms expressed in a consistent frame defined by the estimated attitude. The process involves Jacobian calculations for the system dynamics and measurement model, which are used to approximate the nonlinear functions. The algorithm ensures that the estimation error remains well-defined on the Lie group manifold, leveraging the properties of the exponential map and the Lie algebra. The final state estimate is obtained by exponentiating the updated error terms, resulting in a transformation matrix that represents the attitude. The method is applied to the problem of estimating the orientation of an entity using vector observations, with the bias term accounting for systematic errors in the measurements. The computational steps include initialization of the state and covariance, prediction of the state and covariance, computation of the Kalman gain, update of the state and covariance, and propagation of the state and covariance for the next iteration. The algorithm is designed to handle the nonlinearities inherent in the system dynamics and measurement model by linearizing around the current estimate, ensuring convergence and accuracy in the presence of noise and uncertainty.

DOMAIN: spacecraft attitude estimation using matrix Lie groups

STRUCTURE: other: extended Kalman filter

DATA_OBJECT: dense matrix or tensor

INFERENCE: Bayesian posterior

PROBLEM_FORM: estimation

DISTRIBUTION: continuous; Gaussian

COMPLEXITY: not stated

DATA_AVAILABILITY: none

CODE_AVAILABILITY: none

PREREGISTRATION: none

EVIDENCE_BASIS: mathematical-proof
