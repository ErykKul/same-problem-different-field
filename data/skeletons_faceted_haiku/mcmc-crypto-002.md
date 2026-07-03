MECHANISM: Design Metropolis-Hastings algorithms to sample from discrete lattice Gaussian distributions. The independent MHK algorithm generates candidate lattice points using Klein's algorithm (which samples from a Gaussian-like distribution over the lattice), then applies the Metropolis-Hastings acceptance rule based on the ratio of target densities. The symmetric MK variant uses a symmetric proposal distribution. Prove that the induced Markov chains converge exponentially fast to the target distribution by analyzing ergodicity properties. For the independent MHK algorithm, establish uniform ergodicity using coupling arguments and spectral gap analysis. Derive explicit convergence rates in terms of theta series. For the symmetric MK algorithm, prove geometric ergodicity. Analyze mixing times and computational complexity in relation to the standard deviation parameter.
DOMAIN: Cryptography, lattice-based cryptography, computational number theory
STRUCTURE: graphical models
DATA_OBJECT: point set or hierarchy
INFERENCE: sampling or Monte-Carlo
PROBLEM_FORM: sampling or generation
DISTRIBUTION: none
COMPLEXITY: polynomial iterative
