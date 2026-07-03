MECHANISM: The paper computes a hierarchical framework for modeling, simulation, and optimization of dynamic systems. It constructs models using equation-oriented and object-oriented principles, organizing variables (differential, algebraic, parameters) and equations into hierarchical submodels. The framework supports numerical and symbolic simulation, enabling differentiation of composite simulations. Parameter estimation updates unknown parameters and initial conditions using model predictions and measurements. Dynamic optimization computes control actions over a prediction horizon using control vector parameterization (CVP), which discretizes the control trajectory into intervals. Nonlinear model predictive control (NMPC) integrates repeated estimation, state updates, and dynamic optimization within a closed-loop framework. The framework leverages symbolic computation for automatic differentiation, allowing efficient embedding of customized differentiable simulations into optimization and control workflows. It uses a unified interface for nonlinear programming solvers, enabling consistent use of derivative information. The hierarchical structure allows modular development of large-scale models, with submodels combined across layers to form a complete system. Simulation handles time events by restarting solvers with updated parameters and initial conditions. The framework is demonstrated on a multiscale bioprocess, showing its application to hierarchical model construction, quasi-steady-state simulation, and adaptive NMPC.  
DOMAIN: bioprocess modeling and control  
STRUCTURE: other: hierarchical modeling and workflow-oriented tools  
DATA_OBJECT: model with variables and equations  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: optimization  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-private-data
