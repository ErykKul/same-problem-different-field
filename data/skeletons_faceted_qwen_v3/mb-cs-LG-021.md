MECHANISM: The paper computes a spatial-temporal prediction model by first transforming raw input data into a high-dimensional representation through feature, temporal, and spatial embedding layers. The feature embedding maps raw data into a latent space using a fully connected layer. Temporal embedding captures periodic and trend characteristics by defining learnable representations for intraday and intraweek patterns, which are replicated across nodes to form a temporal embedding. Spatial embedding constructs a dynamic weighted adjacency matrix using self-attention on the input data, which is symmetrized to form a valid adjacency matrix. This adjacency matrix is multiplied by a learnable matrix to produce a dynamic weighted graph structure (DWGS) embedding. A spatial-temporal adaptive embedding is introduced to capture hidden spatial relationships, which is concatenated with the DWGS embedding to form a unified spatial embedding. These embeddings are combined with the temporal embedding to form a final hidden representation. The spatial layer uses dimension reduction, self-attention, and dimension elevation to model spatial dependencies efficiently. The temporal layer applies fast Fourier transform (FFT) to decompose the data into frequency components, which are processed independently by real and imaginary parts through parameter-independent MLPs. The inverse FFT reconstructs the temporal features, and a regression layer maps the final output to the predicted values. The model jointly learns spatial and temporal dependencies through these layers to achieve accurate predictions.
DOMAIN: traffic forecasting
STRUCTURE: graphical models
DATA_OBJECT: graph or network
INFERENCE: deterministic or closed-form
PROBLEM_FORM: prediction or classification
DISTRIBUTION: none
COMPLEXITY: not stated
DATA_AVAILABILITY: public-benchmark-used
CODE_AVAILABILITY: public-repository
PREREGISTRATION: none
EVIDENCE_BASIS: empirical-with-released-data
