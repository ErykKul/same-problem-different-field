MECHANISM: Generate samples of asset paths via stochastic discretization; at each monitoring date moving backward in time, approximate the continuation value (future value function) using Monte Carlo regression with a neural-network basis; parameterize the value function as a shallow neural network (ReLU hidden layer + linear output layer); fit network parameters by minimizing mean-squared error on samples; compute continuation values via numerical integration or closed-form approximations of network expectations; determine optimal exercise by comparing immediate payoff with continuation value.
DOMAIN: Quantitative finance, neural-network-based pricing
STRUCTURE: other: regression-based Monte Carlo
DATA_OBJECT: point set
INFERENCE: frequentist point estimate
PROBLEM_FORM: estimation
DISTRIBUTION: none
COMPLEXITY: polynomial iterative
