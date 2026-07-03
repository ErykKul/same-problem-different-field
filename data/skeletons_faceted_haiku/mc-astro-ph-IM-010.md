MECHANISM: Couples neutrino-transport algorithms (spectral six-species two-moment scheme with DG discretization + IMEX time stepping + nested fixed-point iteration with Anderson acceleration for neutrino-matter coupling) to self-gravitating hydrodynamics in AMR framework (Flash-X). Two-moment closure with special-relativistic observer corrections; implicit treatment of collisional processes (scattering, pair production). Hybrid DG (neutrinos) and finite-volume (fluids) representation; operator-split evolution. GPU-enabled via OpenMP offloading or OpenACC.
DOMAIN: Core-collapse supernovae, neutrino-radiation hydrodynamics
STRUCTURE: spectral or transform (discontinuous Galerkin phase-space discretization)
DATA_OBJECT: dense matrix or tensor (phase-space distribution, fluid state)
INFERENCE: deterministic or closed-form (moment closure)
PROBLEM_FORM: simulation or generation
DISTRIBUTION: none
COMPLEXITY: polynomial iterative
