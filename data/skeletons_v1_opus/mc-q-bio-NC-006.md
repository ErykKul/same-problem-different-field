MECHANISM: A multichannel time-series observation is partitioned into a grid of non-overlapping space-by-time patches, a random fraction of which are masked. Visible patches are projected into dense vectors by a small stack of one-dimensional convolutions, then augmented with two structured positional codes: a spatial code that smooths each channel's coordinate by a learnable distance-decay kernel over inter-channel separations, and a temporal code built from fixed oscillatory and exponential-decay bases. The resulting token sequence is processed by a stack of self-attention layers so each token integrates information from all others. Two heads decode the contextual tokens: one linearly reconstructs the masked raw patches under a robustified regression loss, the other predicts a vector of summary descriptors computed from the full signal (band-integrated spectral fractions, pairwise phase-synchrony summaries, cross-band coupling, and a regularity index). Parameters are fit by stochastic gradient descent on the weighted sum of these two losses over a large unlabeled corpus. The learned encoder is then evaluated either by full fine-tuning or with frozen weights and a small task head, minimizing cross-entropy or squared error per task. Ablations remove each positional code and each pretraining objective.
DOMAIN: brain-signal decoding and neural interfaces
STRUCTURE: neural network
DATA_OBJECT: sequence or time-series
INFERENCE: deterministic optimization
PROBLEM_FORM: prediction or classification
DISTRIBUTION: continuous; none
COMPLEXITY: polynomial iterative
