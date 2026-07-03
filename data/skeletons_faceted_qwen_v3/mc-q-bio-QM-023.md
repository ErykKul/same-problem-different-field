MECHANISM: The paper computes a two-stage factor analysis with Procrustes rotation to reduce high-dimensional time series data into interpretable latent factors for multivariate genomic prediction. First, it decomposes phenotypic data into genetic and residual components, estimating genetic covariance matrices for each timepoint. These matrices are then used to derive factor loadings and factor scores via a probabilistic model assuming multivariate normality. The factor loadings are rotated using Varimax to enhance interpretability, followed by Procrustes rotation to align factor structures across timepoints to a biologically relevant reference. Factor scores are estimated through a modified Thomson regression, incorporating residual covariance adjustments. These scores are then selected using the Bayesian Information Criterion and integrated into a multivariate genomic prediction model to improve predictive accuracy. The method emphasizes consistency across timepoints through rotational alignment and leverages both domain knowledge and data-driven criteria for factor selection. The computational steps involve matrix decomposition, eigenvalue estimation, orthogonal transformations, and optimization-based subset selection. The final model combines latent factors with genetic markers to predict a focal trait, using a structured approach that balances dimensionality reduction with biological interpretability.  
DOMAIN: plant breeding and genomic prediction  
STRUCTURE: other: factor analysis with Procrustes rotation  
DATA_OBJECT: dense matrix  
INFERENCE: optimization only  
PROBLEM_FORM: prediction or classification  
DISTRIBUTION: continuous; multivariate normal  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-private-data
