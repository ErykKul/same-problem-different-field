MECHANISM: The paper computes a mid-training process that aligns temporal data with natural language through bidirectional generation tasks. It synthesizes time series data with rich temporal patterns using a Gaussian-process-based method, then generates natural language descriptions from multiple perspectives using a large language model. These descriptions are categorized as structured (detailed characterizations of properties like trend, seasonality) or unstructured (concise captions). The process reverses this by aligning textual descriptions with corresponding time series, creating paired data. A domain-agnostic synthetic generation ensures scalability, while open-source time series knowledge is incorporated for theoretical grounding. To prevent catastrophic forgetting, general-purpose pre-training data is mixed into the training corpus. The model is trained via full-parameter fine-tuning with AdamW optimization, using a cosine learning rate schedule, bfloat16 precision, and a global batch size of 32. The training includes two model variants (Qwen3-30B-A3B-Instruct and Qwen3-8B) with shared core design elements like Grouped Query Attention and Rotary Positional Embeddings. The final model is evaluated on benchmarks requiring joint reasoning over temporal patterns and domain knowledge, with tasks involving inference of temporal patterns informed by domain knowledge and decision-making based on time series data and general knowledge.  
DOMAIN: time series understanding and natural language processing  
STRUCTURE: other: mid-training  
DATA_OBJECT: time series and text pairs  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: prediction or classification  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: public-repository  
CODE_AVAILABILITY: public-repository  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
