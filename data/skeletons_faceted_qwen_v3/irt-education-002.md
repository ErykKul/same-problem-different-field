MECHANISM: The paper computes a scalable method for learning latent parameters in Item Response Theory (IRT) models using coresets. The process begins by initializing latent parameters for both examinees and items. It then alternates between two optimization steps: first, optimizing item parameters (difficulty, discrimination, guessing) given fixed examinee abilities, and second, optimizing examinee abilities given fixed item parameters. Each optimization step involves solving logistic regression subproblems, where the labels differ per examinee or item. To handle large datasets, coresets are constructed as weighted subsets of the data that approximate the original loss function up to a small error. Coresets are built using sensitivity sampling, which assigns weights to data points based on their individual contribution to the loss function. This allows the algorithm to reduce computational complexity while maintaining statistical accuracy. The method is applied iteratively until convergence or an iteration budget is met. The coreset construction leverages properties of the logistic loss function and bounds on data complexity parameters (e.g., $\mu$-complexity) to ensure sublinear size coresets. The approach is validated empirically for both 2PL and 3PL IRT models, demonstrating computational efficiency without significant loss in statistical performance.  
DOMAIN: psychometrics and machine learning  
STRUCTURE: other: alternating optimization  
DATA_OBJECT: dense matrix or tensor  
INFERENCE: frequentist point estimate  
PROBLEM_FORM: estimation  
DISTRIBUTION: binary; logistic  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-private-data
