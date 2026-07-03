MECHANISM: The paper computes a reparameterized tensor ring functional decomposition to model high-dimensional data. It begins by representing a tensor as a product of third-order core tensors under cyclic constraints. Each core is parameterized by an implicit neural representation (INR) that maps continuous coordinates to latent factor values. A frequency-domain analysis reveals that the spectral properties of the core tensors determine the frequency composition of the reconstructed tensor, limiting high-frequency modeling. To address this, the method reparameterizes each core as a structured combination of a learnable latent tensor and a fixed basis matrix. This reparameterization is shown to improve training dynamics by amplifying gradients for high-frequency components. The fixed basis is initialized using a principled scheme to ensure variance consistency during optimization. The latent tensor is generated through a neural network that maps coordinates to slices, which are then contracted with the fixed basis to form the core tensors. The overall model is trained to minimize a loss function combining data fidelity and optional regularization terms. Theoretical guarantees include Lipschitz continuity of the model and convergence properties of the optimization. The method is evaluated on tasks like image inpainting and super-resolution, demonstrating superior performance over existing approaches.  
DOMAIN: signal processing and machine learning  
STRUCTURE: other: tensor decomposition with neural networks  
DATA_OBJECT: tensor  
INFERENCE: optimization only  
PROBLEM_FORM: recovery  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: public-repository  
CODE_AVAILABILITY: public-repository  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
