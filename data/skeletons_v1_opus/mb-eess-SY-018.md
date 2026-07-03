MECHANISM: A scalar state variable evolves under a first-order differential equation driven by the mismatch between a fixed reference quantity and an instantaneous delivered quantity, where the delivered quantity is a saturated trigonometric function of the state. A piecewise-defined gating function of a measured input variable is constructed: it returns one above an upper threshold, returns the input value itself in an intermediate band, and returns zero below a lower threshold. This gate multiplicatively rescales both the reference quantity and the proportional gain that couples the mismatch into the state derivative. A critical bound on the state is obtained from an equal-area balance condition on the saturated response curve, and the corresponding critical time is computed in closed form by integrating the reciprocal of the state derivative between an initial and the critical state value. Reducing the gain and reference during depressed-input intervals lowers the effective derivative, enlarging the integral and hence the critical time. The closed-form bound is then cross-checked against a fine-grained numerical time-stepping of the full nonlinear system under imposed disturbances. The scheme uses only locally measured quantities and introduces no tunable parameters.
DOMAIN: power electronics and grid stability control
STRUCTURE: other: low-order ODE integration
DATA_OBJECT: continuous function or field
INFERENCE: deterministic or closed-form
PROBLEM_FORM: control
DISTRIBUTION: continuous; none
COMPLEXITY: closed-form
