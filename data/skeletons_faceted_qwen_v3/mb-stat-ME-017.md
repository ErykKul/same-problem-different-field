MECHANISM: The paper computes a topological causal effect by quantifying differences in the topological structure of potential outcomes using persistence diagrams. For each entity, a filtration of simplicial complexes is constructed, and persistent homology is used to summarize topological features as birth-death pairs in a persistence diagram. These diagrams are converted into functional summaries via power-weighted silhouettes, which aggregate tent functions over persistence pairs with weights based on their lifespans. The target parameter is the expected difference in these silhouettes between treatment and control groups across filtration scales. A doubly robust estimator is developed, combining inverse probability weighting and regression adjustment to estimate the functional causal effect. The estimator relies on nuisance parameters: the propensity score and conditional expectations of the silhouette functions under treatment and control. Weak convergence of the estimator is established, enabling formal hypothesis testing of the null hypothesis of no topological effect. The method is nonparametric, with convergence rates depending on the accuracy of nuisance parameter estimation. Stability bounds for the silhouettes under Wasserstein perturbations of persistence diagrams are derived, ensuring robustness to small changes in the input data. The approach generalizes traditional causal estimands by capturing structural changes in complex, non-Euclidean outcomes that scalar summaries cannot detect.  
DOMAIN: topological data analysis and causal inference  
STRUCTURE: other: topological data analysis  
DATA_OBJECT: persistence diagram and functional silhouette  
INFERENCE: frequentist point estimate  
PROBLEM_FORM: estimation  
DISTRIBUTION: none  
COMPLEXITY: convergence rate  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-private-data
