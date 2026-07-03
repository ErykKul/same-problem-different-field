MECHANISM: The paper derives a mathematical relationship between mutual information and minimum mean-square error (MMSE) in the context of Viterbi decoding for convolutional codes. It models a binary input signal transmitted over an AWGN channel using BPSK modulation, where the signal is characterized by a given signal-to-noise ratio (SNR) and equiprobable binary symbols. The soft-decision input to the main decoder is treated as an innovation, defined through the lens of mutual information and MMSE. The MMSE is expressed as a function of the distribution of the encoded block for the main decoder, leveraging properties of Gaussian channels. The paper shows that this derived MMSE satisfies the known relationship between mutual information and MMSE in Gaussian channels, thereby validating the innovation assumption. The analysis connects the input-output mutual information with the distribution of the encoded block, demonstrating that the soft-decision input's statistical properties align with the innovation framework. The derivation relies on signal model assumptions, SNR parameters, and the structure of convolutional codes. No explicit algorithmic steps for decoding are described, but the focus is on theoretical validation of the MMSE-mutual information relationship. The paper does not introduce new computational methods beyond the mathematical derivation of these relationships.  
DOMAIN: information theory and coding theory  
STRUCTURE: other: mathematical derivation  
DATA_OBJECT: continuous function or field  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: estimation  
DISTRIBUTION: binary and continuous  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: mathematical-proof
