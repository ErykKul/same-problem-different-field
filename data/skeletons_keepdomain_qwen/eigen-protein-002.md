MECHANISM: The paper constructs a graph where nodes represent amino acids and edges are weighted by mutual information derived from molecular dynamics simulations. It computes eigenvector centrality by solving the principal eigenvector of the adjacency matrix, which quantifies the influence of each residue in the network. A novel centrality metric is introduced, measuring the relevance of a residue's neighborhood through a modified eigenvector calculation. The method identifies key residues in allosteric pathways by analyzing the eigenvector components corresponding to the largest eigenvalue. The approach is validated by comparing predicted residue importance with experimental NMR data on imidazol glycerol phosphate synthase (IGPS). The algorithm involves matrix diagonalization, eigenvalue decomposition, and thresholding of mutual information values to construct the graph. No probabilistic or stochastic elements are involved; the computation is purely algebraic and deterministic. The method does not involve optimization or iterative refinement beyond the eigenvalue calculation. The resulting centrality scores are used to map momentum transfer pathways in the protein. The technique is applied to a single case study (IGPS) but is presented as a generalizable framework for allosteric analysis.  
DOMAIN: protein allosteric pathways  
STRUCTURE: spectral or transform  
DATA_OBJECT: graph or network  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: characterization  
DISTRIBUTION: none  
COMPLEXITY: polynomial iterative  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-private-data
