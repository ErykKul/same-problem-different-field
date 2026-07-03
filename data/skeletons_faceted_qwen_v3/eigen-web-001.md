MECHANISM: This paper computes two generalized variants of Personalized PageRank through Markov chain analysis. It defines a finite-state Markov chain with a transition matrix combining random walk steps and node-dependent restart probabilities. The stationary distribution of this chain is derived analytically, leading to two distinct centrality measures: Occupation-Time Personalized PageRank (long-run visit frequency) and Location-of-Restart Personalized PageRank (restart-associated visit frequency). The computation involves solving linear systems via matrix inversion ([I-AP]^{-1}), deriving closed-form expressions for stationary distributions, and proving symmetry properties under undirected graph assumptions. The method uses probabilistic interpretations of matrix powers as path enumerations, derives asymptotic behaviors for degree-weighted restarts, and connects the results to existing PageRank formulations through parameter specialization. Theoretical guarantees include consistency with Markov chain properties and explicit formulas for both centrality measures.  
DOMAIN: network analysis  
STRUCTURE: dense linear algebra  
DATA_OBJECT: graph or network  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: estimation  
DISTRIBUTION: continuous; continuous  
COMPLEXITY: polynomial iterative  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: mathematical-proof
