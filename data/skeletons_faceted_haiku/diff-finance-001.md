MECHANISM: Extend the Black-Scholes-Merton diffusion partial differential equation to account for realistic funding costs and financing constraints faced by an agent. Model separate rates for cash borrowing versus lending, haircut requirements for collateral, and repo financing costs. Set up a self-financing wealth balance with repo and debt accounts. Derive asymmetric PDEs for long and short positions, defining a free boundary in the domain where funding regimes change. Solve the nonlinear PDE numerically using an iterative Crank-Nicholson finite difference scheme.
DOMAIN: Mathematical finance and option pricing theory
STRUCTURE: spectral or transform
DATA_OBJECT: continuous function or field
INFERENCE: deterministic or closed-form
PROBLEM_FORM: simulation or generation
DISTRIBUTION: none
COMPLEXITY: polynomial iterative
