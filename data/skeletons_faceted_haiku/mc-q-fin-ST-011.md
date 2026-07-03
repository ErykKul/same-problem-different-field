MECHANISM: A transformer-based architecture processes sequences of observed covariance estimates via self-attention layers, outputting hidden states for each token. A pointwise two-layer MLP head maps each hidden state to a scalar residual correction for the singular values of the covariance matrix. The corrected singular values are reconstructed into a cleaned cross-covariance matrix through SVD. The system is trained on lagged cross-correlation matrices to minimize out-of-sample prediction error via squared Frobenius loss. The model learns to filter noise and adjust spectral properties of estimated covariance matrices through additive corrections to singular values, generalizing a nonlinear extension of basic shrinkage methods.
DOMAIN: Covariance matrix estimation
STRUCTURE: spectral or transform
DATA_OBJECT: dense matrix or tensor
INFERENCE: optimization only
PROBLEM_FORM: estimation
DISTRIBUTION: none
COMPLEXITY: polynomial iterative
