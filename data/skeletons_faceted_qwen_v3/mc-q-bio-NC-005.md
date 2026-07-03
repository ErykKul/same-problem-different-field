MECHANISM: The paper computes a classification of facial expressions using neural activity patterns recorded via intracranial electrodes. It begins by collecting time-series data from electrode contacts, capturing event-related potentials (ERPs) and event-related spectral perturbations (ERSPs) across multiple frequency bands. The method then extracts temporal features by averaging trials within each expression category and identifying significant time points through statistical tests. Principal component analysis (PCA) is applied to trial-averaged matrices to determine the most informative time periods. Similarity between patterns is quantified using Euclidean distance, comparing within-category and between-category trials to assess classification accuracy. The algorithm identifies expression-specific temporal patterns by evaluating how well within-category similarity exceeds between-category similarity across electrode contacts. For ERPs, the method focuses on timecourses with distinct deflection profiles, while for ERSPs, it analyzes frequency-specific spectral changes. The process involves clustering timecourses to reveal heterogeneous temporal patterns and comparing spatial distributions of successful identifications across brain regions. The final output is a map of electrode contacts where specific expressions are reliably identified, based on the discriminative power of their temporal and spectral features.  
DOMAIN: neuroscience, emotion processing  
STRUCTURE: pattern analysis  
DATA_OBJECT: time-series  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: classification  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-private-data
