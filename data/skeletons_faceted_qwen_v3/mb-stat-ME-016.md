MECHANISM: The paper computes a spatial scan statistic for categorical, functional data by first encoding categorical trajectories into real-valued vectors through functional multiple correspondence analysis. This involves maximizing a variance-based integral over time to derive orthogonal eigenvectors that capture temporal dependencies. The transformed data are then processed using a nonparametric scan statistic that computes multivariate ranks via a data-driven transformation matrix, ensuring spherical distribution of ranks. A concentration index is defined as a weighted sum of squared norms of rank means within and outside candidate clusters. The maximum value of this index across all potential clusters defines the scan statistic, which is evaluated using Monte Carlo random permutations to estimate p-values. The method simultaneously addresses functional dependencies, categorical outcomes, and spatial clustering without prior assumptions about cluster shape or location. The algorithm iteratively computes rank transformations, evaluates cluster statistics, and performs hypothesis testing through permutation-based inference. The process includes dimension reduction via eigenanalysis, rank normalization, and spatial scanning with circular window constraints. The final output includes the most likely cluster and its statistical significance.  
DOMAIN: spatial statistics, categorical data, functional data  
STRUCTURE: spectral or transform; map-reduce or embarrassingly-parallel  
DATA_OBJECT: categorical, functional data; real vectors  
INFERENCE: sampling or Monte-Carlo  
PROBLEM_FORM: detection or cluster identification  
DISTRIBUTION: categorical; continuous  
COMPLEXITY: not stated  
DATA_AVAILABILITY: public-benchmark-used  
CODE_AVAILABILITY: public-repository  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
