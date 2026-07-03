MECHANISM: The paper computes the minimum mean-square error (MMSE) in estimating a binary input signal from a noisy observation, using the distribution of an encoded block. The process begins by deriving the joint probability distribution of the input to the main decoder, which is modeled as a combination of Gaussian noise and binary signal components. The covariance matrix of the input is calculated from this joint distribution. The covariance matrix of the estimation error is then obtained by subtracting the covariance matrix of the observation noise from the input covariance matrix. The MMSE is derived as the trace of this resulting covariance matrix, which quantifies the sum of diagonal elements representing the variance of the estimation error. The paper connects this MMSE to the mutual information between the input and output of the system, leveraging known relationships in Gaussian channels. The computation involves statistical decomposition of covariance matrices, trace operations, and probabilistic modeling of the encoded block's distribution. The soft-decision input is validated as an innovation by showing that the derived MMSE satisfies the theoretical relationship between mutual information and MMSE. The method relies on Gaussian assumptions for noise and binary assumptions for the signal, with the final MMSE expressed as a function of the encoded block's distribution. The paper also discusses numerical validation using convolutional codes to compare causal and noncausal estimation scenarios.  
DOMAIN: coding theory  
STRUCTURE: dense linear algebra  
DATA_OBJECT: dense matrix  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: estimation  
DISTRIBUTION: binary; Gaussian  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: mathematical-proof
