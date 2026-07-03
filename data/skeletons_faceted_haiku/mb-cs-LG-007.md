MECHANISM: Transformer multi-head self-attention is reformulated by replacing scaled dot-product operations with sparse Gaussian process posteriors in the output space. A learned symmetric kernel replaces the standard dot-product similarity computation, and sparse GP techniques approximate posterior processes directly within attention blocks. The connection between dot-product attention and the posterior mean of sparse GPs is identified and used to enable uncertainty-calibrated attention inference. The full Transformer backbone is trained end-to-end with these modified attention mechanisms while preserving compatibility with standard deep learning optimization and achieving competitive predictive accuracy.

DOMAIN: deep learning, uncertainty quantification, transformers

STRUCTURE: dense linear algebra

DATA_OBJECT: dense matrix or tensor

INFERENCE: Bayesian posterior

PROBLEM_FORM: prediction or classification

DISTRIBUTION: continuous

COMPLEXITY: not stated
