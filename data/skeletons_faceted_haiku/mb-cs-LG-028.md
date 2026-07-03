MECHANISM: Mid-training bridges pre-trained language models to time series understanding through multimodal alignment. A synthetic time series corpus is generated using kernel methods to model diverse temporal patterns. Each time series is paired bidirectionally with natural language descriptions capturing temporal characteristics (trend, seasonality, peaks). A base language model is trained on this corpus alongside general-purpose data to maintain linguistic capabilities. The model learns to generate temporal descriptions from observations and vice versa, acquiring transferable temporal representations. Training incorporates mixed data including domain-specific time series knowledge texts and general text corpora via continued pre-training on a foundation architecture with grouped query attention. The learned model is evaluated on time series question-answering tasks requiring joint reasoning over temporal patterns and domain knowledge.
DOMAIN: Time series understanding for language models
STRUCTURE: other: multimodal pre-training with contrastive alignment
DATA_OBJECT: sequence or time-series
INFERENCE: none
PROBLEM_FORM: prediction or classification
DISTRIBUTION: none
COMPLEXITY: not stated
