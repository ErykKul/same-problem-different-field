MECHANISM: The paper computes an adaptive control strategy for stabilizing power grids using a reinforcement learning (RL) algorithm. The method operates on a graph representation of the grid, where nodes represent buses and edges represent transmission lines. The algorithm processes a state vector containing inertia, damping coefficients, power injections, angular positions, velocities, and admittance values. A graph neural network (GNN) with Chebyshev convolution layers transforms node features into high-dimensional representations, enabling long-range interactions. For each transmission line, the policy network outputs a binary control decision (whether to adjust admittance) and a Gaussian-distributed adjustment magnitude. During training, control decisions are sampled from a Bernoulli distribution parameterized by the GNN's output, while evaluation uses deterministic values. The algorithm's objective is to minimize frequency fluctuations and power flow deviations after line faults, measured as inertia-weighted variance and steady-state power flow differences. The control policy is trained through episodes where a single action is taken per fault event, with rewards based on stabilization metrics. The method identifies critical lines for regulator placement by analyzing the frequency of control actions and adjustment magnitudes across fault scenarios. It demonstrates that selective intervention on a small subset of lines achieves near-optimal stabilization while reducing deployment costs. The algorithm's effectiveness is validated through simulations on a UK power grid model and synthetic grids, showing significant reductions in frequency deviations and power flow instability.  
DOMAIN: power systems  
STRUCTURE: other: reinforcement learning  
DATA_OBJECT: graph or network  
INFERENCE: sampling or Monte-Carlo  
PROBLEM_FORM: control  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: simulation-study
