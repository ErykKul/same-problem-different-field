MECHANISM: The paper computes optimal importance sampling measures to estimate rare event probabilities with minimal variance. It transforms the target random variable using strictly convex functions (e.g., exponential or quadratic) to derive a zero-variance change of measure. The optimal measure is characterized by solving a stochastic control problem, where the control policy is determined via a feedback mechanism dependent on the system state. Two formulations are analyzed: one based on the logarithmic transformation of the moment generating function (leading to a linear quadratic stochastic control problem) and another based on the square root transformation of the second moment (leading to a risk-sensitive control problem). The solution involves solving Hamilton-Jacobi-Bellman equations for the value function and deriving feedback control policies. An approximate policy iteration (API) algorithm is proposed to iteratively refine the control policy and value function, with convergence guarantees for the logarithmic case and regularization requirements for the square root case. The method avoids reweighting by directly estimating quantities from the value function of the control problem, which is validated through numerical experiments on benchmark committor problems. The approach is nonasymptotic, does not rely on large deviations approximations, and handles unbounded stopping times by formulating indefinite time horizon control problems.  
DOMAIN: molecular dynamics, rare event simulation  
STRUCTURE: other: stochastic control  
DATA_OBJECT: continuous function or field  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: estimation  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: mathematical-proof
