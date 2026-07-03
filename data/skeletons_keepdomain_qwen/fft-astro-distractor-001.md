MECHANISM: The paper computes a Gaussian process (GP) regression model to characterize stellar variability in photometric light curves from exoplanet transit observations. The method combines multiple variability components—stellar oscillations, granulation, and rotational modulation—into a hierarchical GP framework. Each component is modeled as a separate GP kernel, with hyperparameters optimized via Bayesian inference to maximize the likelihood of the observed light curves. The authors compare single-component GP models (1GP) against multi-component models (4–5 components) using cross-validation and model selection criteria. They simulate transits of Earth-, Neptune-, and Jupiter-sized planets, inject them into light curves with modeled stellar variability, and evaluate how well each GP variant recovers the true transit parameters. The multi-component GP outperforms the 1GP model for Earth- and Neptune-sized planets, while the 1GP fails to recover Earth-sized transits due to insufficient modeling of stellar activity. The non-GP baseline model (e.g., polynomial detrending) produces biased results in all cases. The method explicitly accounts for correlated noise from stellar variability, which is critical for high-cadence, high-signal-to-noise data from missions like CHEOPS and PLATO. The computational pipeline includes kernel selection, hyperparameter optimization, and posterior sampling via Markov chain Monte Carlo (MCMC) to quantify uncertainty in the inferred variability components and transit parameters. The paper emphasizes that the GP approach provides a more accurate and flexible description of stellar variability than traditional single-component models, improving the precision of exoplanet radius and orbital period estimates.  
DOMAIN: astrophysics and exoplanet detection  
STRUCTURE: graphical models  
DATA_OBJECT: sequence or time-series  
INFERENCE: bayesian posterior  
PROBLEM_FORM: estimation  
DISTRIBUTION: continuous; gaussian  
COMPLEXITY: not stated  
DATA_AVAILABILITY: public-benchmark-used  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: simulation-study
