MECHANISM: The paper computes a dynamic first-order linear parameter-varying (LPV) model to capture the mean arterial blood pressure (MAP) response dynamics under vasoactive drug infusion. The model incorporates time-varying parameters and input delay, which are discretized and augmented into the state vector as unknown states. A Bayesian-based multiple-model square root cubature Kalman filtering (MMSRCKF) approach is applied to estimate the time-varying parameters of the system. The input delay is treated separately, as it cannot be modeled by a random-walk process, and a multiple-model module with posterior probability estimation is implemented to identify the delay. The algorithm iteratively updates the state vector using Bayesian inference, incorporating measurements of MAP and drug infusion rates. The MMSRCKF combines the predictions from multiple models, weighted by their posterior probabilities, to refine parameter estimates. The method is validated through simulation scenarios and animal experiment data, demonstrating its ability to track parameter changes and delay shifts in real-time. The computational steps involve discretization of the LPV model, state augmentation, Bayesian filtering with multiple models, and posterior probability estimation for delay identification. The algorithm operates in a recursive manner, updating estimates at each time step based on new measurements and prior model predictions. The use of square root cubature Kalman filtering ensures numerical stability and accuracy in parameter estimation. The method is designed for real-time application, making it suitable for automated drug administration in clinical settings.  
DOMAIN: physiological response modeling under drug administration  
STRUCTURE: dynamic programming  
DATA_OBJECT: sequence or time-series  
INFERENCE: Bayesian posterior  
PROBLEM_FORM: estimation  
DISTRIBUTION: continuous; Gaussian  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-private-data
