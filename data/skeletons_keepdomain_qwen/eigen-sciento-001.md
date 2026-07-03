MECHANISM: The paper computes a journal importance metric by analyzing the citation network between journals. It constructs a matrix where each entry represents the number of citations from one journal to another. This matrix is normalized to create a transition probability matrix, and the principal eigenvector of this matrix is computed. The entries of the eigenvector represent the relative importance of each journal, with higher values indicating greater influence. The algorithm iteratively solves the eigenvalue problem until convergence, using the power iteration method. The importance of a journal is determined by both the number of citations it receives and the importance of the journals citing it. The method is deterministic and closed-form, relying on linear algebra operations. The final Eigenfactor score is derived by normalizing the eigenvector entries to a specific range. The computation does not involve probabilistic modeling or uncertainty quantification. The algorithm is applied to a network of journals, with each node representing a journal and edges representing citation relationships. The method is explicitly described as an application of Eigenvector centrality to bibliometric analysis.  
DOMAIN: bibliometrics  
STRUCTURE: dense linear algebra  
DATA_OBJECT: graph or network  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: estimation  
DISTRIBUTION: none  
COMPLEXITY: polynomial iterative  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: mathematical-proof
