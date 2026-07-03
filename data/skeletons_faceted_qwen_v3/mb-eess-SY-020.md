MECHANISM: The paper computes a novel metric, the Generalized Fiedler Vector (GFV), by solving a generalized eigenvalue problem that integrates network topology and nodal inertia. The process begins by constructing a Laplacian matrix from the system's connectivity, then calculating nodal inertia values based on generator parameters and network susceptances. These inertia values form a diagonal matrix, which is combined with the Laplacian to define a generalized eigenvalue problem. The GFV is derived from the normalized eigenvector associated with the smallest nonzero eigenvalue of this problem. This eigenvector quantifies dynamic connectivity by encoding how inertia distribution and network structure influence frequency deviations. The method uses spectral decomposition to relate frequency responses to eigenvalues and eigenvectors, incorporating both local inertia and topological properties. The GFV identifies nodes with higher resilience to stochastic disturbances by mapping inertia heterogeneity and connectivity patterns. The computation involves matrix operations, eigenvalue decomposition, and normalization steps, all performed deterministically without probabilistic assumptions. The metric is validated through simulations that model stochastic variations in power injections and analyze frequency responses across the network.  
DOMAIN: power system dynamics  
STRUCTURE: spectral or transform  
DATA_OBJECT: sparse matrix  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: characterization  
DISTRIBUTION: none  
COMPLEXITY: polynomial iterative  
DATA_AVAILABILITY: public-benchmark-used  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
