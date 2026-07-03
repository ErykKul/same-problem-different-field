MECHANISM: The paper computes a solution to a nonlinear system of equations by reformulating Newton's method as a continuous-time dynamical system (the Newton flow). The system is represented as an ordinary differential equation (ODE) where the derivative of the state vector is proportional to the negative of the residual function. The solution is obtained by numerically integrating this ODE using explicit or implicit discretization schemes. For explicit schemes, the forward Euler method is applied, leading to a damped Newton iteration with a step size that affects convergence behavior. For implicit schemes, the backward Euler method requires solving a nonlinear algebraic system at each step, creating a double-loop structure. The paper introduces quantized-state system (QSS) concepts to adapt the step size dynamically: state variables are quantized, and updates occur only when the state changes by a predefined quantum. The step size is computed based on the magnitude of the state derivative, ensuring event-driven adaptation. This approach is analyzed for local convergence properties under varying step sizes and tested on a synthetic power flow test case. The method is compared to fixed-step and heuristic-based variants, showing improved robustness in ill-conditioned scenarios.  
DOMAIN: power systems  
STRUCTURE: other: numerical integration with adaptive step control  
DATA_OBJECT: dense matrix or tensor  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: estimation  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: public-benchmark-used  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: simulation-study
