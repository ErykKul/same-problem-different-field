MECHANISM: The paper computes the separation of the largest eigenvalues from the covariance matrix of a genotype matrix derived from biallelic genetic marker data. The method involves constructing a matrix where rows represent individuals and columns represent genetic markers, with entries encoding allele frequencies. The covariance matrix is then computed, followed by eigenvalue decomposition to identify principal components. The largest eigenvalues are analyzed to infer the number of discrete subpopulations present in the dataset. The mathematical analysis quantifies how the signal-to-noise ratio in eigenvalues depends on the number of individuals genotyped versus the number of markers. The technique assumes that genetic drift and admixture patterns create distinct eigenvectors corresponding to subpopulation structure. The separation of eigenvalues is interpreted as a measure of population differentiation, with larger gaps indicating more distinct subpopulations. The paper derives theoretical bounds on the detectability of subpopulations based on the effective sample size and marker density. No probabilistic modeling or optimization is performed; the method relies purely on linear algebraic operations and spectral analysis of the genotype matrix. The results are validated through mathematical proofs rather than empirical experiments.  
DOMAIN: genetics and population structure analysis  
STRUCTURE: dense linear algebra  
DATA_OBJECT: dense matrix  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: estimation  
DISTRIBUTION: none  
COMPLEXITY: closed-form  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: mathematical-proof
