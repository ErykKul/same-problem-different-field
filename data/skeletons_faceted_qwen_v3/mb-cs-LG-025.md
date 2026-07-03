MECHANISM: The paper computes a token-level correctness estimation for reasoning traces in large language models (LLMs) using a verification token and low-rank adaptation (LoRA). During inference, a special token ([ToT]) is inserted to activate a LoRA module that accesses the model's key-value (KV) cache, which stores intermediate states from prior computation steps. The LoRA module applies cross-attention to the cached KV states, generating attention outputs that are aggregated into a hidden state. A regression head maps this hidden state to a scalar confidence score (0–1) for the partial reasoning trace up to the token position. Training uses pseudo-confidence labels derived from the final correctness of the full trace, with a linear ramp that interpolates uncertainty (0.5) toward the final outcome (0 or 1) as tokens accumulate. Verification is parallelized by inserting [ToT] at all positions simultaneously, reusing the cached prefix and applying a triangular mask to ensure each probe token only attends to its prefix. The method avoids recomputing the prefix, relying instead on the KV cache for efficient, single-forward-pass verification. Early termination is enabled by thresholding confidence scores to discard low-likelihood traces, reducing token usage without requiring auxiliary models or external feedback. The LoRA updates are gated to preserve the base model's reasoning behavior in default mode, ensuring minimal interference with primary tasks.  
DOMAIN: large language model reasoning verification  
STRUCTURE: transformer-based with parallel verification  
DATA_OBJECT: key-value cache tensor  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: estimation  
DISTRIBUTION: none  
COMPLEXITY: polynomial iterative  
DATA_AVAILABILITY: public-benchmark-used  
CODE_AVAILABILITY: public-repository  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-public-data
