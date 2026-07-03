MECHANISM: A Hidden Markov Model assigns discrete hidden states to positions in a sequence, where each state emits symbols according to a state-specific distribution. Transition probabilities govern state-to-state movement along the sequence. The model parameters (transition and emission matrices) are estimated using the Baum-Welch algorithm, a special case of expectation-maximization that alternates between computing forward/backward probabilities and updating parameter estimates. After training, the Viterbi algorithm decodes the most probable state sequence for a given observation sequence.
DOMAIN: computational biology; genomics; gene sequence classification
STRUCTURE: graphical models
DATA_OBJECT: sequence or time-series
INFERENCE: maximum likelihood estimation via Baum-Welch; Viterbi decoding
PROBLEM_FORM: classification
DISTRIBUTION: measured as discrete symbols (nucleotides A, C, G, T) emitted per state; estimator assumes categorical emission distributions
COMPLEXITY: polynomial iterative
