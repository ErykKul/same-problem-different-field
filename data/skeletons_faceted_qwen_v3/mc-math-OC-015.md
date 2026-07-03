MECHANISM: This paper computes a global optimization problem by reformulating it as a regularized stochastic control problem. The objective function is approximated through a family of controlled stochastic differential equations (SDEs) with a regularization term penalizing large control values. Dynamic programming is applied to derive the associated Hamilton–Jacobi–Bellman (HJB) equations, which are nonlinear partial differential equations (PDEs). A Cole–Hopf transformation linearizes the HJB equations into backward heat equations, enabling probabilistic solutions via the Feynman–Kac formula. The value function is represented as an expectation over stochastic processes, and optimal controls are derived using gradient-like expressions conditioned on the state process. For optimization over probability measures, the problem is approximated by a mean-field control formulation with a master equation, which is further discretized into an $N$-particle system. The solution to the master equation is approximated by solving a finite-dimensional HJB equation for the particle system, again using the Cole–Hopf transformation and Feynman–Kac formula. Monte Carlo methods are employed to simulate the controlled SDEs and compute expectations, leading to derivative-free numerical schemes. Convergence guarantees are established as the regularization parameter approaches zero and the particle count tends to infinity, with error bounds involving logarithmic terms in the regularization parameter and inverse linear terms in the particle count. The method is validated through numerical experiments demonstrating convergence to the global minimum of the original objective function.  
DOMAIN: stochastic control for optimization  
STRUCTURE: dynamic programming  
DATA_OBJECT: point set  
INFERENCE: sampling or Monte-Carlo  
PROBLEM_FORM: optimization  
DISTRIBUTION: none  
COMPLEXITY: convergence rate  
DATA_AVAILABILITY: public-repository  
CODE_AVAILABILITY: public-repository  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
