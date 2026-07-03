MECHANISM: The paper computes a journal ranking metric based on the network structure of citations between entities. It constructs a cross-citation matrix where entries represent the number of links from one entity to another over a five-year period. The matrix is normalized by dividing each column by its total sum, producing a column-stochastic matrix of citation probabilities. A stochastic traversal matrix is defined by combining the normalized matrix with a uniform distribution over all entities, weighted by a parameter α that balances local citation probabilities and global random jumps. The Eigenfactor score is derived as the leading eigenvector of this traversal matrix, representing the steady-state distribution of influence across entities. This eigenvector quantifies the relative importance of each entity based on the weighted influence of its neighbors in the network. The algorithm excludes self-citations by setting diagonal entries of the matrix to zero. The final score is scaled to a percentage of total weighted citations received by each entity. The method mirrors Google’s PageRank algorithm by using a Markov process to model random walks through the citation network. The computation assumes a static network structure and deterministic transitions between entities.  
DOMAIN: bibliometrics  
STRUCTURE: spectral or transform  
DATA_OBJECT: dense matrix  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: ranking or retrieval  
DISTRIBUTION: none  
COMPLEXITY: polynomial iterative  
DATA_AVAILABILITY: public-benchmark-used  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: review-or-position
