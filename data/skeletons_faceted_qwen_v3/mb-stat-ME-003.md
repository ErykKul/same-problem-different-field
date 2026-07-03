MECHANISM: The paper computes a convex optimization procedure for feature selection with finite-sample guarantees on error rates. It formulates a convex objective function combining a squared error term and a sorted ℓ₁ penalty, where the penalty sequence is derived to control k-FWER and FDP thresholds. The method integrates stepdown rules into SLOPE, adjusting the regularization sequence based on user-specified error levels. For orthogonal designs, closed-form regularization sequences are derived using inverse normal quantiles, ensuring provable bounds on k-FWER and FDP. These results are extended to grouped settings via gk-SLOPE and gF-SLOPE, which apply group-level sparsity regularization. For non-orthogonal designs, a data-driven sequence is calibrated using Gaussian approximation and Monte-Carlo correction, preserving convexity and scalability. The algorithm iteratively solves the optimization problem using proximal gradient descent with backtracking line search. The method avoids explicit p-value computation, relying instead on thresholding based on sorted statistics. It operates on a vector of regression coefficients, applying non-increasing regularization parameters to enforce sparsity. The procedure is validated through simulations across sparse, correlated, and group-structured regimes, demonstrating improved power compared to existing methods. Theoretical guarantees are derived for both single and grouped feature selection under k-FWER and FDP constraints.  
DOMAIN: high-dimensional statistical learning  
STRUCTURE: other: convex optimization  
DATA_OBJECT: sequence or time-series  
INFERENCE: frequentist point estimate  
PROBLEM_FORM: estimation  
DISTRIBUTION: continuous; normal  
COMPLEXITY: finite-sample bound  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: simulation-study
