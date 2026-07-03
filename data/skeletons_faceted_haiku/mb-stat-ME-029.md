MECHANISM: Extract interpretable features from raw signals (e.g., ECG data) using a pre-trained foundation model. Feed foundation-model outputs into a generalized additive model (GAM) with smooth, entry-wise functions of each predictor. Fit the GAM via iterative backfitting or penalized likelihood to estimate marginal relationships. Generate predictions by composing smooth functions additively. Compute attributable risk contributions from each smooth component.
DOMAIN: Medical risk prediction and interpretable machine learning
STRUCTURE: other: additive model
DATA_OBJECT: sequence or time-series
INFERENCE: frequentist point estimate
PROBLEM_FORM: prediction or classification
DISTRIBUTION: binary; continuous
COMPLEXITY: polynomial iterative
