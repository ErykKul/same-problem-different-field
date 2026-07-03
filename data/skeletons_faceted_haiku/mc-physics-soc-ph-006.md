MECHANISM: The method combines physics-based decline curve analysis from well performance trends with machine learning regressors to forecast temperature evolution in geothermal reservoirs. Physics models encode domain knowledge via analytical equations governing transient behavior; ML models learn residual patterns from training data. The pipeline extracts temporal features, applies decline curve fitting, then trains ensemble or neural network regressors on observed-minus-predicted gaps to forecast future temperature at observation depths.
DOMAIN: Enhanced geothermal systems, temperature forecasting
STRUCTURE: Other: ensemble regression or neural network
DATA_OBJECT: Sequence or time-series
INFERENCE: Frequentist point estimate
PROBLEM_FORM: Prediction or classification
DISTRIBUTION: continuous; continuous
COMPLEXITY: not stated
