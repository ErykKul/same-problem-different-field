MECHANISM: For each of 6 single-cell genomics datasets, apply combinations of preprocessing steps: (1) normalize expression matrices using one of 7 methods, (2) reduce dimensionality using one of 4 methods, (3) integrate data from multiple batches using one of 5 methods. For each combination, compute three clustering quality metrics: Silhouette Coefficient, Adjusted Rand Index, and Calinski-Harabasz Index. Compare 140 total combinations across dataset types and sizes; recommend best algorithm combinations per dataset class.
DOMAIN: Single-cell genomics data integration
STRUCTURE: Map-reduce or embarrassingly-parallel
DATA_OBJECT: Dense matrix or tensor
INFERENCE: Deterministic or closed-form
PROBLEM_FORM: Decision or test
DISTRIBUTION: none
COMPLEXITY: not stated
