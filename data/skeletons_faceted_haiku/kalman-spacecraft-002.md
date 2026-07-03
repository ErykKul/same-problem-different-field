MECHANISM: Estimate rotating rigid-body attitude (orientation) and gyroscope bias drift from vector observations. Formulate the state using elements of the Special Euclidean group SE(3), combining rotation matrices and translation vectors. Define estimation error on the Lie group manifold rather than in Euclidean space, capturing the geometric constraints of rotations. Apply Extended Kalman Filter using Jacobians of the nonlinear dynamics and measurement models, computing prediction and correction updates in the Lie algebra. Approximate the exponential map for state updates. Provide two variants: one with body-frame error definition, one with reference-frame error definition, both respecting the geometric structure.
DOMAIN: Aerospace attitude estimation and inertial navigation.
STRUCTURE: dynamic programming
DATA_OBJECT: sequence or time-series
INFERENCE: Bayesian posterior
PROBLEM_FORM: estimation
DISTRIBUTION: continuous; continuous
COMPLEXITY: polynomial iterative
