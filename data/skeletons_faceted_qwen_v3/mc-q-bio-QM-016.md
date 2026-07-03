MECHANISM: The paper computes a multimodal temporal embedding framework that integrates sequential and tabular data to identify latent metabolic phenotypes. First, continuous glucose monitoring (CGM) time-series and laboratory measurements are normalized and aligned temporally. These are then encoded as contextual tokens in a transformer architecture, which models long-range dependencies through self-attention mechanisms across modalities. The transformer encoder produces low-dimensional embeddings that capture both short- and long-term temporal dynamics. Next, Gaussian Mixture Modeling (GMM) is applied to the embeddings to cluster patients into latent phenotypes, with probabilistic assignments reflecting continuous transitions between states. For interpretability, attention weights from the transformer are visualized to highlight influential time segments, while SHAP-based feature attribution quantifies the contribution of each input variable to phenotype separation. The framework jointly optimizes reconstruction loss for temporal consistency and clustering loss for latent structure, without explicit supervision. Key outputs include cluster assignments, attention maps, and SHAP values that link biochemical variables to metabolic subgroups. The method does not assume a specific distribution for the input data but relies on probabilistic clustering and post-hoc explanation techniques to ensure clinical relevance.  
DOMAIN: biomedical data analysis with machine learning  
STRUCTURE: other: transformer-based model  
DATA_OBJECT: sequence or time-series; set or table  
INFERENCE: Bayesian posterior  
PROBLEM_FORM: search  
DISTRIBUTION: outcome's measured distribution: categorical; estimator assumes: continuous  
COMPLEXITY: not stated  
DATA_AVAILABILITY: dataset-with-DOI-or-handle  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
