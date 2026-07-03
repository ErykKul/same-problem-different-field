MECHANISM: The paper computes a two-step procedure to estimate volatility spillovers across multiple markets. First, it estimates own-volatility dynamics using ordinary least squares (OLS) to preserve high persistence in volatility, which is modeled as a weighted sum of daily, weekly, and monthly realized volatility components. Second, it applies ElasticNet regularization to cross-market spillover terms, shrinking most coefficients to zero while retaining economically meaningful connections. The algorithm first fits univariate HAR models for each market's own-volatility dynamics, then regresses residuals from these models on lagged volatility from other markets, using a combination of L1 and L2 penalties to enforce sparsity. The resulting sparse network identifies which markets transmit or receive volatility. Joint Impulse Response Functions (JIRFs) are computed by simulating shocks to subsets of markets and propagating these through the estimated model, using the covariance structure of residuals to determine shock correlations. The method separates persistence estimation from spillover identification, ensuring that impulse responses reflect both the slow decay of own-volatility and the sparse cross-market links. The ElasticNet optimization balances sparsity and grouping of coefficients, with parameters selected via time-series cross-validation. The final model combines the OLS-estimated own-dynamics with the ElasticNet-identified spillovers to produce forecasts and network structures.  
DOMAIN: financial econometrics  
STRUCTURE: sparse linear algebra  
DATA_OBJECT: sequence or time-series  
INFERENCE: optimization only  
PROBLEM_FORM: estimation  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: dataset-in-repository  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-private-data
