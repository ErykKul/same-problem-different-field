MECHANISM: The paper computes a numerical solution to the Burgers turbulence problem using an explicit relaxation filtering closure based on Perona-Malik anisotropic diffusion. The method applies a nonlinear diffusion equation with spatially varying diffusivity functions to model subgrid-scale effects in large eddy simulations. The Perona-Malik model is adapted to suppress numerical oscillations while preserving sharp gradients (shock capturing) through a compact stencil scheme. The algorithm iteratively solves the filtered Navier-Stokes equations with explicit time-stepping, incorporating a relaxation parameter that controls the trade-off between subgrid-scale modeling and resolution. Sensitivity analysis is performed on free parameters governing the diffusivity functions, which are chosen to minimize energy accumulation at grid cutoff frequencies. The method is compared against direct numerical simulations (DNS) and under-resolved DNS results to validate its ability to prevent spurious oscillations and maintain spectral accuracy. The computational framework operates on a structured grid with finite-volume discretization, using a flux-limited scheme to enforce monotonicity. The relaxation filtering closure is applied post-discretization to modify the resolved scales, with the anisotropic diffusion tensor computed from local gradient magnitudes. The method's efficiency is demonstrated through its ability to extend the inertial range of turbulence spectra without increasing computational cost. The algorithm is implemented in a way that avoids explicit time integration of the diffusion term, instead using a semi-implicit approach to maintain stability. The paper emphasizes the role of parameter tuning in balancing subgrid-scale modeling accuracy against numerical stability constraints.  
DOMAIN: fluid dynamics and turbulence modeling  
STRUCTURE: other: PDE-based numerical method  
DATA_OBJECT: grid or lattice  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: simulation or generation  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-private-data
