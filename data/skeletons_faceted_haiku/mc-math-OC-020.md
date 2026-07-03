MECHANISM: A software framework that combines equation-oriented, hierarchical modeling with symbolic computation and automatic differentiation to support bioprocess simulation, optimization, and control. Models are defined as compositions of variables and differential-algebraic equations organized into hierarchies. Simulation is implemented using DAE solvers with support for both numerical and symbolic inputs, enabling composite differentiable simulation workflows. Parameter estimation formulates model calibration as a nonlinear program solved using gradient-based optimization. Dynamic optimization uses control vector parameterization to transcribe the optimal control problem into an NLP. Adaptive NMPC repeatedly performs parameter estimation, state estimation via simulation, and dynamic optimization in a closed loop. The framework integrates these components into a unified workflow for large-scale multiscale process applications.
DOMAIN: Bioprocess control, nonlinear model predictive control, process optimization
STRUCTURE: none
DATA_OBJECT: none
INFERENCE: optimization only
PROBLEM_FORM: control
DISTRIBUTION: none
COMPLEXITY: not stated
