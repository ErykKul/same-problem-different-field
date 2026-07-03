MECHANISM: The paper computes a weighted local constant regression estimator with adaptive constraints. It begins by defining a kernel function and a global bandwidth, then partitions the data into fixed waypoints and stochastic observations. For each evaluation point, it assigns weights based on a kernel density function scaled by a global bandwidth. To enforce constraints at fixed waypoints, it introduces a tuning parameter that scales the weights of these points, decoupling smoothness from constraint adherence. The estimator is derived by solving a weighted least squares problem, combining contributions from both stochastic and fixed points. An iterative data sharpening procedure follows, where residuals from the initial estimate are added back to the original responses, and the same estimator is reapplied to the updated dataset. This process reduces bias while maintaining the fixed waypoint mechanism. The algorithm iterates a fixed number of times, balancing bias reduction against variance inflation. Theoretical analysis derives asymptotic bias and variance, proving convergence under standard regularity conditions. The method is applied to synthetic and real-world datasets to validate its ability to balance smoothness and constraint satisfaction.  
DOMAIN: route alignment design  
STRUCTURE: other: kernel regression with adaptive weights  
DATA_OBJECT: set or table  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: estimation  
DISTRIBUTION: continuous; continuous  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: simulation-study
