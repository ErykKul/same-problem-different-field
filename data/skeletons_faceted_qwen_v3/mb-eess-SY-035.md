MECHANISM: The paper computes a hybrid parameter estimation algorithm for linear regression models, combining continuous and discrete dynamics to achieve finite-time convergence. The algorithm operates on a state vector containing two parameter estimates, a timer, and a counter. During continuous flows, the parameters are updated using gradient descent-like rules with adaptation rates γ₁ and γ₂. Discrete jumps occur periodically at a fixed time δ, where the parameters are reset using a gain matrix derived from the state transition matrices of the system. The method requires the regressor to be exciting over a finite interval for constant parameters, and persistent excitation for piecewise constant parameters. The algorithm ensures convergence to the true parameter values in finite time by leveraging hybrid system theory, with robustness guarantees under measurement noise analyzed via input-to-state stability. The key steps involve solving differential equations during flows, computing state transition matrices, and applying jump maps that depend on the system's dynamics and the excitation conditions. The method avoids computational bottlenecks inherent to other approaches by operating directly in n-dimensional parameter space with O(n) cost during flows and O(n³) operations only at sparse jumps. The proof of convergence relies on Lyapunov functions and conditions ensuring the invertibility of state transition matrices.  
DOMAIN: parameter estimation in linear regression models  
STRUCTURE: other: hybrid systems  
DATA_OBJECT: set or table  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: estimation  
DISTRIBUTION: none  
COMPLEXITY: polynomial iterative  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: mathematical-proof
