MECHANISM: The paper computes an American option pricing method using dynamic programming with Chebyshev polynomial interpolation. In an offline phase, generalized conditional moments are computed via numerical techniques (e.g., Monte Carlo, PDE, or Fourier transform methods) for a given asset price model. These moments are then used to construct a discrete Chebyshev grid for the value function approximation. During the online phase, backward induction is performed on this grid without requiring conditional expectation calculations. At each time step, the value function is approximated by a closed-form Chebyshev polynomial expansion, which yields the option price, delta, and gamma. The same generalized moments are reused to compute prices for multiple strikes, maturities, and payoff profiles. The method's error bounds are derived through theoretical analysis, and numerical experiments validate convergence rates and computational efficiency compared to least-square Monte Carlo. The approach decouples model-specific computations from the pricing algorithm, enabling flexibility across asset price models. The Chebyshev grid ensures spectral accuracy in the approximation, and the closed-form expressions avoid iterative optimization during the backward induction step. The method's efficiency stems from precomputing moments and leveraging polynomial interpolation for rapid evaluation.  
DOMAIN: financial mathematics  
STRUCTURE: dynamic programming  
DATA_OBJECT: grid or lattice  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: estimation  
DISTRIBUTION: continuous; continuous  
COMPLEXITY: convergence rate  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: simulation-study
