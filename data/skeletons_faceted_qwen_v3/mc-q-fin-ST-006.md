MECHANISM: The paper computes a regression model where an observed inflation variable $ y $ is predicted using a latent variable $ \tilde{x} $, which is approximated as a linear combination of observed explanatory variables $ X $. The latent variable $ \tilde{x} $ is assumed to lead $ y $ by up to $ F $ periods. The model is formulated as $ y_t = c + \sum_{\tau=1}^F \beta_\tau \tilde{x}_{t-\tau} + \epsilon_t $, with $ \tilde{x}_t = X_t \bm{\omega} + r_t $. Coefficients $ \bm{\omega} $ and $ \beta_\tau $ are estimated iteratively via ordinary least squares (OLS), solving $ \bm{\omega} $ and $ \beta $ in a fixed-point iteration. Out-of-sample predictions assume a first-order autocorrelation structure for $ \tilde{x} $, using $ \mathbb{E}[\tilde{x}_{t+f-\tau}] = \rho^{f-\tau} \tilde{x}_t + (1 - \rho^{f-\tau}) \mathbb{E}[\tilde{x}] $. The method reduces model complexity by enforcing a shared lag structure across all $ X $ variables, resulting in $ 1 + n + F $ coefficients instead of $ 1 + nF $.  
DOMAIN: economics - inflation forecasting  
STRUCTURE: other: regression-based model  
DATA_OBJECT: matrix or tensor  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: prediction or classification  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
