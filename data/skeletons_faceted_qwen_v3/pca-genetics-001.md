MECHANISM: The paper computes a statistical method to assess the fit of a model inferred by principal component analysis (PCA) or an admixture model. The method involves predicting genotype values based on the top principal components or admixture proportions, then calculating residuals as the difference between observed and predicted genotypes. Residuals are analyzed through their covariance and correlation matrices to detect model violations. Two measures are compared: an empirical covariance matrix derived from residuals and an estimated covariance matrix based on a model. Under the correct model, these measures converge as the number of SNPs increases. The method evaluates model fit by examining discrepancies between these matrices, which indicate violations of assumptions such as linear combinations of ancestral populations or independence of individuals. The approach applies to PCA and admixture models, using matrix projections, orthogonal decompositions, and statistical convergence properties. Theoretical guarantees are provided for the behavior of these measures under large SNP counts, including convergence of correlation matrices to specific forms. The method is computationally efficient, relying on fast PCA variants and avoiding expensive leave-one-out procedures. It identifies individuals or groups whose data deviate from the model assumptions by analyzing patterns in residual correlations.  
DOMAIN: population genetics  
STRUCTURE: dense linear algebra  
DATA_OBJECT: matrix  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: characterization  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-private-data
