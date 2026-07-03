MECHANISM: The paper computes a Monte Carlo-based method for pricing and hedging contingent claims using a neural network. It generates sample paths of an underlying stochastic process, then recursively computes the value of the claim at each monitoring date by approximating conditional expectations. At each time step, a parametrized value function is trained using a feed-forward neural network with two hidden layers: the first layer uses ReLU activations to model the payoff structure of options, and the second layer uses linear activations to determine portfolio weights. The trained network is used to approximate the continuation value, which is then compared to the intrinsic value of the option to determine the optimal exercise decision. The method leverages the "regress later" approach, where the value function at a future time is approximated first, allowing the conditional expectation at an earlier time to be computed exactly. This avoids the need for nested simulations typically required in dual formulations. The neural network's output is interpreted as a static hedging portfolio of short-maturity options, enabling semi-static replication of the claim. The algorithm iteratively refines the value function estimates by minimizing the mean squared error between the network's predictions and the true values derived from the sample paths. The method provides both lower and upper bounds on the true price by using sub-optimal and dual formulations, respectively. The computational steps involve generating paths, training the network, evaluating expectations, and updating value functions in reverse chronological order.
DOMAIN: financial mathematics, derivative pricing
STRUCTURE: other: regress later
DATA_OBJECT: point set
INFERENCE: deterministic or closed-form
PROBLEM_FORM: estimation; optimization
DISTRIBUTION: none
COMPLEXITY: polynomial iterative
DATA_AVAILABILITY: none
CODE_AVAILABILITY: none
PREREGISTRATION: none
EVIDENCE_BASIS: simulation-study
