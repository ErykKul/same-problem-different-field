MECHANISM: The paper computes a control system for navigating a spherical entity through a constrained 3D path. It begins by interpolating discrete data points along a path using piecewise cubic Hermite polynomials to approximate continuous trajectories. Geometric properties of the path, including tortuosity calculated via second derivatives of the path's parametric equations, are used to define constraints. Blood flow dynamics are modeled with a drag force equation dependent on velocity differences between the entity and the surrounding medium, with velocity profiles adjusted by radius and path-specific constants. A PID controller generates correction terms for trajectory deviations, combining proportional, integral, and derivative errors derived from position and velocity setpoints. Magnetic gradients are computed as a function of the sum of PID components and a feedforward term compensating for drag forces, with gradient magnitudes scaled by the inverse of the entity's magnetic moment. The magnetic moment is derived from material properties and volume, while propulsion forces are calculated as the product of magnetization, gradient strength, and entity volume. Simulations validate gradient control under varying blood flow profiles and safety constraints, with results visualized using 3D rendering tools. The system operates in real-time with sub-millisecond execution times, ensuring responsiveness to dynamic path adjustments and safety limits.  
DOMAIN: medical robotics and MRI guidance  
STRUCTURE: other: control system simulation  
DATA_OBJECT: mesh  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: simulation or generation  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: simulation-study
