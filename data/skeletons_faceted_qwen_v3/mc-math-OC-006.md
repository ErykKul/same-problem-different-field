MECHANISM: The paper computes a model predictive control (MPC) policy augmented with a Kalman filter to estimate unmodeled disturbance torques and manage angular momentum in a spacecraft. The process begins by defining a nonlinear dynamics model of the spacecraft, which includes the effects of active mass translation (AMT) and reflectivity control devices (RCDs) on angular momentum. This model is linearized for use in the Kalman filter and MPC frameworks. The Kalman filter estimates disturbance torques and system model errors in real time by processing sensor data and comparing it to predictions from the linearized model. These estimates are then integrated into the MPC framework, which solves an online optimization problem to determine the optimal sequence of control actions over a receding horizon. The optimization enforces constraints on both state trajectories and actuator limits, ensuring that the control actions remain within feasible bounds. The MPC policy incorporates a 4-reaction-wheel (4-RW) assembly, which is modeled using a pseudo-inverse allocation approach to distribute control effort among the wheels. The policy also accounts for attitude-dependent solar radiation pressure (SRP) forces and torques, which are computed based on the spacecraft's orientation. The Kalman filter's estimates of disturbance torques are used to refine the MPC's predictions, improving the accuracy of the control actions. The optimization problem is formulated as a quadratic program (QP), which guarantees fast convergence suitable for real-time implementation. The method is validated through numerical simulations that replicate the dynamics of the Solar Cruiser spacecraft, including scenarios involving large-angle slew maneuvers and attitude-dependent SRP effects. The simulations demonstrate that the proposed policy effectively manages angular momentum growth and improves the reliability of the control system compared to prior methods that lacked disturbance torque estimation or realistic 4-RW modeling.
DOMAIN: spacecraft attitude control
STRUCTURE: other: optimization-based control
DATA_OBJECT: set or table
INFERENCE: Bayesian posterior
PROBLEM_FORM: control
DISTRIBUTION: none
COMPLEXITY: polynomial iterative
DATA_AVAILABILITY: none
CODE_AVAILABILITY: none
PREREGISTRATION: none
EVIDENCE_BASIS: simulation-study
