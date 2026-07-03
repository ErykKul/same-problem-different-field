MECHANISM: The paper computes a statistical inference method to estimate parameters of a Potts model from observed correlations in a dataset of sequences. The method uses pseudolikelihood, which approximates the full likelihood by treating each variable's distribution conditionally on others. The Potts model is defined over a graph where nodes represent entities and edges represent pairwise interactions. Parameters include fields (single-entity biases) and couplings (pairwise interaction strengths). The pseudolikelihood function is maximized via gradient-based optimization to find the best-fitting parameters. The inferred couplings are used to identify direct interactions between entities, distinguishing them from indirect correlations propagated through intermediaries. The method avoids explicit modeling of higher-order interactions by focusing on pairwise terms. The optimization process iteratively updates parameters until convergence, using observed marginal distributions as targets. The resulting model is validated by comparing predicted interactions to known structural data. The approach generalizes to systems with discrete states and sparse interactions, avoiding assumptions about the underlying distribution of the data beyond the Potts model's form.  
DOMAIN: statistical mechanics and protein structure prediction  
STRUCTURE: graphical models  
DATA_OBJECT: graph or network  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: estimation  
DISTRIBUTION: binary; discrete  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
