MECHANISM: The paper computes a hybrid numerical scheme for solving hyperbolic partial differential equations arising from fluid dynamics and radiative transfer. The method combines discontinuous Galerkin (DG) spatial discretization with implicit-explicit (IMEX) time integration to handle stiff source terms. A nonlinear system is solved iteratively using nested fixed-point iteration accelerated by Anderson acceleration, enabling implicit treatment of collisional interactions. Fluid variables are represented in a hybrid DG-finite-volume (FV) framework, with operator-split evolution separating transport and collisional processes. Phase-space discretization uses spectral methods with algebraic closure for moment equations. Special-relativistic corrections are applied to observer frames with accuracy proportional to velocity over speed of light. The algorithm is implemented on adaptive mesh refinement (AMR) grids, with GPU acceleration via OpenMP or OpenACC. Verification is performed through transport tests, relaxation problems, and comparison with existing codes. The method is applied to spherically symmetric and axisymmetric core-collapse supernova simulations.  
DOMAIN: computational physics  
STRUCTURE: other: hybrid DG-FV  
DATA_OBJECT: grid or lattice  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: simulation or generation  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: simulation-study
