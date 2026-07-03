MECHANISM: The paper computes a zeroth-order optimization algorithm for minimizing a functional over Gaussian probability measures. The algorithm operates on a system of interacting Gaussian particles, each represented by a mean vector and a covariance matrix. Particles evolve via consensus-based dynamics, where each particle's trajectory is influenced by a weighted barycenter of the ensemble, computed using a linearized Bures-Wasserstein geometry. The barycenter is determined by exponential weights derived from the objective functional. Stochastic exploration is introduced through Brownian processes in the linearized geometry, which perturb particle trajectories. The dynamics are governed by a combination of deterministic consensus forces and stochastic diffusion terms, with the latter scaled by the distance to the consensus point. The algorithm avoids degenerate covariance matrices by linearizing the geometry, enabling well-defined operations in a Hilbert space. Convergence is analyzed via a mean-field approximation, assuming propagation of chaos in the particle system. The method is gradient-free, requiring only evaluations of the objective functional, and is designed for non-convex optimization problems in low-dimensional spaces.  
DOMAIN: variational inference in probability spaces  
STRUCTURE: other: interacting particle system  
DATA_OBJECT: point set  
INFERENCE: optimization only  
PROBLEM_FORM: optimization  
DISTRIBUTION: continuous; continuous  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
