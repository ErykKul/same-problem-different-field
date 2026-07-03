MECHANISM: The paper computes a factor model with attention mechanisms for mixed-frequency data. It transforms input matrices (Y and X) into a unified embedding space using cross-sectional and temporal attention matrices. These matrices adaptively reweight observations based on similarity and relevance, replacing fixed linear combinations with data-dependent weights. For linear activation functions, the model establishes consistency and asymptotic normality of factor and loading estimators by extending classical PCA to incorporate attention matrices. Nonlinear signals are captured through stacked Transformer encoder layers with attention and feedforward networks. The framework aggregates information across frequencies without manual alignment or pre-specified weights, learning how to combine data from target and auxiliary panels. Attention mechanisms act as learned smoothing kernels, reweighing observations based on pairwise similarity. The model jointly estimates signals for target and auxiliary panels by solving an optimization problem that minimizes weighted errors from both datasets. Temporal encoding is used to capture sequential dependencies, and ablation studies assess the role of attention, nonlinearities, and high-frequency data in forecasting. The method generalizes Target PCA by allowing nonlinear signals and adaptive reweighting, while preserving theoretical properties for linear cases. Simulations and empirical applications demonstrate performance in nonlinear environments and macroeconomic forecasting.  
DOMAIN: econometrics and machine learning  
STRUCTURE: other: attention-based neural network  
DATA_OBJECT: dense matrix or tensor  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: estimation  
DISTRIBUTION: none  
COMPLEXITY: consistency  
DATA_AVAILABILITY: public-benchmark-used  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
