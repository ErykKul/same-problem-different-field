MECHANISM: A cell perturbation modeling framework addresses heterogeneity through two mechanisms. First, an LLM-driven semantic unifier maps incompatible metadata schemas across datasets to a canonical ontology. Second, an adaptive Monte Carlo tree search explores a hierarchical space of neural network architectures to automatically select models with appropriate inductive biases for statistical distribution shifts. The search procedure samples candidate architectures, evaluates them on validation data, and updates search statistics to guide the exploration toward architectures that generalize across datasets. The framework integrates both mechanisms into an agent loop that iterates over metadata reconciliation and architecture selection.
DOMAIN: single-cell biology and perturbation modeling
STRUCTURE: backtracking or branch-and-bound
DATA_OBJECT: dense matrix or tensor
INFERENCE: sampling or Monte-Carlo
PROBLEM_FORM: prediction or classification
DISTRIBUTION: none
COMPLEXITY: not stated
