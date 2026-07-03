MECHANISM: The paper computes a dynamic programming solution to an optimal stopping problem using Chebyshev polynomial interpolation. At each time step, the value function is approximated by a finite sum of Chebyshev polynomials, with coefficients determined via a linear combination of function values at Chebyshev grid points. The method separates computation into an offline phase, where generalized conditional moments (expectations of Chebyshev polynomials conditioned on grid points) are precomputed using numerical techniques like Monte Carlo or PDE solvers, and an online phase, where backward induction is performed on the discrete Chebyshev grid without explicitly computing conditional expectations. The value function is represented as a closed-form approximation using Chebyshev polynomials, enabling efficient computation of option prices, deltas, and gammas. The algorithm iteratively applies this process across time steps, leveraging the exponential convergence properties of Chebyshev interpolation for analytic functions. Error bounds are derived by decomposing the total error into contributions from Chebyshev interpolation, distortion at grid points, and numerical approximation of generalized moments. The method's modularity allows reuse of precomputed moments for multiple payoff profiles, strikes, and maturities.  
DOMAIN: financial mathematics, option pricing  
STRUCTURE: dynamic programming  
DATA_OBJECT: grid or lattice  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: estimation  
DISTRIBUTION: continuous; analytic  
COMPLEXITY: polynomial iterative  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: simulation-study
