MECHANISM: The paper computes an optimal inventory policy for a two-tier supply chain by transforming the problem into the z-transform domain. It models demand as an i.i.d. Gaussian sequence and represents the retailer's orders as a one-sided Gaussian MA(∞) process with coefficients encoding the inventory policy. The supplier's forecast accuracy is quantified via spectral density and mean squared forecast error (MSFE), while the retailer's inventory variance is derived from the energy of the transfer function. The optimization problem is reformulated using Hardy space methods, decomposing the transfer function into outer and inner factors. The inner factor, an all-pass filter, introduces unforecastable components, while the outer factor captures forecastable dynamics. The paper derives conditions under which optimal policies are MA(1) or require infinite-order ARMA approximations, showing that pure delay is suboptimal. It introduces group delay to quantify how demand information is temporally distributed across lags, reshaping autocorrelation for improved forecastability. The analysis extends to memory-constrained suppliers, balancing signal complexity against interpretability. Minimum-phase ARMA filters approximate theoretically optimal but non-invertible policies, enabling practical deployment. The solution minimizes a cost function combining inventory variance and supplier MSFE, leveraging spectral analysis and Hardy-Hilbert space properties.  
DOMAIN: supply chain management, inventory control  
STRUCTURE: spectral or transform  
DATA_OBJECT: sequence or time-series  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: optimization  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: mathematical-proof
