MECHANISM: The paper computes a Markov chain Monte Carlo (MCMC) sampling process to generate high-quality and diverse translations from a language model. It defines a Gibbs distribution over translation hypotheses, where the energy function is derived from an external quality metric. The Metropolis-Hastings algorithm is used to sample from this distribution, iteratively proposing new hypotheses by modifying parts of the current hypothesis and accepting or rejecting them based on a temperature-scaled quality difference. The proposal distribution generates a new hypothesis by sampling a position in the sequence and completing the remaining tokens using the language model. This process ensures exploration of high-density regions in the hypothesis space while maintaining diversity. The algorithm operates on sequences of tokens, using a temperature parameter to balance exploration and exploitation. The acceptance probability depends on the ratio of quality scores between the proposed and current hypotheses, normalized by the temperature. The method avoids direct optimization of the quality metric, instead relying on sampling to approximate the target distribution. It does not assume a specific form for the quality metric, allowing compatibility with any evaluation function. The process is repeated for a fixed number of steps, with the final samples forming the output set. The method is designed to overcome limitations of greedy decoding and reranking approaches by avoiding over-reliance on single high-quality hypotheses.  
DOMAIN: machine translation  
STRUCTURE: other: Markov chain Monte Carlo  
DATA_OBJECT: sequence or time-series  
INFERENCE: sampling or Monte-Carlo  
PROBLEM_FORM: simulation or generation  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: public-benchmark-used  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
