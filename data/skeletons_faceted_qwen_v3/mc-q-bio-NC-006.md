MECHANISM: The paper computes a self-supervised learning framework for universal representation learning from unlabeled spatiotemporal data. The process begins by partitioning the input into non-overlapping spatiotemporal patches, with a random subset masked. Visible patches are projected into dense tokens via a temporal convolutional backbone. Two domain-specific positional encodings are applied: one modeling spatial mixing via 3D geometry and exponential decay, and another capturing slow oscillatory and exponential decay dynamics. Tokens are processed by a Transformer encoder to model global dependencies. The model is optimized using two objectives: Masked EEG Reconstruction (MER) to preserve local signal fidelity by reconstructing masked patches, and Neurodynamics Statistics Prediction (NSP) to enforce alignment with macroscopic brain state statistics. The spatial encoding uses pairwise Euclidean distances between electrode positions to compute a learnable spatial kernel, normalizing rows to form a convex combination. The temporal encoding combines fixed sinusoidal bases for slow oscillations and exponential decay functions for adaptation. The final embeddings are obtained by flattening the feature tensor and adding positional encodings. The dual-objective training ensures representations capture both fine-grained waveform details and high-level dynamical order parameters essential for defining brain states.
DOMAIN: neurophysiological signal processing
STRUCTURE: transformer-based model
DATA_OBJECT: spatiotemporal time-series
INFERENCE: deterministic or closed-form
PROBLEM_FORM: estimation
DISTRIBUTION: none
COMPLEXITY: not stated
DATA_AVAILABILITY: none
CODE_AVAILABILITY: public-repository
PREREGISTRATION: none
EVIDENCE_BASIS: empirical-with-private-data
