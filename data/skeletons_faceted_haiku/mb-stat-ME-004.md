MECHANISM: A regression model is estimated by minimizing the Nash-Sutcliffe loss, a normalized metric that is the difference from one minus the Nash-Sutcliffe efficiency. The loss is strictly consistent for estimating a data-weighted component-wise mean functional. Linear regression is performed by minimizing the average Nash-Sutcliffe loss across multiple time series, which reduces to weighted least squares with data-dependent weights. The weighting scheme is derived from the normalizing constant in the NSE formula, placing larger weight on series with higher variability. The framework is extended from the classical formulation to handle stationary dependent time series by reorienting the sample loss function to reflect the underlying data-generating process.
DOMAIN: time series forecasting and loss functions
STRUCTURE: dense linear algebra
DATA_OBJECT: sequence or time-series
INFERENCE: frequentist point estimate
PROBLEM_FORM: prediction or classification
DISTRIBUTION: continuous
COMPLEXITY: closed-form
