MECHANISM: The paper formulates a time-fractional Fisher-KPP equation to model tumor growth, incorporating a Caputo fractional derivative in time to capture subdiffusive dynamics. The equation is derived by replacing the classical first-order time derivative with a fractional-order derivative, which introduces memory effects into the system. The model is analyzed mathematically to establish existence, uniqueness, and stability of solutions under specific conditions. Numerical simulations are performed using a finite difference scheme adapted for fractional derivatives, discretizing both space and time. The spatial domain is approximated with a uniform grid, and the fractional derivative is handled via a weighted sum of past solution values. The simulation tracks the evolution of tumor cell density over time, incorporating nonlinear reaction terms and diffusion coefficients. The method is validated by comparing numerical results with analytical solutions for simplified cases. The paper emphasizes the biological relevance of subdiffusion in heterogeneous tissues and demonstrates how the model captures slower-than-Fickian spreading compared to classical Fisher-KPP. The computational workflow includes parameter calibration based on empirical tumor growth data and sensitivity analysis of the fractional order parameter. The implementation uses explicit time-stepping with adaptive mesh refinement near tumor boundaries. The results are visualized as spatiotemporal heatmaps of cell density and compared to experimental observations in cancer biology literature.
DOMAIN: mathematical biology and tumor growth modeling
STRUCTURE: structured grid
DATA_OBJECT: grid or lattice
INFERENCE: deterministic or closed-form
PROBLEM_FORM: simulation or generation
DISTRIBUTION: none
COMPLEXITY: not stated
DATA_AVAILABILITY: none
CODE_AVAILABILITY: none
PREREGISTRATION: none
EVIDENCE_BASIS: simulation-study
