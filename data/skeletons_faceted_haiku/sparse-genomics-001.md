MECHANISM: A weighted regularized regression framework combines multiple data modalities by assigning different L1 penalties to coefficient blocks from different data sources. The optimization problem minimizes a quadratic loss plus a weighted sum of L1-norms across modalities. For computational efficiency, the problem is reformulated by variable rescaling to reduce to standard LASSO with transformed predictors. This approach generalizes LASSO to handle heterogeneous data modalities with different relevance levels, using a two-stage cross-validation to select both the penalty parameters and the regularization strength.
DOMAIN: Statistical machine learning for prediction with multi-modal biomedical data
STRUCTURE: sparse linear algebra
DATA_OBJECT: sparse matrix
INFERENCE: frequentist point estimate
PROBLEM_FORM: prediction or classification
DISTRIBUTION: binary; frequentist assumptions
COMPLEXITY: polynomial iterative
