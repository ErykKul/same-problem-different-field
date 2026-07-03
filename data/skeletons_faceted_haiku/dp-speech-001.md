MECHANISM: Decode the most probable path through a hidden Markov model trellis in two stages: first compute the posterior probability of each state at each time step using forward-backward probabilities; then apply the Viterbi algorithm to find the best path consistent with the automaton transitions and grammar constraints that maximizes the product of posterior state probabilities; trace back to recover the complete state sequence and assign labels to the observed sequence.
DOMAIN: Computational biology, HMM decoding
STRUCTURE: dynamic programming
DATA_OBJECT: sequence or time-series
INFERENCE: Bayesian posterior
PROBLEM_FORM: prediction or classification
DISTRIBUTION: none
COMPLEXITY: polynomial iterative
