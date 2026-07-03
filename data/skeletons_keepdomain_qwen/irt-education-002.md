MECHANISM: The paper computes a scalable method for learning Item Response Theory (IRT) models by approximating logistic regression using weighted subsets of data called coresets. The process begins by formulating the IRT model as a logistic regression problem, where latent examinee abilities and item difficulties are estimated from categorical response data. A coreset is constructed by selecting a small, weighted subset of the full dataset, where weights are determined by the importance of each data point in representing the overall distribution. These coresets are then used in an alternating optimization algorithm, where parameters are iteratively updated by alternating between estimating latent abilities and item difficulties. The coreset approximation reduces computational complexity by focusing on the most informative data points, enabling efficient scaling to large $n$ and $m$. The algorithm ensures that the coreset maintains statistical fidelity to the original data through weighted sampling techniques. The method is applied to both classical psychometric data (e.g., exams with 200 students and 10 items) and large-scale datasets (e.g., PISA or internet studies) where $n$ and $m$ are orders of magnitude larger. The paper emphasizes that the coreset-based approach preserves the accuracy of traditional IRT methods while significantly reducing computation time. The final estimates of latent abilities and item difficulties are derived through iterative refinement of the coreset-based logistic regression model. The method is validated through empirical testing on large datasets, demonstrating its scalability and accuracy compared to non-approximate methods.  
DOMAIN: psychometrics and machine learning  
STRUCTURE: other: coreset-based approximation  
DATA_OBJECT: set or table  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: estimation  
DISTRIBUTION: count; logistic  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-private-data
