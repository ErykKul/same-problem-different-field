MECHANISM: Constructs a Gaussian process surrogate model to approximate the objective function of a stochastic economic dispatch optimization problem for power systems with random wind generation. Samples input-output pairs from the original expensive dispatch solver and trains a GP with a Matérn covariance kernel. Uses the GP's posterior mean and variance to quantify uncertainty in the dispatch cost under random renewable power generation. Applies Karhunen-Loève expansion to spatiotemporal wind data for model reduction. Replaces the expensive optimization in Monte Carlo sampling with cheap GP evaluations to compute statistical moments of the dispatch cost.
DOMAIN: Power systems, economic dispatch, uncertainty quantification
STRUCTURE: other: kernel-based regression
DATA_OBJECT: dense matrix or tensor
INFERENCE: Bayesian posterior
PROBLEM_FORM: estimation
DISTRIBUTION: continuous; continuous
COMPLEXITY: polynomial iterative
