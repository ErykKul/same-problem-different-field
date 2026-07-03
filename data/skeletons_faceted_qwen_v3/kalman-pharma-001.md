MECHANISM: The paper computes a Bayesian-based multiple-model square root cubature Kalman filter (MMSRCKF) to estimate time-varying parameters of a first-order linear parameter-varying (LPV) model describing a system's response to input. The model incorporates a state vector augmented with unknown parameters and an input delay, which is handled separately via a multiple-model module. The algorithm uses a third-degree spherical-radial cubature rule to approximate integrals in Bayesian estimation, ensuring numerical stability through Cholesky factorization of the error covariance matrix. The process begins with initializing the state vector and covariance matrix, then iteratively propagating cubature points through the system dynamics to predict the state. Measurement updates refine the state estimate using weighted cubature points and innovation covariance matrices. The multiple-model component estimates the input delay by calculating posterior probabilities for candidate delay values, updating the state vector accordingly. The method assumes Gaussian process and measurement noise, and the algorithm iterates prediction and correction steps to converge on parameter estimates. Validation compares results against simulation scenarios and animal experiment data to confirm effectiveness. The core computation involves nonlinear state estimation with uncertainty quantification, parameter augmentation, and delay identification through Bayesian inference.  
DOMAIN: biomedical engineering  
STRUCTURE: graphical models  
DATA_OBJECT: set or table  
INFERENCE: Bayesian posterior  
PROBLEM_FORM: estimation  
DISTRIBUTION: continuous; Gaussian  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-private-data
