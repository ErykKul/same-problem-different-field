MECHANISM: The paper computes eigenvector centrality for each voxel in fMRI data by solving a generalized eigenvalue problem on a similarity matrix derived from pairwise correlations or spectral coherences between fMRI time series. The similarity matrix is constructed by calculating linear correlations or spectral coherences across all voxels in a region of interest, with no thresholding applied. The eigenvector centrality values are determined by iteratively applying the power method to the similarity matrix until convergence, with each voxel's centrality score reflecting its influence within the network. The method does not require parameter tuning or activation models, relying instead on the inherent structure of the similarity matrix. The algorithm is applied to fMRI data from subjects in different states (hunger vs. satiety), and the resulting centrality maps are analyzed to identify state-dependent changes in neural connectivity patterns. The approach is compared to betweenness centrality, which is computationally infeasible for large voxel sets due to its higher complexity. The method's efficiency stems from its linear algebraic formulation and avoidance of graph traversal or combinatorial operations. The paper demonstrates that eigenvector centrality captures intrinsic neural architecture at a voxel-wise resolution, enabling analysis of connectivity patterns across different spectral bands using spectral coherence metrics.  
DOMAIN: neuroimaging and network analysis  
STRUCTURE: spectral or transform  
DATA_OBJECT: dense matrix  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: estimation  
DISTRIBUTION: none  
COMPLEXITY: polynomial iterative  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-private-data
