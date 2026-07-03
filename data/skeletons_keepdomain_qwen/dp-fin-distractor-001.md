MECHANISM: The paper computes the price of high-dimensional contingent claims using a Monte Carlo method enhanced by neural networks. The algorithm first simulates paths of the underlying asset processes, then trains a neural network to approximate the conditional expectation of the claim's payoff at future times. This approximation is used to compute the price via backward induction, avoiding the curse of dimensionality. The neural network architecture is designed to produce interpretable outputs, enabling the construction of a semi-static hedging strategy using a portfolio of short-maturity options. The method computes both upper and lower bounds on the true price: the lower bound is derived by following a sub-optimal hedging policy, while the upper bound is obtained through a dual formulation that avoids nested simulations. The dual formulation leverages the martingale property of the neural network's output, ensuring that the upper bound is computed without additional computational cost. The algorithm's efficiency is demonstrated through numerical experiments on path-dependent options, showing that the bounds converge rapidly with increasing simulation samples. The neural network's training is performed using gradient-based optimization on the simulated data, with the loss function designed to minimize the difference between the network's output and the true conditional expectation. The method's applicability is restricted to Markovian processes under no-arbitrage assumptions, ensuring the validity of the hedging strategy. The paper emphasizes that the neural network's interpretability allows for explicit construction of the hedging portfolio, a key advantage in financial applications where transparency is critical. The computational steps are explicitly tied to the financial context, with no abstraction from the domain-specific terms used in the paper.

DOMAIN: financial mathematics and contingent claims pricing

STRUCTURE: other: Monte Carlo with neural networks

DATA_OBJECT: sequence or time-series

INFERENCE: sampling or Monte-Carlo

PROBLEM_FORM: estimation

DISTRIBUTION: continuous; continuous

COMPLEXITY: not stated

DATA_AVAILABILITY: none

CODE_AVAILABILITY: none

PREREGISTRATION: none

EVIDENCE_BASIS: simulation-study
