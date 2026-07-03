MECHANISM: The paper computes a multimodal representation learning framework that aligns signal-domain data with structured language supervision. Raw input data is transformed into a longitudinal bipolar montage and time–frequency representations, capturing rhythmic and spectral features. Dual transformer-based encoders process complementary temporal and frequency-centric dependencies, with embeddings fused via an adaptive gating mechanism. EEG embeddings are aligned with structured descriptions using a symmetric contrastive objective, encouraging organization according to clinical semantics rather than label identity. An auxiliary text decoder reconstructs expert-style summaries, serving as a consistency constraint alongside standard classification loss. The method jointly optimizes classification, contrastive alignment, and reconstruction tasks, ensuring representations reflect both discriminative power and clinical coherence. Temporal and spectral features are modeled through fixed-window transformations, while stochastic augmentations in the spectrogram domain improve robustness. The framework emphasizes alignment with structured descriptions over discrete labels, using contrastive learning to enforce semantic organization. The final output combines classification accuracy with cross-modal retrieval metrics to evaluate representation quality beyond traditional benchmarks.  
DOMAIN: neurocritical care EEG analysis  
STRUCTURE: other: transformer-based architecture  
DATA_OBJECT: tensor; sequence  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: estimation  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-private-data
