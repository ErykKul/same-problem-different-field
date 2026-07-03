MECHANISM: The paper computes the number of subpopulations in a dataset by analyzing the eigenvalues of an uncentered sample covariance matrix derived from biallelic genetic marker data. The matrix is constructed with rows representing individuals and columns representing markers, where each entry indicates the number of variant alleles. The method relies on asymptotic analysis as the number of individuals (M) and markers (N) grow large. The key steps involve deriving the theoretical behavior of the eigenvalues of the matrix CC', identifying a threshold based on M and N to distinguish large eigenvalues (corresponding to population structure) from smaller ones (attributed to random noise), and showing that the number of large eigenvalues above this threshold estimates the number of subpopulations (K). The threshold depends on parameters like F (inbreeding coefficient) and the relative subpopulation sizes. The analysis assumes independence among markers and individuals, and derives the asymptotic distribution of eigenvalues without centering or normalization. The method is validated through simulations and applied to real genotype data, demonstrating that sufficient sample size ensures strong separation between large and small eigenvalues, enabling accurate estimation of K. The mathematical model uses moments of allele frequencies and derives a deterministic relationship between eigenvalues and subpopulation parameters, avoiding assumptions about specific distributions of allele frequencies.  
DOMAIN: population genetics  
STRUCTURE: dense linear algebra  
DATA_OBJECT: dense matrix  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: estimation  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: simulation-study
