MECHANISM: Suppress generation of an undesired concept by minimizing mutual information between the concept label and generated images. Quantify mutual information using the pre-trained diffusion model's noise reconstruction error across diffusion timesteps. Optimize the unlearned model to make its conditional distribution given the concept match the pre-trained model's unconditional distribution, thereby eliminating concept-related semantics while preserving other generation quality.
DOMAIN: Machine unlearning, diffusion models, concept erasure, information theory
STRUCTURE: spectral or transform
DATA_OBJECT: dense matrix or tensor
INFERENCE: optimization only
PROBLEM_FORM: optimization
DISTRIBUTION: continuous; continuous
COMPLEXITY: convergence rate
