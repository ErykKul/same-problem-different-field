MECHANISM: The paper computes a layer selection strategy for aligning hidden states in a flow model by quantifying each layer's contribution to the velocity field. It first computes a representation score for each layer using cosine similarity between layer outputs and frozen teacher encoders. Then, it computes a contribution score by ablating each layer's forward pass and measuring the induced change in the velocity field. These scores are used to select a sparse subset of layers with the highest contribution scores, which are then adaptively weighted for alignment. The alignment process involves projecting layer outputs into a shared embedding space and minimizing a loss function that aligns these projections with teacher features. The method iteratively updates layer contributions through residual transformations, where each layer's output is a function of its predecessor's state. The selection of layers is based on a top-K ranking of contribution scores, and the alignment weights are normalized by the sum of contribution scores across selected layers. The process is applied to both speech and general audio synthesis, with the velocity field defined as a time-dependent vector field parameterized by the model. The method ensures that alignment is applied only to layers that causally influence the velocity field, rather than those with high representation scores. The computation involves residual updates, Jacobian propagation analysis, and spatiotemporal alignment verification through heatmap visualization of layer scores across diffusion time steps. The final alignment loss is a weighted combination of representation and contribution-based objectives, optimized through gradient descent.  
DOMAIN: audio generation, flow matching, neural network interpretability  
STRUCTURE: dynamic programming  
DATA_OBJECT: sequence or time-series  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: optimization  
DISTRIBUTION: none  
COMPLEXITY: polynomial iterative  
DATA_AVAILABILITY: dataset-with-DOI-or-handle  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
