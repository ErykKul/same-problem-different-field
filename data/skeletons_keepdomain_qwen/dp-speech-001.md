MECHANISM: The paper introduces a two-step decoding algorithm for hidden Markov models (HMMs) called posterior-Viterbi (PV). In the first step, the algorithm computes the posterior probability of each state in the model given an observed sequence, using the HMM's transition and emission probabilities. These posterior probabilities are calculated by marginalizing over all possible state paths, which involves summing over the joint probabilities of the sequence and state path. In the second step, the algorithm applies a modified Viterbi algorithm to find the single most probable state path under the constraint that each state in the path must have a posterior probability above a certain threshold. This threshold is determined by the posterior probabilities computed in the first step. The PV algorithm combines the advantages of posterior decoding (which considers multiple probable paths) and Viterbi decoding (which finds the single optimal path) by first relaxing the constraint of a single dominant path and then enforcing a path selection based on posterior probabilities. The algorithm operates on the same probabilistic framework as standard HMM decoding but introduces a new criterion for path selection. The method is evaluated on synthetic toy models and applied to the problem of predicting the topology of beta-barrel membrane proteins, where the state path corresponds to the protein's transmembrane helix arrangement. The computational steps involve matrix exponentiation for transition probabilities, forward-backward algorithms for posterior computation, and dynamic programming for path selection. The paper does not introduce new mathematical principles but recombines existing HMM inference techniques into a novel decoding strategy.
DOMAIN: computational molecular biology
STRUCTURE: dynamic programming
DATA_OBJECT: sequence or time-series
INFERENCE: bayesian posterior
PROBLEM_FORM: prediction or classification
DISTRIBUTION: none
COMPLEXITY: not stated
DATA_AVAILABILITY: none
CODE_AVAILABILITY: none
PREREGISTRATION: none
EVIDENCE_BASIS: empirical-with-released-data
