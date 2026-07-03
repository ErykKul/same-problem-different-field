MECHANISM: A whole-body controller combines model-based admittance control for the arm with reinforcement learning for locomotion. The admittance model maps external forces into desired end-effector velocities, enabling compliant contact behavior. These velocities are tracked jointly by arm and leg controllers to achieve a unified force response. A Reference Governor enforces safety constraints via model-based design. A Kalman filter augmented with neural networks estimates locomotion state. The RL policy learns locomotion decisions while training incorporates the admittance controller, enabling coupled dynamics without explicit joint optimization.
DOMAIN: Legged robot loco-manipulation control
STRUCTURE: Other: hybrid model-learning control
DATA_OBJECT: sequence or time-series
INFERENCE: sampling or Monte-Carlo
PROBLEM_FORM: Control
DISTRIBUTION: none
COMPLEXITY: not stated
