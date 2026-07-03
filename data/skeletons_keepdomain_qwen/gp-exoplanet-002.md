MECHANISM: The paper computes Bayesian inference on Gaussian Process (GP) models with quasi-periodic (QP) and quasi-periodic plus cosine (QPC) kernels to analyze stellar and exoplanet time-series data. It simulates light curves and radial velocity (RV) data using a spot model, then fits QP and QPC GPs to these data, comparing the posterior distributions of GP hyperparameters (period, length scale, noise parameters) to the input parameters of the spot model. The method involves Markov Chain Monte Carlo (MCMC) sampling or variational inference to estimate posterior distributions, evaluating how well the GP hyperparameters recover the physical parameters of the star and spots. The paper also compares hyperparameters derived from light curves and RV data for the same star, assessing agreement in period and evolution timescales. It investigates the impact of noise levels and time-sampling strategies on hyperparameter estimation in RV data, finding that coverage of rotation periods and spot evolution timescales is more critical than total data points. The harmonic complexity of the GP is analyzed as a function of data type (light curve vs. RV), with RV data showing systematically higher complexity. The QP kernel's hyperparameters are compared to the QPC kernel's, evaluating how additional terms affect parameter recovery. The method relies on probabilistic modeling of stellar activity patterns, with explicit comparison of simulated and inferred parameters to validate the QP/QPC kernel's physical interpretability.  
DOMAIN: stellar time-series analysis  
STRUCTURE: graphical models  
DATA_OBJECT: sequence or time-series  
INFERENCE: Bayesian posterior  
PROBLEM_FORM: estimation  
DISTRIBUTION: continuous; Gaussian  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: simulation-study
