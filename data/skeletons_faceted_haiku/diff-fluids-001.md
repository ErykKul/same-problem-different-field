MECHANISM: Apply nonlinear anisotropic diffusion via Perona-Malik model to a numerical discretization of the Burgers equation. After each time step, filter the solution field by iterating a parabolic diffusion equation once, using a spatially-varying conductivity kernel that depends on local gradients. The kernel preserves high-gradient regions (shocks) while dissipating low-gradient regions. Conduct sensitivity analysis on free parameters controlling the diffusion magnitude.
DOMAIN: Computational fluid dynamics and turbulence modeling
STRUCTURE: spectral or transform
DATA_OBJECT: grid or lattice
INFERENCE: deterministic or closed-form
PROBLEM_FORM: simulation or generation
DISTRIBUTION: none
COMPLEXITY: polynomial iterative
