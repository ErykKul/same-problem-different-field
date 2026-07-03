MECHANISM: The paper computes a supervised classification model to predict the directional movement of an entity's index on the subsequent trading day. The process begins by collecting a sequence of time-series observations, each representing a day's open, high, low, and close values. A rolling window approach is used to construct a feature set, which includes raw price values, volatility-based indicators derived from historical data (e.g., Bollinger Bands, Keltner Channels), and a novel class of features based on mutual ratios of current-day values. These features are engineered to capture both long-term trends and short-term fluctuations. The target class is determined by comparing the open value of the next day to the current day's open, high, low, or close values, resulting in four distinct binary classification tasks. A supervised learning algorithm is trained on this labeled dataset, with performance evaluated using accuracy and Matthews Correlation Coefficient (MCC). The model's predictions are interpreted using Shapley values to quantify the contribution of each feature to the classification outcome. The method relies on deterministic computation, as the model does not explicitly model uncertainty or probabilistic outcomes. The framework is applied to time-series data from two distinct markets, demonstrating robust predictive performance across diverse economic conditions.  
DOMAIN: financial time series analysis and machine learning  
STRUCTURE: other: supervised classification  
DATA_OBJECT: sequence or time-series  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: prediction or classification  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: public-benchmark-used  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
