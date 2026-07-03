MECHANISM: The paper computes a semi-supervised generative adversarial network (GAN) for classifying sparse spike sequences. The method begins by filtering raw signals to isolate spikes, then segments them into non-overlapping windows. A generator maps random noise to synthetic spike sequences using dense layers, transposed convolutions, and activation functions. A discriminator, designed as a shifted-window transformer, processes these sequences with self-attention mechanisms applied locally within fixed-size windows. The discriminator alternates attention boundaries between layers via shifted windows to model cross-window interactions. Semi-supervised learning uses 3% labeled data and 97% unlabeled data, with pseudo-labels generated during training. The model is optimized using Bayesian hyperparameter tuning and validated via Monte Carlo cross-validation. The discriminator outputs class probabilities (Control, Dengue, Zika) through softmax activation. The generator and discriminator are jointly trained to minimize adversarial loss while maximizing classification accuracy on labeled data. The method emphasizes handling sparse, high-frequency spike features through attention-based modeling and maintains performance with minimal supervision.  
DOMAIN: neuronal spike classification  
STRUCTURE: other: generative adversarial network  
DATA_OBJECT: sequence or time-series  
INFERENCE: optimization only  
PROBLEM_FORM: classification  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-private-data
