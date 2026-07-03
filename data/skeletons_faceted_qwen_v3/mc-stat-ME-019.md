MECHANISM: The paper computes an unsupervised clustering of entities based on heterogeneous treatment effects using a modified random survival forest algorithm. The method constructs an ensemble of decision trees, where each tree is grown by recursively partitioning the data using a splitting rule that jointly optimizes for treatment effect heterogeneity and survival outcomes. The splitting rule fits a Cox proportional hazards model to estimate treatment-covariate interactions, using a test statistic that combines concordance index and interaction coefficients. Proximity between entities is quantified as the proportion of trees in which they share terminal nodes, with weights adjusted by outcome relevance. Clustering is then applied to the proximity matrix to identify subgroups with distinct treatment benefit patterns. The algorithm iteratively refines splits to maximize the test statistic, ensuring statistical control of type I error through calibration. The final output includes subgroup assignments, proximity-based similarity metrics, and interpretable decision tree explanations for cluster membership.  
DOMAIN: survival analysis and machine learning  
STRUCTURE: map-reduce or embarrassingly-parallel  
DATA_OBJECT: set or table  
INFERENCE: frequentist point estimate  
PROBLEM_FORM: estimation  
DISTRIBUTION: survival or time-to-event; no specific distribution  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-private-data
