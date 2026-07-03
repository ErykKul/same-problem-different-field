MECHANISM: A fifth-order Hidden Markov Model assigns secondary structure states (quintuplets of residue conformations) to positions in a protein sequence. Emission probabilities are derived from Chou-Fasman propensity scores computed over sliding windows of amino acids flanking each position. The transition probabilities are estimated from counts of observed state transitions, with special handling for length constraints on helices and extended strands. The Viterbi and Baum-Welch algorithms decode the most probable or posterior probable structure sequence given parameter estimates.
DOMAIN: structural biology; protein bioinformatics
STRUCTURE: graphical models
DATA_OBJECT: sequence or time-series
INFERENCE: maximum likelihood estimation from counts; Viterbi decoding; Baum-Welch posterior marginals
PROBLEM_FORM: classification
DISTRIBUTION: measured as discrete secondary structure classes (helix, strand, coil); estimator assumes categorical per-state distribution
COMPLEXITY: polynomial iterative
