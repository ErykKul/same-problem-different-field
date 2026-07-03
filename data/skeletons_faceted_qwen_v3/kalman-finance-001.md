MECHANISM: The paper computes an adaptive parameter estimation framework for a non-linear, discrete-time state-space model. It begins by defining a recursive relationship between latent states and observations, where each state transition and observation depends on a set of unknown parameters. A Bayesian filtering approach is used to estimate both the latent states and parameters, with the posterior distribution updated iteratively using observed data. The method integrates Normal Maximum Likelihood Estimation (NMLE) to compute initial parameter estimates, which are then refined through Bayesian filtering. A performance metric based on the Posterior Cramer-Rao Lower Bound (PCRLB) is computed using particle filter approximations, which involve sampling from the posterior distribution of states and parameters. The PCRLB provides a theoretical lower bound on the mean squared error (MSE) of any estimator, and the method compares the actual MSE of different Bayesian filters (EKF, UKF, PF) against this bound. A switching strategy selects the filter with the smallest deviation from the PCRLB at each time step, using a performance metric derived from the trace of the product of the PCRLB inverse and the actual MSE matrix. The algorithm maintains numerical stability by leveraging boundedness properties of the stochastic processes involved. The process is repeated iteratively over time, updating parameter estimates and filter selection dynamically based on incoming data. The final output is a sequence of parameter estimates and state trajectories that adapt to changes in the underlying system dynamics.  
DOMAIN: stochastic volatility and Bayesian filtering  
STRUCTURE: graphical models  
DATA_OBJECT: sequence or time-series  
INFERENCE: Bayesian posterior  
PROBLEM_FORM: estimation  
DISTRIBUTION: continuous; continuous  
COMPLEXITY: not stated  
DATA_AVAILABILITY: public-benchmark-used  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
