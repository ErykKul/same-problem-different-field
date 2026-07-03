MECHANISM: Compute the value function for each state in a Markov decision process via iterative Bellman updates; each update estimates the expected sum of costs (or optimal reward) from a state given a control policy; update decision states by taking the optimal choice over successor actions and probabilistic states by taking the expectation over the transition distribution; apply a preprocessing step to partition states into levels based on distance to target states and identify a set of states for which values will be guessed; verify guesses efficiently by applying single Bellman updates on reduced MDPs.
DOMAIN: Operations research, stochastic control
STRUCTURE: dynamic programming
DATA_OBJECT: graph or network
INFERENCE: deterministic or closed-form
PROBLEM_FORM: optimization
DISTRIBUTION: none
COMPLEXITY: polynomial iterative
