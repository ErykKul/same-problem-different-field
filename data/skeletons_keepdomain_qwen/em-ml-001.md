MECHANISM: The paper computes a clustering algorithm for isotropic Gaussian mixture models (GMMs) using a truncated variational EM approach combined with coreset-based approximation. The algorithm begins by initializing cluster centroids via efficient seeding, then constructs a coreset by sampling data points with probabilities proportional to their influence on the clustering objective. The truncated variational EM step estimates GMM parameters by optimizing a variational lower bound on the log-likelihood, with truncation applied to reduce computational complexity for large numbers of clusters. The coreset is then used to assign data points to clusters via a final clustering step, leveraging the reduced complexity of the coreset. The method explicitly models the data as a point set, with cluster assignments determined by maximizing the variational lower bound under isotropic Gaussian assumptions. The algorithm's efficiency arises from both the coreset construction (reducing data size) and the truncation of variational updates (reducing per-iteration complexity). The paper evaluates the method on standard large-scale clustering benchmarks and demonstrates wall-clock speedups compared to existing approaches. The coreset construction and seeding steps are designed to translate theoretical sublinear complexity guarantees into practical computational gains. The method does not assume diagonal covariance matrices in this version, focusing instead on isotropic clusters. The final clustering step uses the coreset to approximate the full dataset's cluster assignments without reprocessing all data points.  
DOMAIN: clustering with Gaussian mixture models  
STRUCTURE: other: variational EM with coreset-based approximation  
DATA_OBJECT: point set  
INFERENCE: Bayesian posterior  
PROBLEM_FORM: estimation  
DISTRIBUTION: discrete (cluster labels) and Gaussian  
COMPLEXITY: sublinear complexity  
DATA_AVAILABILITY: public-repository  
CODE_AVAILABILITY: public-repository  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
