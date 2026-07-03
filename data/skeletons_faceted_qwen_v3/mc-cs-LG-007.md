MECHANISM: The paper computes a sequential reservoir computing architecture for spatiotemporal forecasting. The method processes an input sequence through a series of interconnected reservoir layers, each maintaining a dynamic state that evolves based on the previous state and the current input. Each reservoir layer applies a non-linear transformation to its internal state, which is updated using a leaky integration mechanism. The outputs of all reservoir layers are concatenated into a composite state vector, which is then mapped to the output through a linear readout layer trained via ridge regression. The readout layer minimizes a cost function that balances prediction accuracy and model complexity using Tikhonov regularization. The architecture avoids backpropagation by fixing the reservoir weights and only training the readout layer. The sequential arrangement allows the model to capture multi-scale temporal dependencies while reducing memory and computational costs compared to monolithic reservoirs. The method is evaluated on both low- and high-dimensional spatiotemporal datasets, demonstrating improvements in forecast horizon and error metrics. The mathematical formulation includes explicit equations for state transitions, reservoir dynamics, and readout optimization, with parameters such as the leak rate and regularization coefficient controlling the model's behavior. The approach is designed to scale efficiently to high-dimensional inputs by decomposing the reservoir into smaller, modular components.  
DOMAIN: machine learning for spatiotemporal forecasting  
STRUCTURE: other: sequential reservoir layers  
DATA_OBJECT: sequence or time-series  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: prediction or classification  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: public-benchmark-used  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
