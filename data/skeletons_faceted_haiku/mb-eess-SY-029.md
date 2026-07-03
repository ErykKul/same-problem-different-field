MECHANISM: Power flow equations are reformulated as a continuous-time dynamical system (Newton flow), and quantized-state methods are employed to govern the evolution toward the steady-state solution. State quantization controls when updates occur rather than using fixed time steps, providing adaptive stepping behavior that enhances numerical robustness in ill-conditioned problems. The approach reinterprets Newton iterations as the integration of a dynamical system whose equilibrium corresponds to power flow solutions, with quantization providing a mechanism to manage adaptation without explicit discretization.
DOMAIN: Power systems and numerical methods
STRUCTURE: Other: dynamical systems integration
DATA_OBJECT: dense matrix or tensor
INFERENCE: Optimization only
PROBLEM_FORM: Estimation
DISTRIBUTION: none
COMPLEXITY: polynomial iterative
