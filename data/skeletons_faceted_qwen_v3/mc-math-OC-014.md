MECHANISM: The paper computes a scalable algorithm for mean field control problems involving nonlocal interactions through kernel functions. The method replaces quadratic-cost kernel evaluations with linear-time estimates using random Fourier features (RFF). The algorithm proceeds by approximating the kernel $K(x-y)$ with a finite-dimensional random feature map $\Phi(x)$, transforming the convolution $(K \star \mu)(x)$ into an inner product between $\Phi(x)$ and an aggregated feature vector. This reduces the computational complexity of evaluating interaction terms from $O(N^2)$ to $O(NM)$, where $M$ is the number of random features. The aggregated feature vector is computed by averaging $\Phi(x_j)$ over all particles $j$, enabling efficient stochastic gradient descent for training feedback controls. The method integrates this approximation into particle-based simulations of mean field dynamics, allowing decentralized control policies that depend only on individual agent states. Theoretical complexity bounds are derived, and numerical experiments validate the approach on pedestrian and flocking models, demonstrating reduced computational cost while preserving control performance. The algorithm combines particle approximations of population distributions with RFF-based kernel approximations, and applies deep learning techniques for high-dimensional control.  
DOMAIN: mean field control with kernel interactions  
STRUCTURE: sparse linear algebra  
DATA_OBJECT: point set  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: optimization  
DISTRIBUTION: none  
COMPLEXITY: polynomial iterative  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-private-data
