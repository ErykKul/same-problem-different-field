MECHANISM: This paper computes a policy evaluation and training framework for generative models operating on combinatorial spaces represented as directed acyclic graphs (DAGs). The method balances flows along trajectories by enforcing equality between forward and backward trajectory distributions, using a divergence measure derived from KL divergence. The process involves (1) decomposing combinatorial generation into incremental trajectories starting from an initial state and ending at terminal states, (2) defining flows as unnormalized probabilities along edges and states, (3) formulating a balance condition that equates expected log-flow values under forward and backward policies, (4) introducing a subtrajectory-based evaluation balance objective that measures divergence between forward and backward subtrajectories, and (5) optimizing policies through gradient descent on this objective. The evaluation function $V(s)$ is learned to approximate KL divergence between subtrajectory distributions, enabling policy updates that minimize divergence. The method supports parameterized backward policies and integrates offline data collection by relaxing assumptions on policy fixedness. The computational steps include trajectory sampling, flow estimation, divergence calculation, and gradient-based parameter updates, all operating on DAG structures with state and edge flows as core variables.

DOMAIN: generative models and reinforcement learning

STRUCTURE: other: gradient-based optimization

DATA_OBJECT: graph or network

INFERENCE: sampling or Monte-Carlo

PROBLEM_FORM: optimization

DISTRIBUTION: none

COMPLEXITY: not stated

DATA_AVAILABILITY: public-repository

CODE_AVAILABILITY: public-repository

PREREGISTRATION: none

EVIDENCE_BASIS: empirical-with-released-data
