MECHANISM: An adaptive control function modifies power synchronization loops in grid-forming inverters to enhance stability margins. The synchronization loop governs angle dynamics: the phase angle difference between inverter and grid increases when power reference exceeds delivered power. A piecewise linear voltage-dependent function modulates droop coefficient and power reference setpoint based on terminal voltage magnitude. During normal conditions (V > 0.9 pu), parameters remain nominal; during voltage sags (0.5 < V ≤ 0.9 pu), parameters scale proportionally with voltage; during severe faults (V ≤ 0.5 pu), parameters collapse to zero. Critical clearing time is derived analytically via equal-area criterion on saturation curve and integrals of angle dynamics. The adaptive scaling prevents excessive phase angle acceleration toward instability boundaries.
DOMAIN: Transient stability control for grid-forming inverters
STRUCTURE: other: adaptive control with piecewise function logic
DATA_OBJECT: none
INFERENCE: deterministic or closed-form
PROBLEM_FORM: control
DISTRIBUTION: none
COMPLEXITY: not stated
