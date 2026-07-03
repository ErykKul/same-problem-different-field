MECHANISM: The paper computes maximum a posteriori Bayesian estimation (MAP-BE) of pharmacokinetic (PK) parameters using the R package mapbayr. The method operates on population PK models coded in mrgsolve, which define drug absorption (first-order or zero-order), elimination (Michaelis–Menten), residual error structures (combined or exponential), and covariate relationships (time-varying or static). Simulated PK profiles (4000 per model) are generated using these models, incorporating single/multiple dosing and rich/sparse sampling scenarios. MAP-BE is performed by optimizing the posterior distribution of parameters, combining prior information with likelihoods derived from simulated or real data. The algorithm compares results between mapbayr and NONMEM, assessing concordance in parameter estimates and objective function values. Discrepancies arise in cases with large inter-individual variability or dose-related parameters. The package includes tools for data formatting, reporting, and generating Shiny web apps for MIPD. The computational pipeline involves numerical optimization, simulation, and statistical inference under Bayesian principles.  
DOMAIN: pharmacokinetic modeling and Bayesian statistics  
STRUCTURE: optimization only  
DATA_OBJECT: continuous function or field  
INFERENCE: Bayesian posterior  
PROBLEM_FORM: estimation  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: public-repository  
PREREGISTRATION: none  
EVIDENCE_BASIS: simulation-study
