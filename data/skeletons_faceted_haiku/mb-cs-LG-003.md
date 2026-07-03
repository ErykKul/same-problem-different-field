MECHANISM: Multiple quantile regressors are independently trained on historical time series data to estimate conditional quantiles of each variable, capturing distributional information. A genetic algorithm with three objectives iteratively evolves a population of candidate intervention policies represented as sequences of quantiles across time steps and variables. The algorithm minimizes distance between predicted outcomes and desired target values, maintains plausibility by limiting divergence from the original data distribution, and evaluates likelihood of the counterfactual scenario. Granger causality tests are applied to restrict the search space to causally-related variable pairs. Auto-regressive models generate future projections for each variable under the intervention policies.

DOMAIN: Time series forecasting and counterfactual explanation, causal inference

STRUCTURE: genetic algorithm

DATA_OBJECT: time-series

INFERENCE: optimization only

PROBLEM_FORM: optimization

DISTRIBUTION: continuous; continuous

COMPLEXITY: not stated
