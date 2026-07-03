MECHANISM: The paper computes spatially varying parameters of the Epidemic Type Aftershock Sequence (ETAS) model using the Expectation-Maximization (EM) algorithm. The method begins by initializing parameters for the ETAS model, which describes earthquake triggering and spatial-temporal distributions. Spatial Voronoi tessellation ensembles are used to partition the study area into regions, each associated with a subset of earthquakes. For each region, the EM algorithm iterates between an E-step, where it computes the posterior probabilities of earthquakes belonging to different triggering mechanisms, and an M-step, where it updates parameters to maximize the likelihood of the observed data. The Bayesian Information Criterion (BIC) is applied to rank and select the best-fitting models from the ensemble, balancing likelihood and model complexity. The selected models are then combined to produce spatially resolved parameter estimates across the study area. The method is validated using a synthetic earthquake catalog with known parameters, ensuring correctness. The approach is applied to real-world data from the ANSS catalog within a California polygon (1981–2015), revealing spatial variations in parameters such as the efficiency of earthquakes to trigger future ones. The results show a positive correlation between triggering efficiency and surface heat flow, with small earthquakes dominating triggering processes. The computation involves iterative optimization over spatial partitions and statistical model selection.  
DOMAIN: seismology and spatial statistics  
STRUCTURE: optimization only  
DATA_OBJECT: point set  
INFERENCE: frequentist point estimate  
PROBLEM_FORM: estimation  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: public-benchmark-used  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
