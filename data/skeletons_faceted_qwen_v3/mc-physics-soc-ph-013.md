MECHANISM: The paper computes a hierarchical system of equations derived from marginal probabilities of states in a networked agent model. Each agent is represented as a node in a graph, with states evolving via stochastic transitions governed by infection and recovery events. Indicator functions are used to define the state of each node, and ensemble averages of products of these indicators yield exact evolution equations for marginal probabilities. These equations form a hierarchy where lower-order marginals depend on higher-order marginals due to interactions between neighboring nodes. The hierarchy resembles the BBGKY hierarchy in statistical mechanics, where closure is challenging without assumptions about higher-order correlations. The paper retains this hierarchy symbolically, avoiding heuristic closures, and uses generalized derivatives to model jump processes (infection and recovery events). Monte Carlo simulations are employed to validate simplified closures and approximate solutions, providing a unified framework that preserves probabilistic content. The method is applied to analyze how network topology and stochastic interactions influence epidemic propagation, including the effects of lockdown measures. The computational steps involve defining the state space, deriving equations through ensemble averages, handling hierarchical dependencies, and validating with simulations. The focus is on modeling systemic complexity rather than delivering a comprehensive epidemic representation.  
DOMAIN: epidemic dynamics on networks  
STRUCTURE: other: hierarchical equations  
DATA_OBJECT: graph or network  
INFERENCE: sampling or Monte-Carlo  
PROBLEM_FORM: simulation or generation  
DISTRIBUTION: discrete; discrete  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: simulation-study
