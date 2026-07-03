MECHANISM: The paper computes a penalized regression model that incorporates a moving-window smoothing penalty to identify genetic variants associated with a trait. The method minimizes a loss function combining a quadratic or logistic term with LASSO and smoothing penalties. The smoothing penalty enforces similarity in effect sizes across consecutive SNPs within a sliding window, weighted by linkage disequilibrium. For continuous traits, the loss function is quadratic, while for dichotomous traits, it uses logistic regression with iteratively reweighted least squares. The optimization employs coordinate descent, updating coefficients iteratively by solving a one-dimensional subproblem for each SNP. The smoothing penalty spans multiple SNPs, adjusting for correlations via LD measures. Tuning parameters are selected via bisection to control sparsity and window size. The algorithm alternates between updating regression coefficients and recalibrating working variables for logistic loss. The method balances sparsity (via LASSO) and smoothness (via window-based penalties) to improve power over traditional LASSO in GWAS.  
DOMAIN: genetic association analysis  
STRUCTURE: other: penalized regression with moving window  
DATA_OBJECT: set or table  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: estimation  
DISTRIBUTION: continuous: normal; binary: Bernoulli  
COMPLEXITY: polynomial iterative  
DATA_AVAILABILITY: public-benchmark-used  
CODE_AVAILABILITY: public-repository  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
