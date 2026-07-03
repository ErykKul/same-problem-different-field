MECHANISM: The paper computes a federated inverse reinforcement learning framework that fuses locally estimated reward functions using an entropically regularized Wasserstein barycenter. Each client performs a lightweight Maximum Entropy IRL to estimate a reward function from its local data, which is represented as a linear function over a shared state-action space. These local reward functions are normalized into probability distributions over a common lattice, ensuring alignment across clients. The normalized distributions are then aggregated via a Wasserstein barycenter, which computes a geometrically aware average by minimizing a transportation cost between the distributions. This barycenter is entropically regularized to ensure computational tractability and stability. The resulting fused distribution is projected back to the original parameter space using least squares in a shared feature basis, enabling clients to contribute without sharing raw data or trajectories. The method guarantees stability and parameter-error bounds under bounded local estimation errors, ensuring convergence toward the true reward function. The fusion process preserves spatial structure, reduces artifacts from underfit local estimates, and produces a semantically consistent global reward. The algorithm operates iteratively, with each client performing local optimization and the server aggregating results through the barycenter computation. The method is designed to be communication-efficient, requiring only the exchange of normalized reward distributions rather than raw data or full model parameters. The theoretical analysis establishes that the barycentric fusion contracts toward the true reward function under heterogeneity and limited computational resources on clients.  
DOMAIN: federated inverse reinforcement learning  
STRUCTURE: other: optimal transport  
DATA_OBJECT: probability distribution  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: estimation  
DISTRIBUTION: continuous; probability distribution  
COMPLEXITY: finite-sample bound  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-private-data
