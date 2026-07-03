MECHANISM: Factor analysis decomposes a correlation matrix R into a low-rank product: R ≈ Λ Ψ Λ' + Θ, where Λ is a p×m matrix of factor loadings, Ψ is an m×m interfactor correlation matrix, and Θ is a p×p diagonal matrix of unique factor variances. The algorithm fits a linear latent variable model: y = Λη + ε, where y is a vector of observed variables, η is a vector of m unobserved common factors, and ε is a vector of unique factors. Parameters are estimated using maximum likelihood or unweighted least squares to minimize discrepancy between observed and model-implied correlations. In factor analysis of categorical items (Likert-type), polychoric correlations replace product-moment correlations to account for ordinality. The method includes data screening (outliers, multivariate normality, missing data) and assumption testing (factorability of correlation matrix, correlations among residuals).
DOMAIN: Psychometrics and factor analysis
STRUCTURE: dense linear algebra
DATA_OBJECT: dense matrix or tensor
INFERENCE: frequentist point estimate
PROBLEM_FORM: estimation
DISTRIBUTION: none
COMPLEXITY: not stated
