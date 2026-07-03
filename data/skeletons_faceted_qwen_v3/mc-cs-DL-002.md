MECHANISM: The paper computes a percentile-based impact metric (I3) by aggregating citation data across all publications in a database. It first collects citation counts for each publication, then ranks these counts within the full citation distribution using percentile ranks. The metric is calculated as the sum of weighted publication counts across predefined percentile intervals, where weights are determined by the percentile's position in the distribution. This approach avoids biases from skewed citation distributions and numerator–denominator asymmetries inherent in mean-based metrics. The method normalizes results across fields by comparing citation counts to reference sets specific to each discipline. It evaluates the performance of this metric against traditional metrics (JIF and CiteScore) by comparing coverage, methodological robustness, and disciplinary fairness using a matched dataset of journals. The computation involves statistical aggregation, percentile ranking, and field-specific normalization without relying on domain-specific assumptions about citation patterns. The paper does not introduce new algorithms but applies existing methods for citation analysis and percentile-based aggregation.  
DOMAIN: bibliometrics and scientometrics  
STRUCTURE: other: citation-based impact metrics  
DATA_OBJECT: set or table  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: evaluation  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
