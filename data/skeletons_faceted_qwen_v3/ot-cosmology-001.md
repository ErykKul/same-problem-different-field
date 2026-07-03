MECHANISM: The paper computes a reconstruction of an initial state by solving an optimization problem that minimizes a cost functional defined over a space of density fields and velocity fields. The method enforces constraints derived from observed data, such as the final distribution of entities, and incorporates a regularization term to ensure uniqueness. The optimization is performed iteratively, using gradient-based updates to adjust the density and velocity fields toward a configuration that satisfies both the observed data and the physical laws governing the evolution of the system. The algorithm alternates between updating the density field to match the observed distribution and adjusting the velocity field to minimize the transport cost. The cost functional is designed to penalize deviations from a reference model, ensuring that the reconstructed initial state is consistent with cosmological principles. The method avoids explicit modeling of uncertainties by treating the problem as a deterministic inverse problem. The solution is validated by comparing the simulated evolution of the reconstructed state to the observed data, ensuring that the final distribution matches the target. The algorithm's convergence is guaranteed under certain conditions on the cost functional and the constraints. The method does not rely on probabilistic assumptions or sampling techniques, instead focusing on finding a single optimal solution. The computational steps are generic and applicable to any system where the evolution is governed by a known transformation from initial to final states.  
DOMAIN: cosmology  
STRUCTURE: other: optimization-based  
DATA_OBJECT: continuous function or field  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: estimation  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: public-benchmark-used  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: simulation-study
