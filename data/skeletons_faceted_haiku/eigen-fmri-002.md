MECHANISM: Compute the functional centrality of brain voxels in resting-state fMRI networks by constructing a similarity matrix of pairwise correlations (or spectral coherences) between time series; compute the dominant eigenvector of the similarity matrix (the eigenvector corresponding to the largest eigenvalue) using the power iteration method; the eigenvector components represent centrality scores for each voxel, where higher scores indicate voxels that are highly connected to other well-connected voxels; aggregate voxel-wise centrality values to generate brain maps revealing network organization.
DOMAIN: Neuroscience, functional connectivity
STRUCTURE: spectral or transform
DATA_OBJECT: dense matrix or tensor
INFERENCE: deterministic or closed-form
PROBLEM_FORM: ranking or retrieval
DISTRIBUTION: none
COMPLEXITY: polynomial iterative
