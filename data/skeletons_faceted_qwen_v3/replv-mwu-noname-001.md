MECHANISM: The paper computes an algorithm for minimizing regret in a sequential decision-making problem with two experts. The algorithm operates by defining a continuous-time stochastic process (Brownian motion) and solving a partial differential equation (the backward heat equation) to derive a closed-form solution for the optimal probability distribution over experts. This continuous-time solution is then discretized into a discrete-time algorithm with O(T) time complexity. The method involves defining a function R(t,g) that satisfies the backward heat equation, where t represents time and g represents the gap between expert losses. The solution to this equation is used to determine the probability p(t,g) assigned to the lagging expert at each time step and gap value. The algorithm ensures that the regret, defined as the difference between the cumulative loss of the player and the best expert, is bounded by sqrt(T/(2π)) + O(1). The approach leverages stochastic calculus, including Itô's formula, to handle the continuous-time stochastic integral and derive the optimal strategy. The discretization step introduces a small error, which is shown to be negligible for the regret bound. The method is compared to existing dynamic programming approaches, which have higher time complexity (O(T²)), and is shown to achieve the same regret bound with improved efficiency. The algorithm's correctness is validated through mathematical analysis and connections to symmetric random walks.

DOMAIN: online learning, regret minimization, expert advice

STRUCTURE: dynamic programming; other: continuous-time stochastic process

DATA_OBJECT: continuous function or field

INFERENCE: deterministic or closed-form

PROBLEM_FORM: optimization

DISTRIBUTION: none

COMPLEXITY: polynomial iterative

DATA_AVAILABILITY: none

CODE_AVAILABILITY: none

PREREGISTRATION: none

EVIDENCE_BASIS: mathematical-proof
