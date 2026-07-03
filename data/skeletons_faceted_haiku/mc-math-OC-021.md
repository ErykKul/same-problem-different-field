MECHANISM: Design an importance sampling scheme for rare event simulation in stochastic differential equations that avoids reweighting long trajectories. Use variational principles with strictly convex transformations (exponential or quadratic) to characterize zero-variance importance measures. For each transformation, derive the associated stochastic optimal control problem with an unbounded random stopping time. Solve the corresponding Hamilton-Jacobi-Bellman equation to obtain the value function, which encodes the optimal importance sampling measure. Implement an approximate policy iteration algorithm to compute the value function and optimal feedback control policy. Apply this to compute committor functions and mean first exit times for rare transition events in high-dimensional stochastic systems.
DOMAIN: Rare event simulation, molecular dynamics, Monte Carlo variance reduction
STRUCTURE: dynamic programming
DATA_OBJECT: continuous function or field
INFERENCE: sampling or Monte-Carlo
PROBLEM_FORM: estimation
DISTRIBUTION: heavy-tailed; importance sampling distribution
COMPLEXITY: not stated
