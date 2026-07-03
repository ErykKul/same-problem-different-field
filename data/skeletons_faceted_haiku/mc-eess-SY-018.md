MECHANISM: Simulate navigation of ferromagnetic microrobots through blood vessels guided by MRI magnetic field gradients. Extract vascular geometry from 3D medical images and fit a virtual corridor as a safety constraint. Model the robot as a sphere experiencing magnetic force from gradient coils and drag force from blood flow. Use PID feedback control to generate magnetic gradient waveforms that steer the robot along a pre-planned vessel centerline path. Compute three components: proportional control reacting to position error, integral control for steady-state correction, and derivative control for damping. Add feedforward compensation for estimated drag force. Model blood flow using pulsatile velocity profiles at different heart rates.
DOMAIN: Medical robotics and magnetic actuation
STRUCTURE: other: control simulation with PID
DATA_OBJECT: continuous function or field
INFERENCE: deterministic or closed-form
PROBLEM_FORM: control
DISTRIBUTION: none
COMPLEXITY: not stated
