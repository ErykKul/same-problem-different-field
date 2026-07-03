MECHANISM: Solve an optimal stopping problem via backward induction time-stepping; at each step compute the value function as the maximum of immediate payoff and continuation value (expected future value); approximate the value function using Chebyshev polynomial basis with coefficients computed at Chebyshev grid nodes; separate the computation into offline phase (compute generalized conditional moments via Monte Carlo, PDE, or Fourier methods) and online phase (backward induction on the discrete grid); recover both the value function and its derivatives (delta, gamma) in closed form.
DOMAIN: Quantitative finance, derivatives pricing
STRUCTURE: dynamic programming
DATA_OBJECT: continuous function or field
INFERENCE: deterministic or closed-form
PROBLEM_FORM: optimization
DISTRIBUTION: none
COMPLEXITY: polynomial iterative
