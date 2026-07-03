MECHANISM: The paper constructs a stochastic model to simulate the distribution of wealth among agents in a society. Agents are initialized with random wealth values, and their interactions are governed by probabilistic rules that mimic economic behaviors such as income generation, savings, and wealth transfers. At each time step, agents receive random income shocks drawn from a specified distribution, and a fraction of their income is saved, while the remainder is spent or redistributed. The model incorporates parameters such as the saving rate, the variance of income shocks, and the number of agents. Over time, the wealth distribution is tracked by aggregating the wealth of all agents and analyzing its statistical properties. The model is run multiple times with different parameter values to explore how these factors influence the shape of the wealth distribution. The paper compares the simulated distributions to empirical data from real-world wealth distributions, using goodness-of-fit measures to evaluate the model's accuracy. The stochastic nature of the model allows for the exploration of uncertainty in wealth dynamics, and the results are used to infer the underlying mechanisms that generate observed wealth inequality. The model does not explicitly solve for equilibrium but instead focuses on the transient and long-term behavior of wealth distribution under varying conditions. The computational steps involve initializing the agent population, iterating the simulation over time steps, updating agent wealth based on stochastic rules, and aggregating results for analysis. The model's output is a time series of wealth distributions, which are compared to empirical data to validate the theoretical framework.

DOMAIN: economics and econophysics

STRUCTURE: other: agent-based simulation

DATA_OBJECT: set or table

INFERENCE: sampling or Monte-Carlo

PROBLEM_FORM: simulation or generation

DISTRIBUTION: continuous; Pareto or log-normal

COMPLEXITY: not stated

DATA_AVAILABILITY: none

CODE_AVAILABILITY: none

PREREGISTRATION: none

EVIDENCE_BASIS: simulation-study
