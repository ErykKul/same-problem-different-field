MECHANISM: The paper evaluates the performance of linear classifiers (both generative and discriminative) in alignment-free classification of viral genomic sequences. It systematically varies hyperparameters such as smoothing values and regularization penalties, and tests classifiers on different sequence lengths (partial vs. complete genomes) and k-mer word lengths. The method involves training models on k-mer frequency tables derived from viral sequences, then assessing classification accuracy for genotyping and subtyping tasks. The evaluation is performed using statistical learning techniques, with no explicit alignment or phylogenetic analysis. The study compares classifier types and their parameter configurations to identify optimal combinations for HCV classification. The procedure includes cross-validation and benchmarking against standard metrics. The analysis focuses on the interplay between model structure, data characteristics, and classification performance. No novel algorithm is proposed; the work is an empirical assessment of existing linear methods. The computational core is the application of linear classifiers to k-mer-based features for viral sequence categorization. The study does not involve probabilistic modeling or optimization beyond standard training procedures.  
DOMAIN: viral genomics and machine learning  
STRUCTURE: dense linear algebra  
DATA_OBJECT: sequence or time-series  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: classification  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: public-benchmark-used  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
