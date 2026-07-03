MECHANISM: The paper computes a sequence-to-sequence prediction task using multiple deep learning architectures. Input sequences of length $k$ are processed through a model that applies a series of transformations to capture temporal dependencies. For recurrent models, hidden states are updated via gated operations that modulate memory retention and input integration. Attention mechanisms compute weighted combinations of past states using learned projection matrices and softmax normalization. Convolutional layers apply causal dilated convolutions to model long-range dependencies with sparse parameterization. Transformer blocks use multi-head self-attention with scaled dot products and residual connections to aggregate contextual information. Predictions are generated through linear projections of aggregated representations. A separate trading module evaluates directional price changes by computing signed differences between consecutive observations and their second-order differences to trigger buy/sell decisions based on predefined thresholds. All models are trained with Adam optimization and evaluated under identical hyperparameters without architecture-specific tuning. Performance is measured through autoregressive and teacher-forced prediction modes, with trading outcomes assessed via portfolio value trajectories.  
DOMAIN: financial time-series forecasting  
STRUCTURE: other: neural network architectures  
DATA_OBJECT: sequence or time-series  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: prediction or classification  
DISTRIBUTION: continuous; continuous  
COMPLEXITY: not stated  
DATA_AVAILABILITY: dataset-with-DOI-or-handle  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
