MECHANISM: The paper computes a distributed negotiation system that operates on user devices, integrating secure multi-party computation, model distillation, and cryptographic audit trails. The system begins by defining negotiation objectives and validating them against policy constraints. It retrieves context from memory, decomposes goals into sub-goals, and formulates strategies using distilled models. Offers are generated with zero-knowledge proofs to ensure constraint satisfaction without exposing private data. Secure multi-party computation checks for feasible agreements, and a simulation-critic mechanism evaluates proposed actions for safety. The system compresses negotiation states for cross-device continuity, logs decisions with Merkle trees for auditability, and dynamically offloads tasks based on latency, energy, and privacy constraints. Zero-knowledge proofs are used to verify offers, and outcomes are evaluated for fairness and compliance. The distilled world model enables on-device reasoning about counterparty behavior, while the simulation-critic prevents harmful agreements by predicting negotiation outcomes. The system balances privacy, efficiency, and safety through selective state transfer, model-aware offloading, and cryptographic verification.  
DOMAIN: privacy-preserving autonomous negotiation systems  
STRUCTURE: other: secure multi-party computation and model distillation  
DATA_OBJECT: set or table  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: decision or test  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: public-benchmark-used  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
