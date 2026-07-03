MECHANISM: The paper modifies the Black-Scholes partial differential equation (PDE) to incorporate asymmetric funding costs for long and short positions in options. It introduces nonlinear terms representing the difference between unsecured debt rates for borrowed cash and risk-free rates for invested cash. The modified PDEs are derived separately for long and short positions, accounting for varying margin requirements and haircuts. The resulting equations include a free boundary condition that determines the threshold at which funding costs affect the bid-ask spread. The solution involves solving the PDEs with boundary conditions that enforce self-financing of the replicating portfolio. The model demonstrates that dynamic replication remains possible even with funding asymmetry, but the bid price for options is adjusted to reflect the market maker's financing costs. The derivation relies on continuous-time stochastic calculus and assumes geometric Brownian motion for the underlying asset. The paper does not propose numerical methods for solving the PDEs but focuses on the analytical extension of the original theory. The modified equations are validated through theoretical consistency checks rather than empirical data.  
DOMAIN: financial mathematics, option pricing theory  
STRUCTURE: other: partial differential equations  
DATA_OBJECT: partial differential equation  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: estimation  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: mathematical-proof
