MECHANISM: Develop a tube-based robust nonlinear model predictive control (NMPC) framework that decomposes the control problem into a nominal unconstrained system and an auxiliary disturbance-rejection system. Solve two coupled optimization problems: the nominal problem minimizes output tracking error while the auxiliary problem minimizes deviations from the nominal solution under bounded model uncertainties. Recursively update the nominal initial conditions to incorporate feedback about real system states, forming time-varying constraint tubes that guarantee recursive feasibility and constraint satisfaction.
DOMAIN: Model predictive control for anaerobic digestion with uncertain parameters and partial observability
STRUCTURE: dynamic programming
DATA_OBJECT: none
INFERENCE: optimization only
PROBLEM_FORM: control
DISTRIBUTION: none
COMPLEXITY: polynomial iterative
