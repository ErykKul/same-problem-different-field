MECHANISM: The paper computes a parameter-efficient fine-tuning method for large language models (LLMs) by adapting low-rank updates to align with curvature and Fisher information. It begins by representing model updates as a low-rank matrix decomposition ΔW = BA, where B and A are matrices of reduced rank r. Gradients are preconditioned using K-FAC (Kronecker-Factored Approximate Curvature) to approximate the inverse Fisher information matrix within the low-rank subspace, rescaling gradient directions to suppress steps along sharp loss curvature. Periodically, the low-rank basis is reprojected onto dominant eigendirections of the Fisher matrix, aligning the subspace with high-signal, low-interference directions. Effective rank is dynamically adjusted based on the spectrum of rank-space covariances, concentrating updates where energy is concentrated. The method balances task loss with curvature regularization and reprojection constraints, ensuring updates remain sparse and targeted while preserving model performance. The algorithm iteratively applies preconditioning, reprojection, and rank adaptation, maintaining a stable parameterization throughout training. The net effect is reduced parameter count and improved retention of pretraining knowledge compared to fixed low-rank methods like LoRA. The paper models forgetting as a power law in fine-tuning data volume and model size, introducing an effective capacity multiplier to quantify the impact of curvature-aware updates on drift.  
DOMAIN: machine learning, parameter-efficient fine-tuning  
STRUCTURE: spectral or transform  
DATA_OBJECT: sparse matrix  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: optimization  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: public-benchmark-used  
CODE_AVAILABILITY: public-repository  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
