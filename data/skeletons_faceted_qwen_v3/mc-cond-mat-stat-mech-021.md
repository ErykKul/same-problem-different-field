MECHANISM: The paper computes a renewal equation that relates the joint probability density of particle position and gate state to the probability density and first passage time (FPT) density for a totally absorbing boundary. The method decomposes sample paths into alternating sequences of bulk diffusion and instantaneous adsorption/desorption events, terminating when adsorption coincides with an open gate. To avoid immediate re-adsorption, the particle is reset to a distance ε from the boundary upon encountering a closed gate. The renewal equation is solved using Laplace transforms and the convolution theorem, with the solution for ε > 0 shown to converge to the original gated FPT problem as ε → 0. The approach generalizes to higher dimensions by extending spectral methods and introduces a Dirichlet-to-Neumann operator on the target surface. The method explicitly separates the FPT problem for reaching the boundary from the rules governing diffusion restarts. The paper derives explicit solutions for specific cases, including a half-line with a stochastically gated boundary and finite intervals with correlated or uncorrelated boundary conditions. The renewal framework is applied to diffusion in a sphere and compared to alternative formulations involving recursive equations conditioned on trap states. The computational steps involve solving partial differential equations (PDEs) with boundary conditions, transforming them via Laplace methods, and handling integral equations through convolution. The analysis includes deriving survival probabilities, FPT densities, and Green’s functions for modified Helmholtz equations. The method assumes deterministic dynamics for the gate state transitions and closed-form solutions for the propagator under specific boundary conditions.  
DOMAIN: stochastic processes and diffusion models  
STRUCTURE: spectral or transform  
DATA_OBJECT: continuous function or field  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: estimation  
DISTRIBUTION: none  
COMPLEXITY: closed-form  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: mathematical-proof
