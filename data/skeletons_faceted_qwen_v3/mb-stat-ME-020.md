MECHANISM: The paper computes a generalized linear step-up procedure for false discovery rate (FDR) control in variable selection. It begins by clustering predictors hierarchically based on correlation, forming sets of variables. For each set, it tests whether the set contains any non-null effects, using hypothesis testing procedures. The method generalizes existing linear step-up procedures (e.g., Benjamini–Hochberg) to handle composite hypotheses arising from setwise selection. It defines FDR using a sizing function that weights discoveries based on set size, ensuring that rejecting a superset hypothesis does not count as multiple discoveries. The procedure determines a threshold slope α to control FDR by solving for the maximum cutoff c where the sizing function of the closure of rejected hypotheses meets αc. It iteratively adjusts rejection thresholds, considering dependencies between hypotheses and ensuring that only minimal clusters (those not contained within other rejected clusters) contribute to the FDR count. The method is designed to maintain FDR control while allowing selection of sets of variables that may contain true predictors, even when individual variables cannot be uniquely identified. It applies to any variable selection problem with valid p-values for sets of predictors and is validated through simulations and real-data analyses.  
DOMAIN: statistical methodology for variable selection  
STRUCTURE: other: hierarchical clustering and hypothesis testing  
DATA_OBJECT: set of predictors  
INFERENCE: frequentist point estimate  
PROBLEM_FORM: estimation  
DISTRIBUTION: none  
COMPLEXITY: polynomial iterative  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: simulation-study
