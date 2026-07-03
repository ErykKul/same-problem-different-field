MECHANISM: The paper computes a physics-consistent temperature forecasting framework by modifying classical decline curve equations to incorporate equilibrium-temperature terms derived from Newton-type cooling laws. This modification ensures finite late-time temperature limits while reducing to conventional Arps forms when the equilibrium term is zero. The extended decline curves are validated against temperature-time data and used to construct learning surrogates on a controlled dataset spanning fracture count, well spacing, fracture spacing, host-rock thermal conductivity, and circulation rate. An equation-informed neural network embeds the modified decline equations as differentiable internal layers, mapping design and operational inputs to full temperature trajectories while preserving interpretable decline structure. A probabilistic Gaussian Process Regression model is developed for multi-horizon forecasting with calibrated uncertainty, while a XGBoost regression serves as a data-driven baseline. The methods evaluate temperature trajectories across simulation datasets, comparing fidelity metrics like R², RMSE, and MAE. The framework unifies physics-based decline analysis with machine learning surrogates to reduce reliance on computationally intensive simulations. Key steps include equation embedding, probabilistic uncertainty quantification, and comparison of model performance across diverse geological and operational variables.  
DOMAIN: geothermal systems and machine learning  
STRUCTURE: dense linear algebra  
DATA_OBJECT: sequence or time-series  
INFERENCE: Bayesian posterior  
PROBLEM_FORM: prediction or classification  
DISTRIBUTION: continuous; continuous  
COMPLEXITY: not stated  
DATA_AVAILABILITY: dataset-with-DOI-or-handle  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
