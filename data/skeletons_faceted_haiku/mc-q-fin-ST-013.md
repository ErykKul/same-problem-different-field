MECHANISM: Technical indicators (rolling volatility, RSI, rolling mean) are computed from daily log-returns via windowed calculations over 5-day, 10-day, 14-day, and 20-day periods. A neural network or tree-based predictor maps these technical features to discrete price direction predictions (up, down). The model is trained to forecast future returns from past technical indicator values. The methodology tests whether simple mechanical trading rules based on lagged technical indicators have predictive power for directional returns and whether their performance varies across assets or time periods. The approach compares in-sample fitting to out-of-sample generalization across multiple indicator parameterizations and learning algorithms.
DOMAIN: Technical analysis and price prediction
STRUCTURE: other: feature extraction
DATA_OBJECT: sequence or time-series
INFERENCE: optimization only
PROBLEM_FORM: prediction or classification
DISTRIBUTION: ordinal
COMPLEXITY: not stated
