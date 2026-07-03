MECHANISM: The paper computes a modified Black-Scholes partial differential equation (PDE) that incorporates asymmetric funding costs for long and short option positions. The PDE includes nonlinear terms representing funding asymmetry, leading to a free boundary between regions where secured and unsecured financing apply. The solution uses an iterative Crank-Nicholson finite difference method to solve the PDE for European and American options. The algorithm alternates between solving the PDE in regions with and without unsecured financing, enforcing continuity of option price and delta across the free boundary. For each time step, the method updates the funding boundary based on the previous iteration's solution. The PDE's coefficients depend on parameters like repo rates, haircut fractions, and unsecured borrowing rates. The solution enforces self-financing constraints by balancing cash flows from repo accounts, debt accounts, and option positions. The method handles both European and American options by incorporating early exercise boundaries in the finite difference grid. The final output is the option price as a function of time and underlying asset value, adjusted for funding costs.  
DOMAIN: finance, option pricing, market making  
STRUCTURE: other: partial differential equation  
DATA_OBJECT: continuous function or field  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: estimation  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
