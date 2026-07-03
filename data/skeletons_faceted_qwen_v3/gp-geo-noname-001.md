MECHANISM: The paper computes spatial prediction of quantities using geostatistical interpolation and artificial neural networks. First, it calculates semivariograms to model spatial dependencies between sampled points, fitting theoretical models to empirical data. Then, it applies ordinary kriging and ordinary cokriging to estimate values at unsampled locations by weighting nearby measurements based on their spatial correlation. For the neural network approach, it trains a multilayer perceptron by iteratively adjusting connection weights between input, hidden, and output layers using error backpropagation. The input layer receives normalized measurements of multiple quantities, while the output layer predicts target quantities. Training involves minimizing prediction error through gradient descent, with weights updated until convergence. The model evaluates performance using root mean square error, coefficient of determination, and bias metrics. It compares results across methods to select the best predictor for spatial patterns. No explicit probabilistic modeling is performed; all estimates are deterministic. The process does not involve optimization beyond parameter tuning for model fitting.  
DOMAIN: environmental geostatistics and machine learning  
STRUCTURE: other: geostatistical interpolation and neural networks  
DATA_OBJECT: point set  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: prediction or classification  
DISTRIBUTION: continuous; continuous  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-private-data
