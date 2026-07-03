MECHANISM: Route queries in a retrieval-augmented generation system via a trained decision function. Apply Low-Rank Adaptation to a pre-trained language model to learn binary classification (retrieve or fallback) over query-evidence pairs. During inference, suppress autoregressive decoding via constrained vocabulary masking, forcing output to a single token from a binary set. Use the token's logit as a routing decision, passing evidence to downstream generation if high relevance is detected, or triggering fallback tool-use (external search) if contradictions are found. This is parameter-efficient fine-tuning with hardware-aware inference optimization.
DOMAIN: Machine learning and retrieval-augmented generation systems.
STRUCTURE: none
DATA_OBJECT: none
INFERENCE: none
PROBLEM_FORM: decision or test
DISTRIBUTION: none
COMPLEXITY: not stated
