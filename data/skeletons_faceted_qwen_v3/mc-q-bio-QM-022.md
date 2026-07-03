MECHANISM: The paper computes a discrete Bayesian generative process for sequence design. It defines a Bayesian distribution over logits of a categorical distribution for a sequence of length L, where L is determined by input structure. The model iteratively updates beliefs about the sequence distribution through a forward process that corrupts data into parameter space, followed by a receiver network that estimates the true distribution from noisy parameters and time. The receiver uses a geometric transformer with invariant point attention to condition updates on 3D coordinates of atoms. The training objective is a weighted reconstruction loss, minimized via cross-entropy. Inference performs Bayesian updates by adding evidence and uncertainty terms to prior beliefs, refining the sequence iteratively. The model integrates geometric gradients through attention mechanisms that consider both semantic features and Euclidean distances between residues. Gradient accumulation and mixed-precision training are used to optimize performance. The method prioritizes high-fidelity structural signals over large datasets, filtering for resolution and completeness.  
DOMAIN: antibody design  
STRUCTURE: other: Bayesian Flow Network  
DATA_OBJECT: dense matrix or tensor  
INFERENCE: Bayesian posterior  
PROBLEM_FORM: simulation or generation  
DISTRIBUTION: discrete; continuous  
COMPLEXITY: not stated  
DATA_AVAILABILITY: dataset-with-DOI-or-handle  
CODE_AVAILABILITY: public-repository  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
