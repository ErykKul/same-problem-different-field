MECHANISM: Construct supervised learning sequences by applying a sliding window of fixed length over a time-series of scalar observations, pairing past history with future targets. Normalize sequences using statistics computed from the training set. Train multiple sequence-to-scalar (or sequence-to-vector) neural network architectures: recurrent networks with gated units, convolutional networks with dilated causal convolutions, and transformer variants with multi-head self-attention over past timesteps. Generate predictions autoregressively by feeding model outputs back as inputs, or in teacher-forcing mode using ground-truth values. Evaluate error metrics and the trajectories of trading decisions derived from predicted directional movements.
DOMAIN: Stock price forecasting with neural sequence models
STRUCTURE: dynamic programming
DATA_OBJECT: sequence or time-series
INFERENCE: optimization only
PROBLEM_FORM: prediction or classification
DISTRIBUTION: continuous; continuous
COMPLEXITY: polynomial iterative
