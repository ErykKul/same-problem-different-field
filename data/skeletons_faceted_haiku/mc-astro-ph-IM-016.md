MECHANISM: Given data compressed by a base compressor (spatial domain) and user-defined error bounds in both spatial and frequency domains, the algorithm models frequency-domain errors as linear combinations of spatial-domain errors via Discrete Fourier Transform. An alternating projection method iteratively projects the spatial error vector onto two geometric regions: an axis-aligned hypercube (s-cube) from spatial error bounds and a rotated hypercube (f-cube) from frequency-domain constraints via DFT. When convergence is reached, edits to the decompressed data are extracted, quantized, and compressed to enforce dual-domain accuracy.
DOMAIN: Data compression; signal processing; numerical methods
STRUCTURE: spectral or transform
DATA_OBJECT: dense matrix or tensor
INFERENCE: deterministic or closed-form
PROBLEM_FORM: optimization
DISTRIBUTION: none
COMPLEXITY: not stated
