MECHANISM: A multimodal framework (Wave2Word) that learns EEG representations for neurocritical care by jointly modeling raw signal data and structured clinical language. Raw EEG is converted into bipolar montage and time-frequency representations, processed by dual transformer encoders (temporal and frequency) fused via adaptive gating. EEG embeddings are aligned with expert consensus descriptions using contrastive learning, with an EEG-conditioned text reconstruction loss providing additional representation-level supervision alongside classification loss.
DOMAIN: Biomedical signal processing, medical informatics, deep learning
STRUCTURE: other: multimodal dual-encoder fusion with alignment
DATA_OBJECT: sequence or time-series
INFERENCE: deterministic or closed-form
PROBLEM_FORM: classification or prediction
DISTRIBUTION: none
COMPLEXITY: convergence rate
