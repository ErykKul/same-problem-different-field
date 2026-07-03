MECHANISM: Improve autoencoders and variational autoencoders for reconstruction-based anomaly detection by prepending a Random Fourier Transformation layer to the input. The RFT layer maps input data using random combinations of sinusoidal basis functions: sine and cosine terms weighted by random frequency parameters. This expands input features into a Fourier feature space before the encoder processes them. Optionally, introduce trainable variants where frequency parameters are optimized via backpropagation. Encode input to low-dimensional latent space and reconstruct. For VAEs, optimize the evidence lower bound combining reconstruction loss and KL divergence regularization. Use reconstruction error as anomaly score at test time.
DOMAIN: Deep learning and anomaly detection
STRUCTURE: other: autoencoder with spectral transformation
DATA_OBJECT: continuous function or field
INFERENCE: Bayesian posterior
PROBLEM_FORM: estimation
DISTRIBUTION: continuous; latent Gaussian assumption
COMPLEXITY: not stated
