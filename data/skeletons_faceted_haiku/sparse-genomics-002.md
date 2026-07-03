MECHANISM: A moving-window regularized regression method extends single-SNP smoothing to multi-SNP windows by penalizing differences in effect sizes across consecutive variables in genomic order. The method combines an MCP or LASSO selection penalty with a smoothing penalty that enforces similarity of absolute coefficients within sliding windows. The objective is minimized via coordinate descent, with window size chosen adaptively based on autocorrelation structure. This approach leverages sequential structure and linkage disequilibrium without requiring a priori grouping.
DOMAIN: Statistical genetics for genome-wide association studies
STRUCTURE: sparse linear algebra
DATA_OBJECT: sparse matrix
INFERENCE: frequentist point estimate
PROBLEM_FORM: prediction or classification
DISTRIBUTION: binary; frequentist assumptions
COMPLEXITY: polynomial iterative
