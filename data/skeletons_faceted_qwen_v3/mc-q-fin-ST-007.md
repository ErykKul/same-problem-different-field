MECHANISM: The paper computes impulse response functions of investor flows using Tikhonov-regularized deconvolution and models self-exciting trading dynamics with Hawkes processes. The deconvolution problem involves solving a linear inverse problem where the observed return data is expressed as a convolution of order flow imbalance and an unknown impulse response kernel. Regularization is applied to stabilize the solution by balancing fidelity to the data against smoothness of the estimated kernel. The Hawkes process models the intensity of trading events as a self-exciting point process, with the intensity function defined as a baseline rate plus a sum of decaying contributions from previous events. Parameters of the Hawkes process are estimated via maximum likelihood, subject to a stability constraint ensuring stationarity. The analysis distinguishes between permanent and transient price impacts by examining the sign and persistence of the impulse response kernel. The method also employs entropy production rate to validate irreversibility in flow-return dynamics and quantifies clustering in trading surges using Hawkes memory analysis. The computational steps include constructing design matrices from lagged order flows, solving regularized linear systems, and estimating branching ratios and decay rates from event times. The results are validated through cross-verification with entropy measures and regime-dependent impulse response functions.  
DOMAIN: market microstructure and price discovery  
STRUCTURE: other: deconvolution and Hawkes process modeling  
DATA_OBJECT: sequence or time-series  
INFERENCE: optimization only  
PROBLEM_FORM: estimation  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-private-data
