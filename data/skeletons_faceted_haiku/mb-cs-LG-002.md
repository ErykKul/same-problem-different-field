MECHANISM: Build a content-based recommendation system for multimodal items (images and text). Extract semantic representations via three complementary encoders: (1) large language model rewriting text to canonical form; (2) contrastive vision-language model (CLIP variant) embedding image-text pairs into a shared space via symmetric cross-modal matching loss; (3) variational autoencoder fusing visual and linguistic information probabilistically. Combine representations through graph neural networks with learned edge weights to propagate higher-order information. Predict user preferences by scoring item embeddings against user profiles, ranking by similarity. Handle multimodal missing data via uncertainty quantification in latent space.
DOMAIN: Recommendation systems and machine learning for cultural heritage.
STRUCTURE: graph traversal
DATA_OBJECT: graph or network
INFERENCE: Bayesian posterior
PROBLEM_FORM: ranking or retrieval
DISTRIBUTION: none
COMPLEXITY: not stated
