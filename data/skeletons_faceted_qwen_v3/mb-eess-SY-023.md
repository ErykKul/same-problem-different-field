MECHANISM: The paper computes a bi-level optimization model where a leader (regulator) and follower (diesel generator company) interact through strategic decisions. The leader sets upper and lower bounds on price and feed-in tariffs to maximize household economic surplus, subject to constraints ensuring the follower's profitability. The follower then optimizes its own profit by controlling generation schedules, access, and purchases from PV-owners, while adhering to technical and economic constraints. The model incorporates variables representing demand, supply, prices, and constraints on profitability. The leader's objective combines the value of met demand and PV feed-in, discounted over time. The follower's objective maximizes net present value of profits, penalizing unmet demand. Constraints enforce supply-demand balance, capacity limits, and operational feasibility. The model uses representative days weighted by probabilities to capture annual variability. Decision variables include generation schedules, battery usage, and PV installation levels. The solution involves solving nested optimization problems with interdependent constraints. The model explicitly accounts for the DGC's market power and the regulator's limited ability to enforce policies. The computational steps involve defining objective functions, constraints, and solving the bi-level game through iterative or analytical methods.  
DOMAIN: microgrid energy economics  
STRUCTURE: other: game-theoretic optimization  
DATA_OBJECT: set or table  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: optimization  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-private-data
