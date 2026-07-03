MECHANISM: The paper computes a Bayesian inference framework to estimate hyperparameters of quasi-periodic and quasi-periodic plus cosine Gaussian Process (GP) models. It begins by generating synthetic time-series data using a spot model, which simulates evolving active regions on a star. The synthetic data is then modeled using GP kernels, which combine periodic and decaying envelope terms. The GP hyperparameters (period, evolution timescale, harmonic complexity, and amplitude) are inferred via Markov Chain Monte Carlo (MCMC) sampling from the posterior distribution. The process involves fitting the GP to the synthetic data, comparing inferred hyperparameters to the input parameters of the spot model, and analyzing how well the GP recovers these parameters under varying conditions (e.g., noise, time-sampling). The study also evaluates the impact of data type (light curves vs. radial velocity curves) on hyperparameter recovery and investigates degeneracies in the GP model's parameter space. The analysis includes testing the robustness of the QP and QPC kernels, comparing their performance in recovering physical parameters, and assessing the influence of noise and sampling on the inferred hyperparameters. The results are validated through statistical tests (e.g., Kolmogorov-Smirnov) and visual comparisons of posterior distributions.  
DOMAIN: astronomy  
STRUCTURE: graphical models  
DATA_OBJECT: sequence or time-series  
INFERENCE: Bayesian posterior  
PROBLEM_FORM: estimation  
DISTRIBUTION: continuous; continuous  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: simulation-study
