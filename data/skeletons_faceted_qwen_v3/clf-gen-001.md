MECHANISM: The paper computes a classification mechanism using linear models on k-mer frequency vectors derived from nucleotide sequences. Sequences are transformed into feature vectors by counting occurrences of k-length subsequences (k-mers). These vectors are then used to train generative and discriminative linear classifiers. Generative models estimate class-conditional probabilities using multinomial distributions or Markov chains, while discriminative models learn decision boundaries via logistic regression or support vector machines. Hyperparameters such as smoothing values and regularization penalties are optimized. The method evaluates classifier performance using weighted F-measure on complete and fragmented sequences, comparing results across varying k-mer lengths and classification tasks (genotyping vs. subtyping). Training involves estimating model parameters from complete genomes, and testing is performed on both complete and partial sequences without explicit sampling of fragments during training. The process includes cross-validation strategies to assess robustness and generalization across different sequence lengths and taxonomic levels.  
DOMAIN: virus genomic classification  
STRUCTURE: dense linear algebra  
DATA_OBJECT: dense matrix  
INFERENCE: Bayesian posterior  
PROBLEM_FORM: classification  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: dataset-with-DOI-or-handle  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
