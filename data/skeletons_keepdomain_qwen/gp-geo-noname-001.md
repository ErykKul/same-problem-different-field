MECHANISM: The paper computes spatial prediction of trace metal concentrations and pollution indices in sediment samples using geostatistical and machine learning models. Sediment samples are collected and analyzed for total concentrations of As, Cr, Cu, Fe, Mn, Ni, Pb, Sn, and Zn. Pollution indices (SPI, NI, mCD, RI) are calculated from these concentrations. Ordinary Kriging (OK) and Ordinary Cokriging (OCK) are applied to model spatial variability, involving semivariogram modeling to quantify spatial dependency and interpolation to predict values at unsampled locations. Artificial Neural Networks (ANN) are trained on the same data, with layers of neurons and weights optimized via backpropagation to minimize prediction error. Model performance is evaluated using RMSE, R², scatter index (SI), and bias. Cross-validation selects the best-performing model, which is ANN for trace metal concentrations and pollution indices. The process involves data collection, feature computation, model training, validation, and selection based on statistical metrics. The paper does not describe uncertainty quantification or probabilistic inference.  
DOMAIN: environmental geostatistics and machine learning  
STRUCTURE: other: geostatistical and neural network  
DATA_OBJECT: point set  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: prediction or classification  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-private-data
