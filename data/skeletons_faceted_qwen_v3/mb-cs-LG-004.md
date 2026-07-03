MECHANISM: The paper computes a thermodynamically-informed multimodal foundation model that fuses three structural modalities (sequence, graph, and spatial geometry) through bidirectional cross-modal attention and gated fusion. Each modality is encoded separately: a Transformer processes a sequence, a graph convolutional network processes a graph, and a SchNet processes spatial geometry. Auxiliary encoders process experimental conditions and molecular descriptors. The fused representation is refined through a stack of condition-aware modules that route per-property inputs to four candidate prediction heads (thermodynamic equation, group contribution, fragment count, and direct FFNN). Training enforces inter-property consistency via cross-property loss terms (e.g., flash-point–vapor-pressure coupling). A four-stage training strategy combines self-supervised pretraining on unlabeled data, joint multi-task training with condition-aware refinement, low-learning-rate fine-tuning, and applicability-domain filtering. The model outputs property estimates through a tournament selection of heads, with uncertainty-weighted multi-task loss balancing objectives. Thermodynamic constraints are embedded via domain-informed equation heads that replace standard output layers, ensuring physical consistency without explicit supervision of equation coefficients.  
DOMAIN: molecular property prediction  
STRUCTURE: other: multimodal fusion  
DATA_OBJECT: graph or network  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: prediction or classification  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: public-benchmark-used  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
