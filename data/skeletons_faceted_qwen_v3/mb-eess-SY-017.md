MECHANISM: The paper computes a hybrid control strategy for continuum robots by transforming visual observations into a geometrically interpretable shape space. Multi-view planar images are encoded using Bézier curves, which parameterize the robot's shape with control points. These control points are concatenated into a feature vector representing the three-dimensional configuration. Neural ordinary differential equations (NODEs) are then trained to model both shape dynamics and end-effector position dynamics from data, without requiring explicit analytical models. The NODEs approximate the time derivative of the shape state vector and end-effector state vector as functions of the current state and actuation inputs. A Jacobian-based control framework combines these learned models to regulate shape and position simultaneously. The Bézier curve fitting process uses least-squares optimization to estimate intermediate control points from skeletonized image data. The shape feature vector is derived by vectorizing concatenated planar shape matrices from multiple views. The NODEs are trained using a loss function that minimizes the difference between predicted and actual state trajectories. The method enables obstacle avoidance and self-motion by leveraging the explicit geometric structure of the shape space. The control strategy maintains end-effector accuracy while adapting to environmental constraints through learned dynamics.
DOMAIN: robotics and geometric modeling
STRUCTURE: other: neural differential equations
DATA_OBJECT: point set
INFERENCE: deterministic or closed-form
PROBLEM_FORM: control
DISTRIBUTION: none
COMPLEXITY: not stated
DATA_AVAILABILITY: none
CODE_AVAILABILITY: none
PREREGISTRATION: none
EVIDENCE_BASIS: empirical-with-private-data
