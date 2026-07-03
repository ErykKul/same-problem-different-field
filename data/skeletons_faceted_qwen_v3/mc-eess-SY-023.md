MECHANISM: The paper computes long-term forecasts of a quantity using historical time-series data and energy-mix characteristics. It first preprocesses the data by interpolating missing values and removing outliers. Then, it fits multiple time-series models to the data, including autoregressive integrated moving average (ARIMA), seasonal ARIMA (SARIMA), and exponential smoothing (Holt-Winters). Each model is evaluated using metrics like mean absolute error (MAE), root mean squared error (RMSE), and R-squared. The best-performing model for each region is selected based on accuracy, residual behavior, and long-term stability. Forecasts are generated from 2024 to 2060 using the selected model, with uncertainty quantified through prediction intervals and bootstrapped ensembles. The forecasts are used to analyze how energy-mix composition influences future emission trajectories and alignment with net-zero goals.  
DOMAIN: environmental time-series analysis  
STRUCTURE: spectral or transform  
DATA_OBJECT: sequence or time-series  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: prediction or classification  
DISTRIBUTION: continuous; continuous  
COMPLEXITY: not stated  
DATA_AVAILABILITY: public-benchmark-used  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
