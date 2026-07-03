MECHANISM: The paper computes an algorithm for minimizing regret in online learning with two experts, where each expert provides advice over $T$ rounds with costs in $[0,1]$. The algorithm initializes weights for the two experts and updates them iteratively based on observed costs, using a closed-form update rule derived from stochastic calculus. It avoids the $O(T^2)$ pre-processing time of prior dynamic programming approaches by leveraging continuous-time approximations and optimal control theory. The method ensures regret bounded by $\sqrt{T/2\pi} + O(1)$, matching the asymptotic optimality of classical methods while reducing computational overhead. The update rule depends on the difference in cumulative costs between experts and applies a time-varying adjustment factor derived from the solution to a stochastic differential equation. The algorithm guarantees that the regret grows sublinearly with $T$ and does not depend on the number of experts $n$, which is fixed at two. The derivation uses variational principles to minimize the expected regret under a continuous-time cost model, then discretizes the solution for implementation. The method is optimal in the sense that no algorithm can achieve lower regret for this problem class without additional assumptions on the cost structure. The paper proves the regret bound using martingale techniques and analysis of the continuous-time approximation's error terms. The algorithm's per-round computation involves only basic arithmetic operations on the current weights and observed costs, achieving $O(1)$ time complexity.  
DOMAIN: online learning with expert advice  
STRUCTURE: dynamic programming  
DATA_OBJECT: sequence or time-series  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: optimization  
DISTRIBUTION: continuous and continuous  
COMPLEXITY: polynomial iterative  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: mathematical-proof
