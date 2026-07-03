MECHANISM: Reconstruct the displacement between an initial near-uniform distribution of mass and an observed final distribution by solving a mass-conserving assignment that minimizes total squared displacement cost. The ill-posed inverse problem, in which intermediate velocities are unknown, is reduced to a well-posed convex assignment whose unique minimizer recovers the map from final positions back to initial positions. Solving the assignment yields the displacement field and hence the inferred initial configuration and the implied velocities at observation time. The strictly convex quadratic cost guarantees a unique optimal coupling, removing the non-uniqueness that defeats velocity-free reconstruction. The recovered initial state can be evolved forward and compared against observations to validate the model.
DOMAIN: cosmology
STRUCTURE: N-body or all-pairs
DATA_OBJECT: point set
INFERENCE: optimization only
PROBLEM_FORM: optimization
DISTRIBUTION: none
COMPLEXITY: polynomial iterative
DATA_AVAILABILITY: none
CODE_AVAILABILITY: none
PREREGISTRATION: none
EVIDENCE_BASIS: simulation-study
