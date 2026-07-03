MECHANISM: The task is to approximate the trade-off surface of a constrained selection problem in which a quadratic cost and a linear gain are jointly optimized over weights on a fixed-size subset of items, with binary inclusion indicators, a budget equality, a fixed-cardinality equality, and per-item bounds. Because the integer-constrained quadratic problem is intractable, the two objectives are scalarized by a convex weight and the scalar weight is swept across the unit interval to trace candidate trade-off points. For each weight, an approximate solver returns a feasible selection; solutions are pooled across weights and the dominated ones are discarded to extract the nondominated frontier. Frontier quality is scored against a reference unconstrained frontier by an averaged nearest-distance metric capturing both proximity and spread, and by a per-weight deviation metric. The approximate solvers themselves are produced by an iterative generate-evaluate loop: a language model is prompted with the formulation, role, and prior best solver plus its feedback and score, emits code, the code is executed and scored externally, and the best-scoring variant is fed back greedily. Multiple solver families are generated this way, pruned on a training instance, and the survivors are pooled; pooling diverse solvers improves frontier coverage.
DOMAIN: portfolio selection in finance
STRUCTURE: numerical optimization
DATA_OBJECT: set or table
INFERENCE: deterministic optimization
PROBLEM_FORM: optimization
DISTRIBUTION: continuous; none
COMPLEXITY: combinatorial or NP-hard
