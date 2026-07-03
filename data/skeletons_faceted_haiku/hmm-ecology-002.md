MECHANISM: A Hidden Markov Model for identifying behavioral states from movement trajectories. The method uses a process equation based on correlated random walk with switching between discrete states, implementing via maximum likelihood estimation. The transition matrix captures switching probabilities between states at each time step. The likelihood is computed as a product over observations of state-conditional movement probabilities, structured as a sequence of diagonal matrices with transition matrices interspersed. Latent behavioral states are decoded post-hoc using the Viterbi algorithm given parameter estimates.
DOMAIN: animal movement ecology; behavioral state identification
STRUCTURE: graphical models
DATA_OBJECT: sequence or time-series
INFERENCE: maximum likelihood estimation; Viterbi decoding
PROBLEM_FORM: classification
DISTRIBUTION: measured movement characteristics (turning angle, step length) modeled as continuous; estimator assumes Gaussian process error
COMPLEXITY: polynomial iterative
