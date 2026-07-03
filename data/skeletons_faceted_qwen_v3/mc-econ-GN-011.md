MECHANISM: The paper computes a dynamic interaction model between three quantities using a generalized Lotka-Volterra framework. It begins by defining a system of differential equations with parameters representing growth rates, self-limitation, and cross-quantity interactions. Observations are transformed into a discrete-time format for regression analysis, estimating parameters through zero-intercept regression. The model identifies equilibrium points by solving for steady-state conditions where time derivatives vanish. Stability is assessed via eigenvalues of the Jacobian matrix derived from linearizing the system around equilibria. Sensitivity analysis quantifies how parameter uncertainty propagates to equilibrium outcomes using Sobol indices. The method involves partitioning variance into first-order and total-order contributions for each parameter. Results include equilibrium values, stability classifications, and sensitivity rankings. All computations are deterministic, relying on algebraic solutions and numerical simulations rather than probabilistic inference. The model's structure is defined by nonlinear differential equations with interaction terms, and parameters are estimated from time-series data through regression. The analysis focuses on quantifying interaction strengths, equilibrium stability, and parameter influence on long-term outcomes.  
DOMAIN: economic modeling  
STRUCTURE: other: differential equations  
DATA_OBJECT: sequence or time-series  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: estimation  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-private-data
