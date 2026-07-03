MECHANISM: The paper computes a global minimization problem to reconstruct a sparse or compressible signal from incomplete and noisy Fourier measurements. The signal is represented as a vector in a high-dimensional space, and the measurements are modeled as a linear transformation of this vector corrupted by noise. The method introduces a sparsity constraint, assuming that the signal has only a few significant components in a chosen basis. The optimization problem combines a data fidelity term, which measures the discrepancy between the observed measurements and the model predictions, with a regularization term that enforces sparsity. The solution is obtained by solving a convex optimization problem, which guarantees a unique minimum under certain conditions. The algorithm iteratively updates the estimate of the signal by balancing the trade-off between fitting the data and maintaining sparsity. The method allows for the incorporation of prior information through the choice of the regularization term, which can be tailored to the specific characteristics of the signal. The computational steps involve forming the sensing matrix, applying the optimization algorithm, and evaluating the quality of the reconstruction using metrics derived from the residual error. The approach is compared to a local iterative method, demonstrating its superiority in handling incomplete and noisy data. The framework is general and can be adapted to different types of signals and measurement configurations.  
DOMAIN: radio interferometry  
STRUCTURE: other: convex optimization  
DATA_OBJECT: dense matrix or tensor  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: estimation  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: simulation-study
