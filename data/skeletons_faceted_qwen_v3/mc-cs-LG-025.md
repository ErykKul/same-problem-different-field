MECHANISM: The paper computes the evolution of a kernel matrix governed by an ordinary differential equation (ODE) derived from a convex loss function and regularization. The ODE describes the competition between a task-specific drive operator and isotropic decay. The drive operator compresses the kernel into a low-dimensional subspace aligned with the task, following a "water-filling" spectral law. This compression is enforced by the architecture and loss function, independent of time-scale separation. The analysis shows that stable steady states have rank at most C, where C is the output dimension. Stochastic gradient descent (SGD) noise is confined to a low-rank subspace determined by C, restricting diffusion to task-relevant directions. The framework extends to population limits and self-supervised learning via graph Laplacian and log-det repulsion, producing high-rank, Laplacian-aligned kernels. The results unify supervised compression and self-supervised expansion through spectral analysis. The ODE is derived for squared loss, with general convex losses yielding similar rank compression but not closed-form spectral trajectories. The analysis relies on gradient flows, matrix inversion, and spectral decomposition of the kernel and label Gram matrix.  
DOMAIN: machine learning, neural networks, kernel methods  
STRUCTURE: other: differential equations  
DATA_OBJECT: dense matrix  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: estimation  
DISTRIBUTION: none  
COMPLEXITY: convergence rate  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: mathematical-proof
