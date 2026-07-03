MECHANISM: A language model agent (MoCo-Agent) iteratively generates metaheuristic algorithms in Python code to solve cardinality-constrained portfolio optimization. The process uses reasoning-action iterations: the agent receives engineered prompts including problem formulation, role assignment, and I/O specifications, plus feedback from the previous iteration's best algorithm (score, feasibility, errors). The agent generates a new algorithm; this is executed across a discretized weight simplex (sweeping trade-off ratios between return and risk objectives). Solutions are extracted as non-dominated points (Pareto front), scored via inverted generation distance (IGD) against a theoretical optimal frontier, and the best-scoring algorithm is retained. This cycles for T iterations, accumulating diverse algorithms into a portfolio.
DOMAIN: Portfolio optimization and combinatorial optimization via LLM agents
STRUCTURE: dynamic programming
DATA_OBJECT: dense matrix or tensor
INFERENCE: optimization only
PROBLEM_FORM: optimization
DISTRIBUTION: continuous
COMPLEXITY: combinatorial or NP-hard
