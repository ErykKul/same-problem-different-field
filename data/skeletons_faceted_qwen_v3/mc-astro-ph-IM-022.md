MECHANISM: The paper computes a multi-dimensional linear regression to correct instrumental drifts in radial velocity measurements. The process begins by collecting a set of independent variables, including telemetry-based quantities (e.g., temperature sensor readings) and empirically derived parameters (e.g., line bisector spans and échellogram shifts). These variables are combined into a design matrix, where each row corresponds to an observation and each column to a tracer. The regression model estimates coefficients that minimize the residual variance between the observed radial velocities and the predicted values derived from the tracers. The corrected radial velocities are obtained by subtracting the predicted instrumental trends from the raw measurements. The method relies on temporal binning to isolate long-term systematics, using median filtering to smooth out short-term noise. The regression is applied to both stellar and solar data, with solar data used to difference out shared signals and isolate instrument-specific effects. The correction model is validated through injection-recovery simulations, which assess the improvement in sensitivity to low-amplitude planetary signals. The algorithm is deterministic, with no explicit handling of uncertainty or probabilistic modeling. The final output is a set of corrected radial velocities with reduced scatter, achieved by optimizing the binning window and selecting tracers that capture the dominant instrumental variations.  
DOMAIN: astronomical instrumentation  
STRUCTURE: other: multi-dimensional regression  
DATA_OBJECT: set or table  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: estimation  
DISTRIBUTION: none  
COMPLEXITY: closed-form  
DATA_AVAILABILITY: dataset-in-repository  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
