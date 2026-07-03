MECHANISM: The paper computes a reformulation of optimization problems involving a quantity subject to constraints on another quantity. It begins by lifting the original problem into a convex optimization framework where variables are represented as combinations of symmetric rank-one tensors. This lifting is achieved by mapping the original problem's constraints and objective into a higher-dimensional space using tensor operations. The method then constructs a convex program over the cone of completely positive tensors by expressing the original problem's constraints as linear equalities involving tensor variables. The dual formulation is derived by transforming the primal problem into a copositive tensor program, leveraging duality properties of conic programming. The approach ensures that the reformulated problem maintains equivalence to the original under mild conditions, such as the feasibility of the dual problem and the validity of strong duality. The method relies on analyzing the recession cone of the feasible set to establish the equivalence between the original problem and its lifted convex formulation. This allows the use of existing numerical methods for conic programming to solve the reformulated problem. The process involves verifying that the constraints of the original problem are compatible with the structure of the completely positive tensor cone, ensuring that the reformulation is valid. The paper also proves that the dual problem is strictly feasible and that strong duality holds under certain assumptions, which guarantees the optimality of solutions derived from the reformulated problem. The overall mechanism combines tensor algebra, convex analysis, and duality theory to transform a non-convex optimization problem into a tractable conic program.  
DOMAIN: polynomial optimization and conic programming  
STRUCTURE: other: convex optimization with tensor variables  
DATA_OBJECT: tensor  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: optimization  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: mathematical-proof
