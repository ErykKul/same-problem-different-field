MECHANISM: The paper computes a method for estimating gradients in neural networks by restricting perturbations to a low-dimensional manifold. It begins by estimating an orthonormal basis for the neural manifold using incremental PCA. Noise is then sampled in the low-dimensional subspace defined by this basis and projected into the full activation space. The resulting perturbations are used to compute output changes, which are correlated with the perturbations to update feedback weights via an exponential moving average. These feedback weights are then used to compute pseudo-errors at each layer, which guide forward weight updates through local gradient descent. The method leverages the observation that the Jacobian's row space aligns with the neural manifold, reducing the effective dimensionality of the estimation problem. This alignment allows perturbations to be concentrated along functionally relevant directions, improving sample efficiency and gradient alignment compared to isotropic noise methods. Theoretical analysis shows that the expected feedback weight updates depend on the noise covariance and the Jacobian, with NMNC producing pseudo-gradients that are scaled by the manifold's structure. Empirical validation demonstrates that this approach improves performance and sample efficiency across various network architectures and datasets.
DOMAIN: neural networks and credit assignment
STRUCTURE: spectral or transform
DATA_OBJECT: dense matrix or tensor
INFERENCE: deterministic or closed-form
PROBLEM_FORM: estimation
DISTRIBUTION: none
COMPLEXITY: not stated
DATA_AVAILABILITY: public-benchmark-used
CODE_AVAILABILITY: none
PREREGISTRATION: none
EVIDENCE_BASIS: empirical-with-released-data
