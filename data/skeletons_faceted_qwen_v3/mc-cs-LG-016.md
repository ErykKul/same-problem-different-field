MECHANISM: The paper computes a generative model that combines a conditional variational autoencoder (CVAE) with latent-space constraints and Gaussian process (GP) completion. The CVAE learns a low-dimensional latent representation of spatiotemporal data by maximizing a variational lower bound on the conditional likelihood of observations given input features. To enforce consistency across multiple realizations, the model introduces a penalty term that aligns latent embeddings at predefined anchor points across different realizations. After training, the latent space is completed using a multi-output GP regressor, which maps local neighborhood features (derived from nearest-neighbor latent codes) to dense latent coordinates for unseen locations. These predicted latent coordinates are then decoded into full realizations of the observed quantities. The method involves training separate CVAEs per realization, applying alignment constraints, and using sparse variational inference for GP prediction. The workflow includes encoding, latent-space completion, and decoding steps, with evaluation based on reconstruction error and latent-space neighbor distances. The approach addresses fragmentation in jointly trained CVAEs by enforcing cross-realization homogeneity through anchor points and GP extrapolation.  
DOMAIN: climate modeling and generative AI  
STRUCTURE: other: conditional variational autoencoder with Gaussian process completion  
DATA_OBJECT: grid or lattice  
INFERENCE: Bayesian posterior  
PROBLEM_FORM: simulation or generation  
DISTRIBUTION: continuous; Gaussian  
COMPLEXITY: not stated  
DATA_AVAILABILITY: public-benchmark-used  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-private-data
