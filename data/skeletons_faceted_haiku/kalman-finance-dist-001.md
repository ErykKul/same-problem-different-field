MECHANISM: Evaluate multiple methods for one-step-ahead prediction of time series. Linear method: maintain a posterior distribution over current state using a linear state-transition model and noisy observations, combining prediction and measurement uncertainty. Nonlinear methods: train recurrent neural networks with gates controlling information flow and internal state, using backpropagation to learn weights from historical data. Compare methods on empirical error metrics (RMSE, MAE, R2) and classify time series by volatility to select the better algorithm per class.
DOMAIN: Stock price forecasting and time series prediction.
STRUCTURE: dynamic programming
DATA_OBJECT: sequence or time-series
INFERENCE: deterministic or closed-form
PROBLEM_FORM: prediction or classification
DISTRIBUTION: continuous; continuous
COMPLEXITY: polynomial iterative
