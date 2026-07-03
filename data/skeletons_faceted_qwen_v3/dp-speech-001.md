MECHANISM: The paper computes a decoding algorithm for probabilistic state sequences using a two-step process. First, it calculates the posterior probability of each state given an observed sequence of observations. This involves computing forward and backward probabilities for each state at each position in the sequence, then normalizing these to obtain posterior probabilities. Second, it applies a Viterbi-like dynamic programming algorithm to find the most probable path through the states that adheres to the automaton grammar constraints. The algorithm initializes probabilities for the start state, then recursively computes the maximum probability path ending at each state by considering all possible prior states and their transition probabilities. At each step, it maintains a traceback pointer to reconstruct the optimal path. The process terminates by selecting the highest-probability end state, then backtracks through the pointers to reconstruct the full path. Finally, it assigns labels to each position in the sequence based on the selected states. The method combines posterior probabilities with grammar constraints to improve decoding accuracy compared to traditional Viterbi or posterior-only approaches.
DOMAIN: computational molecular biology
STRUCTURE: dynamic programming
DATA_OBJECT: sequence or time-series
INFERENCE: deterministic or closed-form
PROBLEM_FORM: prediction or classification
DISTRIBUTION: none
COMPLEXITY: polynomial iterative
DATA_AVAILABILITY: public-benchmark-used
CODE_AVAILABILITY: none
PREREGISTRATION: none
EVIDENCE_BASIS: empirical-with-released-data
