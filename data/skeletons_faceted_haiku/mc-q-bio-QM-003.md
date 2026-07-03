MECHANISM: Apply Good-Turing statistical methods to molecular dynamics simulation trajectories to estimate the probability of observing completely new (previously unobserved) molecular configurations. For each trajectory, compute pairwise root-mean-square deviations (RMSD) between all structures, identify frequency distributions of unique and rare configurations, and use Good-Turing smoothing to estimate probabilities for unobserved configurations. The improved algorithm scales linearly with trajectory length by computing RMSD incrementally without storing the full matrix.
DOMAIN: Molecular dynamics simulation and convergence analysis
STRUCTURE: Other: statistical frequency estimation
DATA_OBJECT: Sequence or time-series
INFERENCE: Frequentist point estimate
PROBLEM_FORM: Estimation
DISTRIBUTION: none
COMPLEXITY: not stated
