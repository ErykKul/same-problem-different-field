MECHANISM: Decompose a long-horizon sequential decision task into two levels: first, search over a semantic space to generate a high-level plan (blueprint) that breaks the task into sub-goals; second, condition an action policy on the selected blueprint to execute atomic actions. Optimize the planner and executor without value networks using group-relative advantages computed within level-specific cohorts. Stabilize the bi-level learning by alternating between fixing the executor and updating the planner, then fixing a high-confidence plan and updating the executor.
DOMAIN: Reinforcement learning, LLM agents, hierarchical control, long-horizon planning
STRUCTURE: dynamic programming
DATA_OBJECT: sequence or time-series
INFERENCE: frequentist point estimate
PROBLEM_FORM: decision or test
DISTRIBUTION: continuous; continuous
COMPLEXITY: convergence rate
