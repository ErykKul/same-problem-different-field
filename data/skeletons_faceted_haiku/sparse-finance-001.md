MECHANISM: Given asset return estimates and transaction costs, solve robust mean-variance portfolio selection by minimizing risk-aversion-weighted variance plus worst-case value-at-risk term plus fixed transaction costs (indicator function penalty on non-zero weights). Formulate as a difference-of-convex (DC) optimization problem and solve via proximal DC algorithm with semismooth Newton subproblems.
DOMAIN: Finance; portfolio optimization; robust optimization
STRUCTURE: Sparse linear algebra or other: difference-of-convex optimization
DATA_OBJECT: Dense matrix (covariance, returns)
INFERENCE: None
PROBLEM_FORM: Optimization
DISTRIBUTION: None
COMPLEXITY: NP-hard (combinatorial cardinality constraint)
