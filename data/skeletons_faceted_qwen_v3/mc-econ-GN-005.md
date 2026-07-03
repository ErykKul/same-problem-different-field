MECHANISM: The paper computes a conditional expectation function from a set of observable variables, partitioning entities into discrete groups using supervised decision trees. These partitions are defined by measurable attributes rather than latent factors. A gradient-boosted tree model estimates the function, incorporating cross-fitting to account for dependencies between paired observations. The model decomposes variance into components attributable to worker groups, firm groups, sorting effects, and interactions between groups. Each group's contribution is derived by projecting the estimated function onto discrete partitions, ensuring orthogonal decomposition. The method avoids assumptions about additivity by allowing non-linear interactions. Variance shares are calculated using cell means, with residuals capturing unexplained variation. Sorting patterns are inferred from the distribution of worker groups across firm groups. Partial dependence and accumulated local effect plots are used to interpret how specific attributes influence predicted outcomes. The framework retains a two-way decomposition structure similar to traditional models but replaces latent effects with interpretable partitions. The algorithm iteratively refines partitions based on out-of-sample performance metrics, ensuring robustness to sparse data and generalizability to new entities.  
DOMAIN: labor economics and econometrics  
STRUCTURE: other: gradient-boosted trees  
DATA_OBJECT: set or table  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: estimation  
DISTRIBUTION: continuous; conditional expectation  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
