MECHANISM: Layer-wise capacity allocation is formulated as a convex optimization problem driven by curvature-adjusted layer gains equal to the Hessian-weighted gradient norm. This quantity represents twice the maximal second-order risk reduction achievable by updating each layer alone. Normalized quality scores are computed from these gains. Two complementary convex programs follow: capacity allocation distributes additional resources (LoRA rank, expert slots) preferentially to high-quality layers under a budget constraint using curvature-weighted water-filling with closed-form solution via log-returns penalty; pruning concentrates sparsity on low-quality layers while protecting high-quality layers under a global sparsity target. Both problems are solved via bisection on dual variables in O(K log 1/epsilon) time.

DOMAIN: large language models, model optimization, capacity allocation

STRUCTURE: sparse linear algebra

DATA_OBJECT: sparse matrix

INFERENCE: optimization only

PROBLEM_FORM: optimization

DISTRIBUTION: not stated

COMPLEXITY: polynomial iterative
