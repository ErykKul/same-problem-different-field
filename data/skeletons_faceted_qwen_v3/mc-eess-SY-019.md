MECHANISM: The paper computes a method to enhance autoencoder and variational autoencoder (VAE) models by integrating Random Fourier Transformation (RFT) as a preprocessing layer. The transformation maps input data into a feature space defined by random sinusoidal basis functions, enabling the model to capture both low- and high-frequency components simultaneously. The RFT layer is implemented as two shared-weight convolutional layers with kernel size 1, applying sine and cosine activation functions to expand input channels into predefined Fourier features. These features are concatenated to form the transformed representation, which is then fed into the encoder of the autoencoder or VAE. The model is trained using backpropagation, optimizing parameters of the RFT layer (specifically the frequency parameters $b_i$) alongside the encoder and decoder. For VAEs, the loss function combines a reconstruction error (measured via a likelihood term) and a regularization term (KL divergence between the learned latent distribution and a prior). The method is evaluated on synthetic low-dimensional datasets and a high-dimensional aviation safety dataset, comparing performance between fixed-random RFT, trainable RFT, and conventional autoencoders/VAEs. The analysis includes frequency principle (F-Principle) decomposition to study how models learn different frequency components during training. The paper investigates whether trainable RFT improves over fixed RFT in capturing high-frequency patterns and reducing spectral bias in neural networks.  
DOMAIN: machine learning, anomaly detection  
STRUCTURE: spectral or transform  
DATA_OBJECT: dense matrix or tensor  
INFERENCE: Bayesian posterior  
PROBLEM_FORM: detection or test  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: dataset-in-repository  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-private-data
