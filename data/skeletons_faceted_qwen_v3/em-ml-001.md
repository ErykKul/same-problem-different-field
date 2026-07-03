MECHANISM: The paper computes a clustering algorithm that merges variational EM with coreset approximations to reduce computational complexity. The method begins by approximating the full dataset with a weighted subset (coreset) to reduce the number of data points. It then applies truncated variational EM, which replaces full posterior probabilities with truncated distributions that consider only a subset of clusters per data point. The algorithm alternates between optimizing cluster parameters (M-step) and variational parameters (E-step). In the M-step, cluster means and variances are updated using weighted sums over the coreset data and truncated posteriors. In the E-step, the algorithm identifies the subset of clusters contributing most to each data point's likelihood, using pairwise distance comparisons to ensure the variational bound increases monotonically. The coreset construction and seeding are optimized separately, with lightweight coreset methods requiring two passes over the data and efficient seeding using Markov chains. The initial variance is estimated based on distances between data points and initial cluster centers. The overall process combines coreset reduction, truncated variational inference, and efficient parameter updates to achieve sublinear complexity in large-scale clustering.  
DOMAIN: clustering algorithms for Gaussian mixture models  
STRUCTURE: other: variational optimization with coreset approximation  
DATA_OBJECT: point set  
INFERENCE: variational  
PROBLEM_FORM: estimation  
DISTRIBUTION: continuous; continuous  
COMPLEXITY: not stated  
DATA_AVAILABILITY: public-repository  
CODE_AVAILABILITY: public-repository  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
