MECHANISM: The paper computes optimal transportation distances between histograms by solving a regularized linear program with an entropic penalty term. The classical transportation problem is transformed into a matrix scaling problem through the addition of an entropy regularization term, which ensures the solution can be computed efficiently. The resulting optimization problem is solved using Sinkhorn-Knopp's matrix scaling algorithm, which iteratively scales the rows and columns of a cost matrix to satisfy marginal constraints. The algorithm operates on a dense matrix representing the transportation plan, with the entropic regularization parameter controlling the trade-off between accuracy and computational speed. The method guarantees convergence to a distance metric that approximates the original optimal transportation distance while achieving significant speed improvements. The paper evaluates the method on the MNIST benchmark, comparing its performance against classical transportation solvers in terms of computational time and retrieval accuracy. The algorithm's efficiency stems from the structure of the entropic regularization, which allows for fast matrix operations and avoids the combinatorial complexity of the original linear program. The final distance metric is computed as the dual objective of the regularized problem, which is shown to be a valid distance measure under certain conditions. The method's parameters are tuned based on empirical validation on the benchmark dataset, and the paper reports improved retrieval performance over existing methods. The computational steps are explicitly described as a sequence of matrix scaling iterations with convergence guarantees.  
DOMAIN: optimal transportation theory  
STRUCTURE: dense linear algebra  
DATA_OBJECT: dense matrix  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: estimation  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: public-benchmark-used  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
