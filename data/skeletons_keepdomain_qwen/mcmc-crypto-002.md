MECHANISM: The paper computes the sampling from a lattice Gaussian distribution using two Metropolis-Hastings (MH) algorithms. The first algorithm, independent MHK, constructs a Markov chain with an independent proposal distribution, where each proposed sample is accepted or rejected based on the ratio of the target lattice Gaussian density to the proposal density. The second algorithm, symmetric SMK, uses a symmetric proposal distribution, ensuring detailed balance. Both algorithms are analyzed for their ergodicity properties, with the independent MHK proven to be uniformly ergodic, converging exponentially fast to the stationary distribution regardless of initial conditions. The convergence rate is quantified using theta series, which relates to the lattice's structure and provides a predictable mixing time. The symmetric SMK is shown to be geometrically ergodic, meaning its convergence rate is polynomial in the number of steps. The analysis involves deriving bounds on the total variation distance between the chain's distribution and the target distribution, leveraging properties of the lattice Gaussian and the proposal mechanisms. The paper does not implement the algorithms computationally but focuses on theoretical guarantees of convergence and mixing time for lattice Gaussian sampling in cryptography.  
DOMAIN: lattice Gaussian sampling in cryptography  
STRUCTURE: other: Markov chain Monte Carlo  
DATA_OBJECT: grid or lattice  
INFERENCE: sampling or Monte-Carlo  
PROBLEM_FORM: simulation or generation  
DISTRIBUTION: continuous; continuous  
COMPLEXITY: convergence rate  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: mathematical-proof
