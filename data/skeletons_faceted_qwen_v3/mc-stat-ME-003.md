MECHANISM: The paper computes a semi-parametric quasi-likelihood estimator for correlation and covariance using rank-based transformations of observed pairs. It begins by constructing centred score matrices from pairwise comparisons, where each element is +1, -1, or 0 based on relative ordering. These matrices are embedded into a Hilbert space via a Whitney embedding, transforming them into vectors. The correlation estimator is derived from the inner product of these vectors, normalized by their sample variances. The framework incorporates higher-order central moments (second, third, and fourth) of the transformed data to construct a quasi-likelihood function, which is optimized by solving equations derived from the log-likelihood and its derivatives. The estimator is shown to be unbiased and asymptotically normal, with consistency guaranteed by the sub-Gaussian properties of the rank-transformed data. The method extends classical rank-based inference to multivariate settings while preserving exact unbiasedness under linear mappings. The quasi-likelihood function is parameterized by weights for the moments, and optimization involves computing gradients and Hessians of the log-likelihood with respect to these weights. The approach ensures finite-sample unbiasedness and asymptotic efficiency by leveraging the Cramér-Rao bound and properties of the Fisher information matrix.  
DOMAIN: statistical inference  
STRUCTURE: other: quasi-likelihood optimization  
DATA_OBJECT: score matrix  
INFERENCE: frequentist point estimate  
PROBLEM_FORM: estimation  
DISTRIBUTION: continuous; sub-Gaussian  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: mathematical-proof
