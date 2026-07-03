MECHANISM: The facility location problem is reformulated as a Quadratic Unconstrained Binary Optimization (QUBO) model and solved via three algorithms: greedy heuristics, exact branch-and-bound solvers, and quantum-inspired reverse annealing. The objective function combines linear demand maximization and quadratic overlap penalty terms using a spatial decay function. A digital twin of an urban road network (via OpenStreetMap and Dijkstra's shortest paths) provides realistic distance metrics. Quantum-inspired reverse annealing begins from a warm start (greedy solution), induces partial superposition, then forward anneals toward ground state, sampling final configurations to identify near-optimal facility selections.
DOMAIN: Supply chain optimization, facility location, quantum computing in logistics
STRUCTURE: backtracking or branch-and-bound
DATA_OBJECT: graph or network
INFERENCE: optimization only
PROBLEM_FORM: optimization
DISTRIBUTION: none
COMPLEXITY: combinatorial or NP-hard
