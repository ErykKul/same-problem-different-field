MECHANISM: The paper computes a self-exciting point process model to capture space-time clustering in crime events. The conditional intensity function is decomposed into a stationary background rate and a sum of triggering contributions from prior events. The background rate represents the baseline risk of events independent of previous occurrences, while the triggering kernel quantifies how past events increase the likelihood of future events in space and time. Estimation is performed nonparametrically using a stochastic declustering procedure, which separates the background and triggered components by iteratively removing the influence of recent events. The model parameters are inferred by maximizing the likelihood of the observed event times, with the triggering kernel estimated as a function of spatial and temporal distance from prior events. The method is applied to residential burglary data, where the spatial and temporal coordinates of each event are used to fit the model. The decomposition allows for prediction of future crime rates by combining the stationary background with the dynamic influence of past events. The nonparametric estimation avoids assuming a specific functional form for the triggering kernel, instead relying on data-driven smoothing techniques. The model's performance is validated by comparing predicted event rates to observed data, ensuring that the estimated parameters accurately reflect the underlying crime dynamics. The approach is analogous to seismic models used in seismology, where aftershocks are similarly modeled as triggered events following a main shock. The method provides a framework for understanding how crime spreads spatially and temporally, enabling targeted interventions based on predicted hotspots.  
DOMAIN: criminology and spatial statistics  
STRUCTURE: other: nonparametric estimation  
DATA_OBJECT: point set  
INFERENCE: optimization only  
PROBLEM_FORM: estimation  
DISTRIBUTION: binary; continuous  
COMPLEXITY: not stated  
DATA_AVAILABILITY: dataset-in-repository  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-private-data
