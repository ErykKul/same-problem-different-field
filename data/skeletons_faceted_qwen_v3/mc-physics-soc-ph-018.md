MECHANISM: The paper computes a mutual information objective between observed node states and an unobserved epidemic prevalence quantity. The goal is to select a subset of nodes that maximizes this mutual information, which quantifies how much information about the prevalence distribution is gained from observing the selected nodes. The mutual information is defined as the difference between the entropy of the prevalence and the conditional entropy of the prevalence given the observed nodes. The conditional entropy is computed using properties of the network and disease spread model, which involves summing over all possible infection states. For general networks, the mutual information is computationally challenging due to exponential complexity in the number of nodes, but for specific network classes (e.g., trees, paths), closed-form expressions or efficient algorithms exist. A greedy algorithm is proposed that iteratively selects nodes to add to the subset, using estimates of mutual information derived from cascade simulations. The algorithm's performance is evaluated through simulations on synthetic and real-world networks, showing improvements in variance reduction and information gain compared to baselines. The problem is shown to be NP-hard, with no polynomial-time approximation guarantees better than logarithmic factors. The method relies on entropy calculations, submodularity properties of the objective function, and sampling-based estimation techniques for general networks.  
DOMAIN: epidemic surveillance in networks  
STRUCTURE: other: greedy submodular optimization  
DATA_OBJECT: graph or network  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: estimation  
DISTRIBUTION: continuous; Poisson binomial  
COMPLEXITY: combinatorial or NP-hard  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: simulation-study
