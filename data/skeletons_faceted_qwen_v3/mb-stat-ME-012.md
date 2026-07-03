MECHANISM: The paper computes a semiparametric two-component mixture model to estimate the distribution of z-scores derived from gene expression data. The null component is a standard normal distribution, while the alternative component is a skew-normal scale mixture with an unspecified mixing distribution over scale parameters. The model accommodates skewness and heavy tails by integrating a nonparametric maximum likelihood estimator (NPMLE) for the scale distribution. The algorithm iteratively estimates parameters using an expectation-conditional maximization (ECM) approach, alternating between computing posterior probabilities for each observation (E-step) and updating the scale distribution and finite-dimensional parameters (C-step). The NPMLE for the scale distribution is derived via directional derivatives and optimality conditions, ensuring consistency under mild regularity assumptions. The model's identifiability is established through linear independence between the null and alternative components, and the estimation procedure avoids restrictive parametric assumptions on the alternative distribution. The method is applied to estimate the proportion of null genes, location shift, skewness parameter, and the nonparametric scale distribution, enabling probabilistic inference for differential expression.  
DOMAIN: statistical modeling of gene expression  
STRUCTURE: other: mixture model  
DATA_OBJECT: point set  
INFERENCE: optimization only  
PROBLEM_FORM: estimation  
DISTRIBUTION: continuous; continuous  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
