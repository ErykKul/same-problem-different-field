MECHANISM: The paper computes maximum a posteriori Bayesian estimation (MAP-BE) of parameters in a population pharmacokinetic (PK) model. The process begins by defining a statistical model that relates observed data to unobserved parameters, incorporating both inter-individual variability (IIV) and residual error. Predictions are generated using a differential equation solver based on the model's structural equations and input data. The objective function value (OFV) is calculated as a combination of the negative log-likelihood of the observed data and a penalty term derived from the IIV distribution. The OFV is minimized by optimizing the IIV parameters (ηi) using the limited-memory Broyden–Fletcher–Goldfarb–Shanno with box constraints (L-BFGS-B) algorithm. The optimization iteratively adjusts ηi to find the set of values that minimizes the OFV, which corresponds to the most probable parameter estimates under the Bayesian framework. The method assumes a log-normal distribution for IIV parameters and a multivariate normal distribution for residual errors. The computation involves evaluating the objective function, which depends on predicted values, observed data, and the covariance structures of IIV and residual errors. The algorithm is applied to both simulated and real-world datasets to validate the accuracy of parameter estimates. The process is repeated for each individual in the dataset, with results compared to those from a reference software (NONMEM) to assess concordance. The method is implemented in an R package (mapbayr) that integrates with tools for data formatting, reporting, and interactive web applications.  
DOMAIN: pharmacokinetics and Bayesian parameter estimation  
STRUCTURE: optimization-based  
DATA_OBJECT: set or table  
INFERENCE: Bayesian posterior  
PROBLEM_FORM: estimation  
DISTRIBUTION: continuous; log-normal  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: public-repository  
PREREGISTRATION: none  
EVIDENCE_BASIS: simulation-study
