MECHANISM: Decode a sequence transmitted through a noisy channel using dynamic programming over a trellis of states; at each time step, compute the maximum-likelihood path by evaluating path metrics that combine received symbol likelihoods with transition costs; maintain only the best partial path to each state (pruning); use the soft-decision (continuous-valued) channel observations rather than hard-decision (binary) data to improve decoding performance; derive the minimum mean-square error (MMSE) of the soft-decision input by analyzing its statistical distribution and covariance properties.
DOMAIN: Digital communications, channel decoding
STRUCTURE: dynamic programming
DATA_OBJECT: sequence or time-series
INFERENCE: Bayesian posterior
PROBLEM_FORM: decision or test
DISTRIBUTION: continuous; Gaussian
COMPLEXITY: polynomial iterative
