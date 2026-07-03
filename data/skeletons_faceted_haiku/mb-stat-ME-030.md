MECHANISM: Learn a directed acyclic graph (DAG) structure representing conditional dependencies among random variables from observational data. Formulate as a combinatorial search problem over the DAG space constrained by acyclicity. Use a score-based algorithm (e.g., A* search, greedy equivalence search) optimizing a criterion (BIC, BDe). Alternatively, solve a continuous relaxation via differentiable acyclic constraint to make the problem tractable. Identify the learned edges and estimate strength via coefficients. Evaluate identifiability under model assumptions.
DOMAIN: Causal discovery and structure learning
STRUCTURE: other: combinatorial search
DATA_OBJECT: graph or network
INFERENCE: frequentist point estimate
PROBLEM_FORM: search
DISTRIBUTION: none
COMPLEXITY: combinatorial or NP-hard
