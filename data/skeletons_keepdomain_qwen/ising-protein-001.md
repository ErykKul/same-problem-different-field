MECHANISM: The paper computes a statistical inference method to distinguish direct from indirect interactions between amino acid sites in protein sequences. It applies pseudolikelihood estimation to 21-state Potts models, which encode pairwise couplings between sites as parameters. The method maximizes a pseudolikelihood function derived from evolutionary data, approximating the full likelihood by treating each site's state as conditionally independent given the others. This approach avoids the computational intractability of exact maximum-likelihood estimation for large systems. The inferred couplings are interpreted as direct interactions, with a modified coupling-strength score used to filter out indirect effects. The model parameters (fields and couplings) are estimated from observables such as site-specific frequencies and pairwise correlations in multiple sequence alignments. The method is validated by comparing predicted residue-residue contacts with known crystal structures, using a scoring function that measures agreement between predicted and observed contacts. The algorithm iteratively updates parameters using gradient-based optimization, with convergence criteria based on changes in the pseudolikelihood. The approach is contrasted with mean-field methods, which approximate the full distribution using factorized assumptions, leading to less accurate contact predictions. The paper emphasizes that the pseudolikelihood method provides a more accurate estimation of direct couplings by avoiding the biases introduced by mean-field approximations. The final model is used to predict three-dimensional structures by identifying pairs of residues with high coupling strengths, which are then mapped to spatial proximity in the protein's folded state.  
DOMAIN: structural biology, protein contact prediction  
STRUCTURE: graphical models  
DATA_OBJECT: sequence or time-series  
INFERENCE: optimization only  
PROBLEM_FORM: estimation  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: public-benchmark-used  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
