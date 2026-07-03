MECHANISM: Design a hierarchical control architecture with four modules for large mobile robots on slip-prone terrain. Low-level: approximate complex wheel actuation dynamics with a supervised deep neural network trained via Levenberg-Marquardt, augmented by adaptive control using logarithmic barrier functions for safety. Mid-level: implement nonlinear model predictive control with multiple-shooting transcription to correct pose deviations from a reference trajectory by updating wheel velocity commands in real-time, subject to kinematic constraints. High-level: visual simultaneous localization and mapping using stereo cameras provides accurate pose estimates. Stability analysis establishes uniform exponential stability of the actuation subsystem.
DOMAIN: Robotics and control for mobile systems
STRUCTURE: other: hierarchical control with neural networks and optimization
DATA_OBJECT: continuous function or field
INFERENCE: deterministic or closed-form
PROBLEM_FORM: control
DISTRIBUTION: none
COMPLEXITY: convergence rate
