MECHANISM: The problem selects a subset of nodes in a network to maximize mutual information with an outcome (prevalence or outbreak size). The method defines mutual information as I(X_A; Z) where X_A represents states of chosen nodes and Z is a weighted sum of infection states. The objective is NP-hard to approximate. For special network classes (trees, paths, 1-hop models), the conditional entropy H(Z|X_A) can be computed exactly using dynamic programming techniques. For general networks, a greedy sampling-based algorithm GreedyMI iteratively adds nodes that minimize conditional entropy, using cascade simulations to estimate the mutual information function.
DOMAIN: Disease surveillance, epidemic prediction, information theory on networks
STRUCTURE: graph traversal
DATA_OBJECT: graph or network
INFERENCE: bootstrap or resampling
PROBLEM_FORM: optimization
DISTRIBUTION: continuous; none
COMPLEXITY: NP-hard
