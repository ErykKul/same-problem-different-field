MECHANISM: The paper introduces a modified Value Iteration (VI) algorithm for Markov chains (MCs) and Markov decision processes (MDPs) that incorporates a "guessing" step to accelerate convergence. The algorithm iteratively applies Bellman updates to compute value functions for states, but introduces a preprocessing phase that identifies and prioritizes states with high potential impact on the optimal policy. This guessing step uses graph-theoretic properties of the MC/MDP to approximate initial value estimates, reducing the number of required Bellman updates. The method maintains the standard VI structure but modifies the initialization and update order. The algorithm proceeds in iterations: (1) initialize value functions with guesses based on structural properties of the graph; (2) apply Bellman updates to refine values; (3) check for convergence by comparing updated values to previous estimates. The guessing step leverages reachability and shortest-path information to prioritize states that are most influential in determining the optimal policy. The process terminates when the value functions stabilize within a predefined threshold, ensuring the computed policy is optimal. The method is designed to handle both MCs (with no decisions) and MDPs (with actions). The paper analyzes the theoretical guarantees of the algorithm, proving that the number of Bellman updates is reduced compared to standard VI. The approach is applied to both probabilistic models and planning problems with reachability and stochastic shortest path objectives.  
DOMAIN: Markov decision processes and probabilistic systems  
STRUCTURE: dynamic programming  
DATA_OBJECT: graph or network  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: optimization  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: mathematical-proof
