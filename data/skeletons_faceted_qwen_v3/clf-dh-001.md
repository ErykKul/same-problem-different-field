MECHANISM: The paper computes a text style feature vector by analyzing word occurrence patterns across natural frequency zones. First, all words in a text are mapped to their natural frequency values, which are precomputed from a large corpus. Words are then partitioned into zones based on these frequencies using linear, radix, or logarithmic methods. For each zone, the algorithm calculates the occurrence positions of words, normalizing them by text length. It then computes pairwise distances between consecutive word occurrences within each zone. These distances are aggregated to derive two statistical features per zone: the average (ODE) and variance (ODV) of occurrence distances. These features collectively form a style vector that captures both frequency and distributional properties of word usage. The vector is used as input to a classifier (e.g., SVM) to determine authorship by comparing the text's style to known author profiles. For open attribution, the method evaluates confidence scores across candidate authors by comparing the proportion of attributed texts to expected random baselines. The process involves segmenting long texts into subsets, applying the basic scheme to each, and aggregating results to decide whether to attribute or reject candidates.  
DOMAIN: authorship attribution, text analysis  
STRUCTURE: other: feature extraction and classification  
DATA_OBJECT: sequence or time-series  
INFERENCE: frequentist point estimate  
PROBLEM_FORM: classification  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-private-data
