MECHANISM: The paper computes a statistical assessment of the fit of principal component analysis (PCA) and admixture models to genetic data. It uses the top principal components from PCA as a linear model to predict individual genotypes, then calculates residuals as the difference between observed and predicted genotypes. The method evaluates the covariance and correlation of these residuals to detect violations of model assumptions, such as non-linear relationships or outliers. For admixture models, the same approach applies, where the mean of the data is represented by linear matrix decomposition. The process involves projecting genetic data onto principal components, performing linear regression to predict genotypes, and analyzing residual statistics to quantify model misfit. The method is applied to both simulated and real genome-wide human data to validate its effectiveness. It identifies individuals whose genotypes are poorly explained by the chosen principal components, aiding in the interpretation of population structure. The approach is generalizable to other linear models that decompose data into low-rank components. The computational steps include matrix decomposition, regression, and statistical testing on residual covariance. The method does not rely on probabilistic assumptions but instead uses deterministic calculations of variance and correlation. The results guide the selection of appropriate models for population structure inference.  
DOMAIN: genetics and population structure  
STRUCTURE: dense linear algebra  
DATA_OBJECT: dense matrix  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: estimation  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: public-benchmark-used  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
