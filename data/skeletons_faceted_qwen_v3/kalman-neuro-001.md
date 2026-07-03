MECHANISM: The paper computes a Bayesian filtering algorithm derived from variational free energy minimisation via gradient descent. It begins with a probabilistic model of hidden states and observations, defining a joint distribution over hidden variables and measurements. A variational density is introduced to approximate the true posterior, and the free energy is expressed as the difference between the variational density and the joint distribution. The free energy is minimized by optimizing parameters of the variational density, which involves computing gradients with respect to both the mean and covariance of the hidden states. The gradient descent updates are derived using matrix inversion lemmas and properties of Gaussian distributions. The steady-state solution of this optimization corresponds to the Kalman filter equations, which are shown to emerge naturally from the variational treatment. The derivation includes prediction and correction steps for the mean and covariance of the hidden states, with the Kalman gain computed as a function of the covariance matrices. The method assumes linear dynamics and Gaussian noise, leading to closed-form updates for the posterior distribution. The approach bridges variational inference and classical Kalman filtering by showing that the latter is a special case of the former under specific assumptions. The algorithm iteratively refines estimates of hidden variables using observed data, balancing the fit to the data and the complexity of the model through the free energy objective. The derivation relies on Laplace approximations and matrix algebra to simplify the optimization problem, ultimately yielding the standard Kalman filter update equations.  
DOMAIN: Bayesian estimation and Kalman filters  
STRUCTURE: graphical models  
DATA_OBJECT: continuous function or field  
INFERENCE: variational  
PROBLEM_FORM: estimation  
DISTRIBUTION: continuous; Gaussian  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: mathematical-proof
