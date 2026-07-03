MECHANISM: The paper computes a statistical algorithm for estimating model states and parameters using ensemble-based data assimilation. The method operates on an ensemble of model realizations, where each realization represents a possible state of the system. During the forecast step, the model equations are applied to advance each ensemble member's state forward in time, producing a forecast ensemble. The ensemble mean is calculated as the average of all ensemble members, and the forecast error covariance matrix is estimated from deviations of each member from the mean. Observations are assimilated in the analysis step, where the Kalman gain matrix is computed to weight the influence of observations on the ensemble. The Kalman gain is derived from the forecast error covariance and the observation error covariance, which accounts for uncertainties in the observations. The analysis ensemble is updated by applying the Kalman gain to the difference between observed and forecasted values, adjusting each ensemble member's state toward the observations. A matrix-free formulation avoids explicit computation of the covariance matrix, reducing computational cost and enabling parallel execution. The algorithm supports both stochastic and deterministic variants, with the stochastic version introducing perturbations to observation vectors to maintain ensemble spread. The deterministic variants apply transformations to the ensemble without perturbing observations, reducing computational overhead. The method is designed to handle high-dimensional, nonlinear systems and includes adaptive mechanisms for localization and inflation to improve stability and accuracy. The algorithm is implemented in a modular framework that allows integration with diverse modeling environments and supports scalable parallelization for large-scale simulations.  
DOMAIN: ice sheet modeling  
STRUCTURE: other: ensemble-based data assimilation  
DATA_OBJECT: set or table  
INFERENCE: Bayesian posterior  
PROBLEM_FORM: estimation  
DISTRIBUTION: continuous; Gaussian  
COMPLEXITY: not stated  
DATA_AVAILABILITY: public-repository  
CODE_AVAILABILITY: public-repository  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
