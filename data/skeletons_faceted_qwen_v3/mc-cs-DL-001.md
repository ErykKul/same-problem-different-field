MECHANISM: The paper computes a conversational recommendation system that processes multi-turn natural language queries to recommend datasets. It first extracts structured elements (data, topic, constraints, evaluation metrics) from unstructured text using a perceptor module. Then, it compresses historical dialogue context into a structured memory to mitigate forgetting in large language models. A two-stage retrieval mechanism is applied: first, filtering candidate datasets using metadata and dense embeddings, then reranking with a ColBert model for fine-grained semantic matching. Each recommended dataset is linked to a CSTR identifier for traceability. The system balances retrieval efficiency and effectiveness through staged filtering and reranking, while structured memory ensures context consistency across turns. The algorithm operates on sequences of user queries and metadata-rich dataset descriptions, using deterministic processing for intent extraction and retrieval, with no explicit probabilistic modeling. The output is a ranked list of datasets aligned with the user's scientific intent, with trustworthiness ensured via CSTR citations. The system is evaluated using offline metrics (recall, NDCG, MRR) and online click-through rates.  
DOMAIN: scientific dataset recommendation  
STRUCTURE: other: agentic framework with memory and retrieval  
DATA_OBJECT: set or table  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: recommendation  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
