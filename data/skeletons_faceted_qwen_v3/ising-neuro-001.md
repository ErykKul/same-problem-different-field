MECHANISM: The paper computes a stimulus-dependent maximum entropy (SDME) model to estimate the conditional probability distribution over neural codewords given an input. The model extends the linear-nonlinear framework by introducing pairwise interactions between units, capturing dependencies through a set of parameters that maximize entropy under constraints derived from observed data. These constraints include first- and second-order moments of the codeword distribution, such as mean firing rates and pairwise correlations. The algorithm iteratively adjusts parameters to satisfy these constraints while ensuring the distribution remains as uniform as possible. The model's parameters are estimated using optimization techniques that balance entropy maximization with fidelity to empirical statistics. The resulting distribution is used to predict the likelihood of codewords under different stimuli, enabling inference of neural coding properties. The method assumes that higher-order interactions are negligible, focusing on pairwise couplings to simplify computation. The model's accuracy is validated by comparing predicted codeword distributions to empirical data, quantifying improvements over uncoupled models. The approach does not explicitly model temporal dynamics or incorporate explicit stimulus features beyond the input's influence on codeword statistics.  
DOMAIN: computational neuroscience, neural coding  
STRUCTURE: graphical models  
DATA_OBJECT: sequence or time-series  
INFERENCE: optimization only  
PROBLEM_FORM: estimation  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-private-data
