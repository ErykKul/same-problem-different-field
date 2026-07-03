MECHANISM: The paper computes a spatially varying parameter estimation using an iterative optimization algorithm. It begins by partitioning a spatial domain into regions using a tessellation method, where each region corresponds to a subset of observations. For each region, it applies an iterative algorithm to estimate parameters by alternating between an expectation step, which computes the likelihood of observations given current parameter estimates, and a maximization step, which updates parameters to maximize the likelihood. The algorithm incorporates spatial information by weighting parameter estimates based on proximity to observations within each region. After estimating parameters for all regions, it uses a model selection criterion to evaluate trade-offs between model fit and complexity, selecting a subset of regions whose parameter estimates contribute most to the overall model. The selected parameter estimates are then combined into a continuous spatial field through interpolation or aggregation. The method is validated by applying it to synthetic data generated under known parameter conditions, comparing estimated values to true values. Finally, the method is applied to a real-world dataset of observations, producing spatial maps of parameter estimates that are analyzed for patterns of variation.  
DOMAIN: computational seismology  
STRUCTURE: other: iterative optimization  
DATA_OBJECT: point set  
INFERENCE: frequentist point estimate  
PROBLEM_FORM: estimation  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: public-benchmark-used  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
