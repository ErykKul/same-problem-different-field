MECHANISM: A parameter-efficient fine-tuning method for large language models implements three coupled techniques to make low-rank adaptation curvature-aware. First, K-FAC (Kronecker-Factored Approximate Curvature) applies natural-gradient preconditioning within the low-rank subspace to suppress updates along sharp curvature directions. Second, periodic neural reprojection aligns the low-rank basis onto dominant Fisher eigendirections to suppress drift and remove low-energy directions. Third, dynamic rank adaptation allocates effective rank by reading the Fisher spectrum so capacity concentrates in high-signal, low-interference directions. Training balances task loss with curvature regularization.
DOMAIN: parameter-efficient fine-tuning, large language models
STRUCTURE: other: curvature-aware low-rank optimization
DATA_OBJECT: dense matrix or tensor
INFERENCE: optimization only
PROBLEM_FORM: optimization
DISTRIBUTION: none
COMPLEXITY: polynomial iterative
