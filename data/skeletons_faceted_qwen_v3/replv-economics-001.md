MECHANISM: The paper computes the dynamic behavior of a game system using a velocity vector field defined by differential equations. It linearizes the system near a Nash equilibrium, computes the Jacobian matrix, and derives eigenvalues and eigenvectors to analyze stability and invariant manifolds. The eigenvectors are used to construct eigencycles, which quantify cyclic motion in the system. These eigencycles are calculated using amplitude and phase differences between eigenvector components. The method identifies rotation axes by projecting eigen-trajectories onto 2D subspaces, leveraging the constraint that strategy probabilities sum to one. Theoretical predictions are validated against human subject experiments and agent-based simulations by comparing eigencycle values and rotation axis directions. The analysis involves solving linear systems, matrix diagonalization, and statistical correlation of time-series data to test invariance properties under parameter changes.  
DOMAIN: evolutionary game theory  
STRUCTURE: dense linear algebra  
DATA_OBJECT: dense matrix  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: simulation or generation  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-private-data
