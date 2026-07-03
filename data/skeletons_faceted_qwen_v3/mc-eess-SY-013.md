MECHANISM: The paper computes a control framework for large-scale mobile robots (LSMRs) using a supervised deep neural network (SDNN) and nonlinear model predictive control (NMPC). The SDNN approximates the actuation dynamics of the robot by learning from input-output data collected under safe operating conditions. The network is trained using Levenberg-Marquardt backpropagation, which iteratively minimizes a mean-squared error loss between predicted and target outputs. The SDNN's architecture consists of multiple hidden layers with affine transformations and nonlinear activation functions, mapping per-side velocity commands to motor RPM signals. To handle out-of-distribution disturbances, the SDNN is augmented with robust adaptive control laws that adjust the control signal based on tracking errors and a logarithmic barrier function. The logarithmic barrier function enforces safety constraints by penalizing deviations from a predefined threshold on the robot's pose error. At the high level, NMPC computes optimal wheel velocity commands by solving a constrained optimal control problem (OCP) transcribed into a nonlinear programming problem (NLP) using multiple-shooting. The NLP is solved iteratively with sensor data fusion to correct drift from the reference trajectory. The control policy ensures uniform exponential stability of the actuation subsystem and system-level safety through the logarithmic barrier. The framework synchronizes modules operating at different frequencies and validates performance on a 6,000 kg LSMR.  
DOMAIN: robotics and control systems  
STRUCTURE: dense linear algebra  
DATA_OBJECT: dense matrix  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: control  
DISTRIBUTION: none  
COMPLEXITY: polynomial iterative  
DATA_AVAILABILITY: public-benchmark-used  
CODE_AVAILABILITY: public-repository  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
