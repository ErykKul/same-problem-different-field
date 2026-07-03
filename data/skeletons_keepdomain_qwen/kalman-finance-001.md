MECHANISM: The paper computes an adaptive parameter estimation framework for the Heston model, a stochastic volatility model in finance, using Bayesian filtering theory and the Posterior Cramer-Rao Lower Bound (PCRLB). The method represents the Heston model in a non-linear, discrete-time state-space form, where latent states (volatility and parameters) are estimated using Bayesian filters, including the Extended Kalman Filter (EKF), Unscented Kalman Filter (UKF), and Particle Filter (PF). A switching strategy is implemented to adaptively select the optimal filter at each time step based on a PCRLB-based performance measure derived from a particle filter approximation. The PCRLB quantifies the theoretical lower bound on the mean squared error of any Bayesian estimator, allowing the framework to dynamically choose the filter with the lowest expected error. The method integrates Normal Maximum Likelihood Estimation (NMLE) to refine parameter estimates, combining it with Bayesian filtering for joint state and parameter estimation. The Heston model's parameters are estimated from observed index data (S&P 500 and NSE Index), with volatility and parameters inferred through the adaptive switching mechanism. The framework is evaluated by comparing its volatility estimates with the VIX measure and historical volatility for the same indexes. The computational steps involve: (1) modeling the Heston process as a state-space system; (2) applying Bayesian filters to estimate latent states and parameters; (3) computing the PCRLB for each filter's performance; (4) selecting the filter with the lowest PCRLB at each time step; (5) updating parameter estimates using NMLE; and (6) validating results against empirical benchmarks. The method emphasizes adaptability to changing market dynamics by continuously reassessing filter performance through the PCRLB metric.  
DOMAIN: stochastic volatility modeling in finance  
STRUCTURE: other: Bayesian filter switching  
DATA_OBJECT: non-linear discrete-time state-space model  
INFERENCE: Bayesian posterior  
PROBLEM_FORM: estimation  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: public-benchmark-used  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
