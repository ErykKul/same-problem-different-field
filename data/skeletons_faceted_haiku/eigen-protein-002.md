MECHANISM: Compute the allosteric signal propagation pathways in proteins by constructing an adjacency matrix from mutual information between amino-acid residue fluctuations obtained from molecular dynamics simulations; weight edges by generalized correlation coefficients and apply an exponential distance damping factor to control locality; compute the eigenvector corresponding to the largest eigenvalue of the adjacency matrix using eigendecomposition; visualize residue centrality coefficients to identify key nodes that act as channels for momentum transmission; compare centrality distributions between protein states (apo vs. ligand-bound) to reveal allosteric pathways.
DOMAIN: Biochemistry, protein dynamics
STRUCTURE: spectral or transform
DATA_OBJECT: sparse matrix
INFERENCE: deterministic or closed-form
PROBLEM_FORM: characterization
DISTRIBUTION: none
COMPLEXITY: polynomial iterative
