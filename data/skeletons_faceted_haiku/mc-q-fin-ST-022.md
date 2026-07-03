MECHANISM: Trains a frozen backbone (TCN or Transformer) on historical data with supervised loss; at test time applies causality-preserving augmentations (amplitude scaling, jitter, masking) to recent unlabeled windows; updates only small parameter sets (normalization affine parameters or batch statistics) using unsupervised objectives: entropy minimization plus temporal consistency for classification, prediction variance minimization plus EMA-teacher distillation for regression; includes drift penalty to control inter-timestep parameter change; triggers uncertainty-based fallback to batch-normalization statistics refresh when entropy or variance exceeds threshold; evaluates via rolling metrics, Diebold-Mariano tests, and economic backtests.
DOMAIN: Test-time adaptation for non-stationary time series with distribution shift
STRUCTURE: other: test-time adaptation
DATA_OBJECT: sequence or time-series
INFERENCE: frequentist point estimate
PROBLEM_FORM: prediction or classification
DISTRIBUTION: continuous; continuous
COMPLEXITY: polynomial iterative
