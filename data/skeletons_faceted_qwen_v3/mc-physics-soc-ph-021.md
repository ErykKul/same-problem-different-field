MECHANISM: The paper computes a Quadratic Unconstrained Binary Optimization (QUBO) model to solve the Capacitated Facility Location Problem (CFLP). The objective function combines three terms: a linear term maximizing total demand by summing selected demand scores, a quadratic term penalizing pairwise overlaps between selected nodes using an exponential decay function of distance, and a cardinality constraint enforcing exactly K hubs. The algorithm uses a hybrid quantum-classical approach with reverse annealing, starting from a greedy solution as a warm start, then partially melting the system state to induce superposition, followed by forward annealing to converge to low-energy states. The method samples 1000 solutions from the energy landscape to identify configurations minimizing overlap risk while maximizing demand. The QUBO matrix is constructed with parameters α, β, and γ to balance demand, overlap, and cardinality. The greedy heuristic selects top K nodes by demand alone, ignoring overlaps, while the exact solver uses Branch-and-Cut with auxiliary variables to linearize quadratic terms. The quantum-inspired method leverages simulated annealing to approximate quantum tunneling effects, exploring local neighborhoods around the greedy solution to avoid local optima. The solution is validated on a digital twin of Delhi NCR's road network, using shortest-path distances and simulated demand distributions.  
DOMAIN: supply chain optimization  
STRUCTURE: other: quadratic unconstrained binary optimization  
DATA_OBJECT: dense matrix  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: optimization  
DISTRIBUTION: none  
COMPLEXITY: combinatorial or NP-hard  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: simulation-study
