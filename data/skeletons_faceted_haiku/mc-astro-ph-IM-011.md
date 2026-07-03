MECHANISM: Trains five-member ensemble of convolutional neural networks for real-time post-merger gravitational wave detection and multi-mode frequency extraction. Shared encoder (6 convolutional blocks, progressive channel expansion, GroupNorm, MaxPooling, global adaptive average pooling) feeds detection head (binary presence/absence) and three frequency heads (normalized to 2–4 kHz, each predicting f_norm and aleatoric uncertainty). Training on 413,000 augmented post-merger waveforms (CoRe database) with synthetic O4 noise (non-stationary PSD, spectral lines, heavy-tailed statistics, authentic GravitySpy glitches). Focal Loss for detection, MSE for frequency; AdamW optimizer, early stopping. Ensemble aggregates via arithmetic mean; epistemic uncertainty from member variance.
DOMAIN: Gravitational wave astronomy, real-time signal processing
STRUCTURE: other: convolutional neural network with multi-head architecture
DATA_OBJECT: dense matrix or tensor (spectrograms)
INFERENCE: optimization only
PROBLEM_FORM: prediction or classification + estimation
DISTRIBUTION: none
COMPLEXITY: not stated
