MECHANISM: The paper computes dynamic state estimation for nonlinear systems using two variants of the Kalman filter. The process begins with initializing a state estimate and its covariance matrix. At each time step, the algorithm predicts the next state by applying a nonlinear function to the current state and process noise. For the Extended Kalman Filter (EKF), the nonlinear function is linearized using Jacobian matrices computed at the current state estimate. The prediction is then corrected using measurements, where the measurement model is also linearized. The correction step computes a Kalman gain by inverting a matrix derived from the predicted covariance and measurement noise. The state estimate is updated by combining the predicted state with the weighted difference between actual and predicted measurements. For the Unscented Kalman Filter (UKF), the nonlinear function is approximated using a set of sigma points sampled from the state distribution. These points are propagated through the nonlinear function, and the mean and covariance of the predicted state are computed from the transformed sigma points. The measurement update follows a similar process, with sigma points transformed through the measurement model to compute the predicted measurement and its covariance. Both methods iteratively refine the state estimate by alternating between prediction and correction steps, incorporating process and measurement noise models. The algorithms assume Gaussian noise distributions and use matrix operations to update state estimates and covariances. The computational steps involve solving linear systems, matrix inversions, and transformations of state and measurement vectors.  
DOMAIN: power systems  
STRUCTURE: dense linear algebra  
DATA_OBJECT: dense matrix  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: estimation  
DISTRIBUTION: continuous; normal  
COMPLEXITY: polynomial iterative  
DATA_AVAILABILITY: public-repository  
CODE_AVAILABILITY: public-repository  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
