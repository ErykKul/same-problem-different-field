MECHANISM: The paper computes dynamic state estimation of power systems using extended Kalman filter (EKF) and unscented Kalman filter (UKF). The EKF linearizes nonlinear system dynamics via first-order Taylor expansions, while the UKF approximates the state distribution using a set of sigma points sampled from the prior distribution. Both methods iteratively predict the system state and covariance based on the power system model, then update these estimates using noisy measurement data. The power system model includes Newton-Raphson power flow equations and admittance matrix calculations to represent generator dynamics, load behavior, and network topology. The filters use a recursive algorithm: initial state and covariance are set, then prediction and update steps are repeated for each time step. The measurement model maps the true state to expected sensor outputs, accounting for noise in voltage, current, and frequency measurements. The UKF outperforms the EKF in nonlinear scenarios due to its deterministic sampling strategy. The algorithm is validated on case studies using the WECC 3-machine 9-bus and New England 10-machine 39-bus systems, with performance metrics comparing estimation accuracy between EKF and UKF. The code for Newton-Raphson power flow, admittance matrix computation, and filter implementations is publicly available on GitHub.  
DOMAIN: power systems dynamics  
STRUCTURE: other: recursive filtering  
DATA_OBJECT: sequence or time-series  
INFERENCE: Bayesian posterior  
PROBLEM_FORM: estimation  
DISTRIBUTION: continuous; Gaussian  
COMPLEXITY: not stated  
DATA_AVAILABILITY: public-repository  
CODE_AVAILABILITY: public-repository  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
