MECHANISM: The paper computes a deep neural network model, specifically a long short-term memory (LSTM) recurrent architecture, to predict equity returns based on historical time-series data. The LSTM is trained using backpropagation through time to learn nonlinear dependencies in the data. Predicted returns are then used as inputs to an optimization algorithm that constructs optimal portfolios by maximizing expected returns while minimizing risk, subject to constraints on portfolio weights. The optimization problem is solved using quadratic programming techniques. The model's performance is evaluated by comparing portfolio returns against benchmarks and traditional linear regression models. The paper does not explicitly describe the mathematical form of the loss function or the specific constraints applied during optimization. The LSTM's hidden states are updated iteratively through the sequence of input data points, and the final output layer produces point estimates of future returns. These estimates are then used to compute portfolio weights via mean-variance optimization. The paper does not report the exact hyperparameters or regularization techniques applied during training.  
DOMAIN: finance and portfolio optimization  
STRUCTURE: other: deep learning  
DATA_OBJECT: sequence or time-series  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: optimization  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-private-data
