MECHANISM: The paper computes a curvature-adjusted layer gain metric derived from a second-order expansion of the training objective. This metric quantifies the maximal reducible risk achievable by updating a layer, using the gradient and a regularized Hessian inverse. The gain is normalized into layer quality scores, which drive two convex optimization programs: one for capacity allocation under diminishing returns and another for pruning. The allocation program distributes resources preferentially to high-gain layers via a closed-form "curvature-weighted water-filling" solution, while the pruning program removes parameters from low-gain layers. Both programs are solved via bisection on a dual variable, with complexity O(K log 1/ε). A transfer regret bound is proven, showing allocations remain near-optimal under curvature score drift. The method relies on convexity, Lagrangian duality, and Tikhonov regularization to ensure closed-form solutions and theoretical guarantees. The curvature-adjusted gain is shown to strictly dominate gradient-norm-based scores by incorporating local curvature information. The optimization objectives balance model complexity penalties and data-fit improvements, modeled as concave and convex functions of resource allocation. The framework is grounded in the Minimum Description Length principle, formalizing trade-offs between model complexity and data fit through codelength minimization.  
DOMAIN: machine learning optimization  
STRUCTURE: other: convex optimization  
DATA_OBJECT: dense matrix  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: optimization  
DISTRIBUTION: none  
COMPLEXITY: polynomial iterative  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: mathematical-proof
