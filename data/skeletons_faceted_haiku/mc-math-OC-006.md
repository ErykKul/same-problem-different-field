MECHANISM: Model spacecraft attitude dynamics with time-varying moment of inertia affected by active mass translator motion; employ a Kalman filter to estimate unmeasured disturbance torques in real time; design a model predictive control (MPC) policy that solves online quadratic programs to optimize control inputs (AMT and RCD actuation, RW commands) subject to state and actuator constraints; allocate MPC-computed control torques to four reaction wheels using pseudoinverse methods; track attitude slew maneuvers while managing reaction wheel saturation.
DOMAIN: Spacecraft attitude control and momentum management for solar sails
STRUCTURE: dynamic programming
DATA_OBJECT: sequence or time-series
INFERENCE: Bayesian posterior
PROBLEM_FORM: control
DISTRIBUTION: none
COMPLEXITY: polynomial iterative
