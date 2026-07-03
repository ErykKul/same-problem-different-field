MECHANISM: Adapt a federated learning model to non-stationary data streams without ground-truth labels by estimating per-client, per-timestep adaptive learning rates based on distribution shifts. Estimate two types of distribution dynamics: (1) uncertainty dynamics using cosine distance between consecutive batch-level softmax prediction distributions; (2) representation dynamics using cosine distance between consecutive batch-level normalized feature means. Combine these signals into a unified shift metric, then scale the learning rate adaptively between fixed min/max bounds. Use Black-box Shift Estimation to infer label distributions from model predictions on unlabeled data.
DOMAIN: Federated learning, online adaptation, distribution shift, non-stationary learning
STRUCTURE: other: adaptive learning rate scheduling
DATA_OBJECT: sequence or time-series
INFERENCE: frequentist point estimate
PROBLEM_FORM: optimization
DISTRIBUTION: none
COMPLEXITY: convergence rate
