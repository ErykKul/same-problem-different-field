MECHANISM: Learn spatiotemporal representations from EEG via self-supervised pretraining on two dual objectives: reconstruct masked signal patches using transformer encoding, and predict neurodynamical statistics (spectral power, phase-locking value, cross-frequency coupling, sample entropy) from incomplete observations; incorporate neurophysiologically grounded positional encodings capturing volume conduction via 3D electrode geometry and temporal dynamics via oscillatory and exponential decay bases; fine-tune or freeze backbone for downstream classification.
DOMAIN: Neuroscience; brain-computer interfaces; EEG signal processing
STRUCTURE: other: masked autoencoder with self-attention transformer
DATA_OBJECT: sequence or time-series
INFERENCE: deterministic or closed-form
PROBLEM_FORM: estimation; classification
DISTRIBUTION: none
COMPLEXITY: not stated
