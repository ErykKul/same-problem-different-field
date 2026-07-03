MECHANISM: The paper computes an approximation algorithm for maximizing a non-monotone γ-weakly DR-submodular function over a convex set. The algorithm operates in two phases: a γ-aware Frank–Wolfe–guided continuous greedy step and a γ-aware double–greedy step. The Frank–Wolfe component iteratively selects directions within the convex set that maximize the gradient of the objective function, while the double–greedy component maintains two solutions (upper and lower bounds) and adjusts them to resolve conflicts between inclusion and exclusion of coordinates. The algorithm introduces γ-dependent thresholds and progress certificates to balance ascent along Frank–Wolfe directions with measured updates, ensuring feasibility and monotonic decay of the residual gap. A convex mixture of certificates from both phases is optimized to produce a performance curve Φ_γ that strictly improves prior bounds for γ ∈ (0,1) while matching the DR boundary at γ=1. The method relies on first-order information and linear optimization over the convex set, avoiding projections and curvature assumptions. Key technical steps include deriving γ-weighted inequalities for weakly DR-submodular functions, proving bounds on the relationship between function values at join/meet points, and combining these with polynomial-time solvable convex body properties to achieve the final approximation guarantees.  
DOMAIN: optimization and theoretical computer science  
STRUCTURE: other: hybrid optimization framework  
DATA_OBJECT: convex set  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: optimization  
DISTRIBUTION: none  
COMPLEXITY: polynomial iterative  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: mathematical-proof
