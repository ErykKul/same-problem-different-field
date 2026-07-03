MECHANISM: The paper computes a dual-module neural network framework to model concept formation and understanding. The first module, concept abstraction (CA), transforms high-dimensional input data into low-dimensional concept vectors through hierarchical gating mechanisms. These vectors dynamically modulate the second module, task-solving (TS), which performs classification tasks using a multi-layer perceptron (MLP) with a two-head classifier. Training proceeds in two phases: first, network parameters (CA and TS modules) are learned together; second, concept vectors are updated iteratively. A pretrained backbone extracts features, and the CA module generates control signals that reconfigure the TS module's activity. Concept vectors are updated via a round-robin process until accuracy plateaus. The framework supports cross-network knowledge transfer through a translation module that maps concept spaces between networks. Concept vectors are validated against human semantic models using representational similarity analysis (RSA), and their alignment with neurocognitive structures is tested via fMRI data comparisons. The model's performance is evaluated using accuracy metrics on visual classification tasks and semantic similarity measures.  
DOMAIN: neuroscience and artificial intelligence  
STRUCTURE: other: hierarchical neural network  
DATA_OBJECT: dense matrix or tensor  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: simulation or generation  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: public-benchmark-used  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
