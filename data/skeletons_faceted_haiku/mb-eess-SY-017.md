MECHANISM: A vision-based self-modeling framework learns robot shape and end-effector dynamics from multi-view camera observations without analytical models. Robot backbones in each planar image are parameterized using quadratic Bézier curves fitted via least-squares to skeleton extractions, yielding compact control-point representations. Control-point coordinates from multiple views are stacked into a high-dimensional shape feature vector uniquely determining 3D configuration. Neural ordinary differential equations learn both shape dynamics and end-effector position dynamics as continuous vector fields. Jacobian matrices are estimated numerically from the learned dynamics via finite differences. Hybrid shape-position control combines weighted shape and position controllers with pseudo-inverse Jacobian-based command generation. Obstacle avoidance calculates closest point on Bézier curves and applies escape velocities with magnitude proportional to proximity.
DOMAIN: Continuum robot control with vision-based self-modeling
STRUCTURE: other: neural ODE dynamics learning with Jacobian-based control
DATA_OBJECT: dense matrix or tensor
INFERENCE: deterministic or closed-form
PROBLEM_FORM: control
DISTRIBUTION: none
COMPLEXITY: polynomial iterative
