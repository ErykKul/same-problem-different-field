MECHANISM: The paper computes a threshold value $ r_c $ by analyzing the structure of correlation matrices derived from time-series data. The method involves thresholding the correlation matrix to probe connectivity, treating this as a percolation-like process. Multiple cluster- and network-level observables (e.g., cluster size, number of clusters, and network properties) are tracked as the threshold $ r $ varies. The threshold $ r_c $ is identified as the value where these observables converge or exhibit a peak, indicating a critical transition in the network structure. This $ r_c $ is then used as a descriptor of the underlying dynamical state of the system. The method is applied to empirical data (e.g., fMRI time-series) and validated through numerical simulations of models with known critical behavior (e.g., the GH model and Ising model). The computation involves matrix operations (e.g., correlation matrix construction), thresholding, and statistical analysis of cluster properties. Alternative definitions of $ r_c $ are explored, including measures based on degree distribution, coefficient of variation, and cluster size distribution. The method is shown to relate to standard percolation theory through analytical approximations and empirical comparisons. The paper also derives mathematical relationships between Pearson correlation and time autocorrelation in the context of dynamic models, such as VAR(1), to support the theoretical underpinnings of the method.  
DOMAIN: neuroscience and brain dynamics  
STRUCTURE: other: percolation-based network analysis  
DATA_OBJECT: dense matrix  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: estimation  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: public-benchmark-used  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
