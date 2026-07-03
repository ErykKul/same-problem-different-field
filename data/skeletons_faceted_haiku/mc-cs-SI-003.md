MECHANISM: A sequential decision algorithm iteratively selects elements from a ground set to maximize a submodular function over discrete time steps. The algorithm maintains a priority queue of candidate elements, each with cached marginal gain values. In each step, it greedily selects the element with highest marginal gain by either accepting the top candidate from the queue or recomputing its gain relative to the current set. The algorithm exploits submodularity to avoid redundant gain computations through lazy re-evaluation: gains are only recomputed when an element becomes the top candidate, and previous gains bound current gains for elements not recently checked. After selecting k elements (the exploration phase), the algorithm commits to this set for remaining rounds (exploitation).
DOMAIN: Online influence maximization in social networks
STRUCTURE: dynamic programming
DATA_OBJECT: graph or network
INFERENCE: deterministic or closed-form
PROBLEM_FORM: optimization
DISTRIBUTION: none
COMPLEXITY: polynomial iterative
