MECHANISM: The paper computes stock price predictions using a linear Kalman filter and long short-term memory (LSTM) networks. Historical stock price data is processed as time-series inputs, with the Kalman filter applied recursively to estimate the next-day value based on a linear state-space model. For LSTM models, the data is partitioned into sequences, and the network is trained to capture temporal dependencies through gated recurrent units. The models are evaluated by comparing predicted values to historical "true" values using error metrics such as mean squared error. The paper identifies clusters of stocks based on volatility (e.g., low-volatility stocks like Microsoft vs. high-volatility stocks like Tesla) and trains separate LSTM architectures for each cluster. The Kalman filter performs well on low-volatility stocks, while LSTMs outperform it on high-volatility stocks. The method involves no explicit probabilistic modeling of uncertainty, relying instead on deterministic error minimization. The computational pipeline includes data preprocessing, model training, and performance quantification across multiple stock types. The goal is to automate portfolio generation by selecting models based on target return rates.  
DOMAIN: financial time series prediction  
STRUCTURE: other: Kalman filter and recurrent neural networks  
DATA_OBJECT: sequence or time-series  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: prediction or classification  
DISTRIBUTION: continuous; continuous  
COMPLEXITY: not stated  
DATA_AVAILABILITY: public-benchmark-used  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
