MECHANISM: The paper computes time-series forecasting using two distinct algorithms. The first is a linear Kalman filter, which recursively estimates the current state by balancing measurement uncertainty and prediction uncertainty. It assumes that short-term stock price movements follow a random walk, with the variance of the predicted state proportional to historical variance. The second method is a long short-term memory (LSTM) network, a type of recurrent neural network with memory cells and three gates (forget, input, output). The LSTM processes sequential data by updating memory states through element-wise multiplication and neural network layers, allowing it to capture long-term dependencies. Both models are trained on historical stock price sequences, which are normalized to a [0,1] range for the LSTM. After training, predictions are rescaled to match the original data range. Model performance is evaluated using root-mean-square error (RMSE), mean absolute error (MAE), and R2 values. The study compares single-layer, stacked, bidirectional, and CNN-enhanced LSTM variants, finding that complex architectures perform better on volatile stocks while simpler models suffice for low-volatility cases. The Kalman filter is applied without data scaling and is found to perform well on low-volatility stocks. The paper concludes that clustering stocks by volatility and training separate models for each class could automate portfolio generation.  
DOMAIN: financial forecasting  
STRUCTURE: other: recurrent neural network  
DATA_OBJECT: sequence or time-series  
INFERENCE: optimization only  
PROBLEM_FORM: prediction or classification  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-private-data
