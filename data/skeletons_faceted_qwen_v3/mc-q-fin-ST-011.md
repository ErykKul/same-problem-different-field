MECHANISM: The paper computes a nonlinear mapping from empirical singular values of a cross-covariance matrix to cleaned values, using a neural network architecture that preserves rotational invariance. The process begins with a singular value decomposition (SVD) of an input matrix, extracting singular values and corresponding singular vectors. Marginal projections are computed by projecting empirical covariance matrices onto these singular vectors. These projections, along with singular values and aspect ratios, are encoded into feature vectors. Two parallel streams process these vectors independently through multi-layer perceptrons (MLPs), producing embeddings that are fused additively. A bidirectional LSTM aggregator then processes the fused sequence to capture global spectral context. A residual correction is applied to the singular values via a pointwise MLP, adjusting them to minimize a Frobenius loss relative to an out-of-sample target. The cleaned singular values are recombined with the original singular vectors to reconstruct the estimated cross-covariance matrix. The architecture is designed to recover an analytical shrinkage solution as a special case while adapting to non-stationary dynamics through learned parameters. Training involves minimizing the mean squared error between predicted and observed cross-covariance matrices over rolling windows of data. The method explicitly enforces symmetry constraints implied by random matrix theory and avoids introducing spurious structure by operating in the empirical singular-vector basis.  
DOMAIN: financial econometrics  
STRUCTURE: other: neural network  
DATA_OBJECT: matrix  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: estimation  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: public-repository  
CODE_AVAILABILITY: public-repository  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
