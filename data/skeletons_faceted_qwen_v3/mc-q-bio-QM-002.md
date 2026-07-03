MECHANISM: The method identifies key landmarks in a time-series by detecting local maxima ("peaks") and minima ("nadirs") through thresholding on prominence, which quantifies the vertical distance between a peak and the lowest adjacent valley. Additional "support" points are selected iteratively using a greedy algorithm to minimize reconstruction error, measured as the L2-norm of the difference between the original and interpolated signal. The compressed representation consists of timestamps and values at these landmarks. Reconstruction is performed via piecewise cubic Hermite interpolating polynomial (PCHIP), which preserves the shape and smoothness of the original signal by fitting cubic polynomials between consecutive landmarks. The algorithm operates in two phases: first, selecting landmarks based on prominence thresholds and greedy support point selection; second, interpolating between them to regenerate the full time-series. The method is deterministic, with no probabilistic or Bayesian components, and focuses on minimizing reconstruction error while maintaining clinically relevant features. The prominence threshold and compression ratio are parameters that control the trade-off between fidelity and data reduction. The process is applied to any continuous, time-ordered sequence of numerical values, regardless of domain.  
DOMAIN: biomedical signal processing  
STRUCTURE: other: landmark-based compression  
DATA_OBJECT: sequence or time-series  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: simulation or generation  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: public-repository  
CODE_AVAILABILITY: public-repository  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
