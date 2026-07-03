MECHANISM: Verify asymptotic stability of switched systems with state-dependent mode transitions by constructing multiple Lyapunov functions using neural networks. For each system mode, train a neural network to approximate a Lyapunov function satisfying two conditions: (1) the function decreases along mode-specific trajectories in its domain region, (2) the function value decreases when the system switches to a new mode. Employ a counter-example guided inductive synthesis loop: sample regions where conditions are violated, add these examples to the training set, and retrain until all conditions are satisfied. Handle both continuous-time and discrete-time dynamics.
DOMAIN: Nonlinear systems and stability analysis
STRUCTURE: other: neural network-based verification with synthesis
DATA_OBJECT: continuous function or field
INFERENCE: deterministic or closed-form
PROBLEM_FORM: proof or characterization
DISTRIBUTION: none
COMPLEXITY: not stated
