MECHANISM: The paper computes the convergence of policy evaluation and Q-learning algorithms under non-Markov processes using linear function approximation. The algorithm iteratively updates parameters θ_t via a stochastic approximation scheme, where each update involves a matrix A(Z_t) and vector b(Z_t) derived from the joint process Z_t = (S_{t+1}, S_t, C_t, U_t). The process relies on ergodicity conditions to ensure the joint process Z_t has a stationary distribution π. The algorithm decomposes the error term into a martingale difference and telescoping summable terms using a Poisson equation under Assumption 1. The convergence is shown to a fixed point of the joint operator composed of an orthogonal projection and the Bellman operator of an auxiliary Markov decision process. For Q-learning, convergence is not guaranteed in general but holds under special cases like discretization-based basis functions or specific covariance conditions. The error bounds for the learned values are derived by decomposing the error into projection and finite-memory approximation terms. The method assumes the stationary average matrix A is positive definite and uses uniform boundedness of A(Z_t) and b(Z_t) to ensure convergence.  
DOMAIN: reinforcement learning with non-Markov processes  
STRUCTURE: polynomial iterative  
DATA_OBJECT: sequence or time-series  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: estimation  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: mathematical-proof
