MECHANISM: The paper computes a bi-level metamodel to estimate treatment effects across multiple intervention levels and geographic regions. The first level uses Gaussian process regression (GPR) to model spatial and contextual dependencies of response-function coefficients, which are defined as linear functions of intervention levels. Each coefficient is treated as a continuous function over a high-dimensional input space of spatial and socio-economic features. The second level maps these coefficients to outcome predictions via a parametric response function. The framework employs a two-stage sequential design: the first stage selects regions with highest posterior uncertainty in the GPR model, prioritized by signal-to-noise ratio; the second stage selects intervention conditions within chosen regions based on credible interval width. The GPR model incorporates heteroscedastic noise, with observation variance estimated from simulation replicates. Kernel functions combine radial basis components to capture smooth spatial variation. The response function coefficients are estimated as posterior means of GPRs evaluated at input features, enabling interpolation across untested intervention levels and regions. The method quantifies predictive uncertainty to guide adaptive sampling, reducing the number of required simulations by an order of magnitude compared to exhaustive evaluation.  
DOMAIN: public health intervention modeling  
STRUCTURE: graphical models  
DATA_OBJECT: continuous function or field  
INFERENCE: Bayesian posterior  
PROBLEM_FORM: estimation  
DISTRIBUTION: continuous; continuous  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: simulation-study
