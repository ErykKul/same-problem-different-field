MECHANISM: The paper computes an optimization algorithm for minimizing a function $ f(x) $ under Markovian noise using zero-order information. The method approximates gradients via finite differences, querying the function at two points along a random direction to estimate directional derivatives. To handle Markovian noise, the algorithm employs batching techniques that reduce variance by averaging over multiple samples from the noise process. The key innovation involves partitioning the Markov chain into subchains, reducing temporal correlation, and reconstructing the full gradient coordinate-wise. This approach achieves a complexity bound that depends on both the dimension $ d $ and the mixing time $ \tau $ of the noise process. The algorithm uses a smoothed version of the objective function to mitigate non-smoothness, leveraging the fact that the expectation of the finite-difference estimator aligns with the gradient of the smoothed function. The method is analyzed for both smooth and non-smooth cases, with theoretical guarantees on convergence rates and oracle complexity. The paper also establishes information-theoretic lower bounds, showing that the proposed algorithm is optimal up to logarithmic factors. The computational steps include gradient estimation, variance reduction through batching, and acceleration via coordinate-wise subchain partitioning. The algorithm operates in a stochastic setting where the noise is not independent but follows a Markovian structure, requiring specialized handling of temporal dependencies.  
DOMAIN: optimization with Markovian stochasticity  
STRUCTURE: other: stochastic optimization with Markovian noise  
DATA_OBJECT: continuous function or field  
INFERENCE: optimization only  
PROBLEM_FORM: optimization  
DISTRIBUTION: continuous; bounded  
COMPLEXITY: finite-sample bound  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: mathematical-proof
