MECHANISM: Compute feature frequency statistics from attribute-value vectors. Apply three variant Bayesian probabilistic classifiers (multinomial, Bernoulli, Gaussian) each with distinct distributional assumptions. Each variant estimates class-conditional probability distributions from training data and assigns new instances to the class maximizing posterior probability. Compare accuracy across variants to understand how classifier assumptions affect performance on intrusion detection data.
DOMAIN: Network intrusion detection and anomaly classification
STRUCTURE: graphical models
DATA_OBJECT: set or table
INFERENCE: frequentist point estimate
PROBLEM_FORM: classification
DISTRIBUTION: none
COMPLEXITY: polynomial iterative
