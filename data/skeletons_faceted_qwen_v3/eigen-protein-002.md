MECHANISM: The paper constructs a graph where nodes represent entities and edges represent pairwise correlations derived from mutual information between entities. The adjacency matrix is defined with weights based on mutual information and an exponential damping factor to control locality. The eigenvector centrality (EC) is computed as the leading eigenvector of the adjacency matrix, reflecting the importance of nodes in the network. The EC values are compared across different damping parameters to analyze the role of short- and long-range correlations. The method also introduces a neighborhood centrality measure by subtracting degree centrality from EC values. The analysis involves diagonalizing the adjacency matrix or using the power method for efficiency. The EC distribution is compared to essential dynamics (ED) methods, which use covariance matrices instead of mutual information. The paper validates the approach against experimental NMR data and demonstrates how effector binding alters the EC distribution, revealing allosteric pathways. The locality parameter λ is adjusted to isolate short-range interactions, and long-range contributions are quantified by comparing EC values at different λ thresholds. The method identifies key residues and their neighborhoods as targets for mutagenesis based on changes in centrality.  
DOMAIN: protein structure analysis  
STRUCTURE: spectral or transform  
DATA_OBJECT: graph or network  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: characterization  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
