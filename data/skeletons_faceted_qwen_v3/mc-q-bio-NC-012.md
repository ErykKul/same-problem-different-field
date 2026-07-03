MECHANISM: The paper computes a hierarchical decomposition of temporal sequences using deep neural networks with scale-invariant dynamics. A feedforward network (SITHCon) is trained to classify hierarchical symbolic sequences, where each layer spontaneously organizes into distinct temporal receptive windows (TRWs) despite uniform time constants. Temporal scrambling analysis quantifies TRW scales by measuring correlation drops under input permutations. A recurrent architecture (SITH-RNN) is derived by enforcing block-diagonal weight matrices, tensor product structures, and geometric eigenvalues to separate feature identity ("what") from temporal context ("when"). Recurrent dynamics are constrained to produce scale-invariant activity through diagonal recurrent matrices with geometrically distributed time constants. Readout weights use banded (Toeplitz) matrices to generate translated eigenvectors, enabling sequential activation patterns. Training on hierarchical sequences reveals that deeper layers develop abstract, compositional receptive fields spanning multiple scales. Zero-shot generalization is achieved by freezing geometric eigenvalues and restricting readout motifs to fixed-width temporal patterns, allowing the network to recognize hierarchical structures across arbitrary time rescalings without explicit segmentation cues.  
DOMAIN: computational neuroscience  
STRUCTURE: other: recurrent neural networks with scale-invariant dynamics  
DATA_OBJECT: sequence or time-series  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: classification  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-private-data
