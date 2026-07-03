MECHANISM: A matrix factorization decomposes an observation matrix into a sum of two components: a low-rank matrix and a sparse matrix. Convex optimization minimizes a penalized objective combining a data fitting term with a nuclear norm penalty (inducing low rank) and an L1 sparsity penalty. Alternating proximal algorithms solve for each component given the other until convergence.
DOMAIN: Robust principal component analysis
STRUCTURE: sparse linear algebra
DATA_OBJECT: sparse matrix
INFERENCE: optimization only
PROBLEM_FORM: optimization
DISTRIBUTION: none
COMPLEXITY: polynomial iterative
