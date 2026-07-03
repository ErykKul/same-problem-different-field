MECHANISM: The paper computes a neural network architecture that transforms input identifiers (for entities) into dense vector representations through embedding layers. These embeddings are concatenated and processed by a multi-layer perceptron (MLP) with dropout regularization to capture non-linear interactions between entity representations. The final layer applies a softmax activation to produce a probability distribution over discrete rating categories (e.g., 1–5 stars). The model trains by minimizing categorical cross-entropy loss between predicted probabilities and true labels. Input identifiers are mapped to dense vectors via lookup tables, where similar entities receive similar vector representations. The architecture avoids explicit one-hot encoding by using compressed embeddings. Predictions are made as probability distributions over rating categories, with the highest-probability category serving as the discrete prediction. Reliability is inferred from the magnitude of the corresponding probability value. The model is trained using gradient descent with the Adam optimizer, and evaluation metrics include precision, recall, and mean absolute error. The approach is compared to regression-based baselines using public benchmark datasets.  
DOMAIN: recommender systems  
STRUCTURE: other: neural network  
DATA_OBJECT: set or table  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: prediction or classification  
DISTRIBUTION: ordinal; categorical  
COMPLEXITY: not stated  
DATA_AVAILABILITY: public-benchmark-used  
CODE_AVAILABILITY: public-repository  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
