MECHANISM: The paper computes a method to explore the Pareto front in multi-objective optimization by leveraging intermediate quantum states during a quantum annealing process. The method begins with initializing a quantum state in a superposition of all possible solutions. A time-dependent Hamiltonian is applied to evolve the state toward the ground state, which corresponds to an optimal solution. At specified mid-anneal times, the quantum state is measured, producing a set of intermediate solutions. These measurements are repeated across multiple annealing runs to collect a distribution of solutions. The timing of measurements is varied to control the trade-off between solution diversity and convergence to non-dominated solutions. Earlier measurement times yield a broader distribution of solutions, while later times focus on refining solutions toward the Pareto front. The method combines physical experiments using quench-based readout with numerical simulations that assume ideal mid-anneal measurements. Both approaches validate the effectiveness of the timing strategy in balancing diversity and convergence. The results are analyzed to identify a practical compromise timing that optimally balances these metrics. The method does not explicitly solve for the Pareto front but instead samples it through controlled measurement timing. The computational steps involve quantum state evolution, measurement, and statistical analysis of the resulting solution distributions.  
DOMAIN: quantum computing and multi-objective optimization  
STRUCTURE: simulation or generation  
DATA_OBJECT: sequence or time-series  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: optimization  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-private-data
