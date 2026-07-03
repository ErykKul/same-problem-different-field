MECHANISM: Replace gradient-based training with fixed random recurrent layers followed by a convex linear regression readout. Decompose a large recurrent memory module into a sequence of smaller interconnected fixed reservoirs. Feed the output of each reservoir as input to the next, capturing hierarchical temporal features. Train only the linear output layer via Tikhonov regularization to map concatenated reservoir states to target predictions. Compare computational cost and forecast accuracy against LSTM and standard RNN baselines on chaotic and spatiotemporal dynamics.
DOMAIN: Reservoir computing for spatiotemporal forecasting
STRUCTURE: spectral or transform
DATA_OBJECT: dense matrix or tensor
INFERENCE: deterministic or closed-form
PROBLEM_FORM: prediction or classification
DISTRIBUTION: continuous; continuous
COMPLEXITY: polynomial iterative
