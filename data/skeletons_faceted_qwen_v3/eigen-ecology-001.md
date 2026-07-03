MECHANISM: The paper computes a centrality measure for nodes in a directed graph by decomposing flow through the network into boundary, direct, and indirect pathways. It constructs a matrix $\mathbf{F}$ representing flow quantities between nodes, derives a normalized direct flow intensity matrix $\mathbf{G}$, and computes the integral flow matrix $\mathbf{N}$ as the infinite sum of $\mathbf{G}^m$ for $m=0$ to $\infty$. This matrix captures all pathways, including indirect ones, by summing contributions across all path lengths. The integral matrix is calculated using the identity $(\mathbf{I}-\mathbf{G})^{-1}$, where $\mathbf{I}$ is the identity matrix. Node throughflow is then computed by multiplying $\mathbf{N}$ with an input vector $\mathbf{z}$, yielding total throughflow $\mathbf{T}$. Centrality measures are derived by normalizing row and column sums of $\mathbf{N}$, producing input centrality ($EC^{in}$), output centrality ($EC^{out}$), and their average ($AEC$). These metrics quantify a node's contribution to total system activity by aggregating flow intensities across all pathways. The method integrates transient and equilibrium dynamics by considering all path lengths and weights. It evaluates sensitivity by comparing $AEC$ across variations in flow distribution and demonstrates uniqueness by contrasting it with other centrality metrics like eigenvector and degree centrality. The approach uses matrix algebra, normalization, and summation over paths to estimate node importance in a network.  
DOMAIN: ecological network analysis  
STRUCTURE: spectral or transform  
DATA_OBJECT: dense matrix or tensor  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: estimation  
DISTRIBUTION: none  
COMPLEXITY: polynomial iterative  
DATA_AVAILABILITY: dataset-in-repository  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
