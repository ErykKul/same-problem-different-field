MECHANISM: Combine a 9-state Multiplicative Extended Kalman Filter (MEKF) with a Bayesian Multiple-Model Adaptive Estimation (MMAE) framework to jointly estimate spacecraft attitude, angular velocity, and gyroscope bias alongside fixed star-tracker sensor misalignments. The MEKF processes TRIAD-derived attitude observations and gyroscope measurements via quaternion kinematics. The MMAE layer maintains a discrete grid of misalignment hypotheses and updates their probabilities. A novel diversity metric triggers adaptive refinement of the grid around a weighted-mean estimate to prevent premature model collapse.
DOMAIN: Spacecraft attitude determination and sensor calibration in deep-space CubeSat missions
STRUCTURE: graphical models
DATA_OBJECT: sequence or time-series
INFERENCE: Bayesian posterior
PROBLEM_FORM: estimation
DISTRIBUTION: continuous; continuous
COMPLEXITY: polynomial iterative
