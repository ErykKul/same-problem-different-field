MECHANISM: The paper computes inverse optimal stabilizers for control-affine nonlinear systems constrained to positive states and controls. It begins by defining a strict control Lyapunov function (CLF) that ensures global asymptotic stability. The method modifies conventional $L_gV$-based feedback laws, which assume symmetric input penalties, to accommodate asymmetric costs necessary for positive systems. Two frameworks are introduced: one uses a CLF, stabilizing feedback, and an expander function to amplify control effects away from equilibrium; the other uses a CLF and a contractor function to reduce control effects near equilibrium. The expander function $\Sigma$ satisfies $\Sigma(s) < s$ for $s < 1$ and $\Sigma(s) > s$ for $s > 1$, ensuring stability while preserving positivity. The contractor function $\Theta$ is strictly increasing, maps positive reals to positive reals, and satisfies $\Theta(1) = 1$ with $\Theta'(1) < 1$. A control penalty $\Psi$ is derived from $\Theta$ via integration, ensuring strict convexity and a minimum at equilibrium. The resulting feedback laws are proven to minimize a cost functional that incorporates asymmetric penalties on control and state deviations. The method generalizes to arbitrary dimensions and applies to systems like predator-prey models with positive orthant constraints. Theoretical guarantees include global asymptotic stability and inverse optimality via Hamilton-Jacobi-Bellman characterization.  
DOMAIN: nonlinear control systems  
STRUCTURE: other: inverse optimal control methods  
DATA_OBJECT: continuous function or field  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: control  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: mathematical-proof
