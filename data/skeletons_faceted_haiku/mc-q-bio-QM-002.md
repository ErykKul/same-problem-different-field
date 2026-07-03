MECHANISM: Develop peak-nadir encoding for time-series glucose data: identify local maxima and minima in continuous glucose monitoring signals, store their values and timestamps with reduced precision, and reconstruct the original signal using piecewise cubic Hermite interpolation between peak and nadir points. Evaluate compression ratio, storage efficiency, and reconstruction fidelity using metrics such as mean absolute error, coefficient of variation, and clinically relevant glucose excursion measures.
DOMAIN: Time-series signal compression for medical monitoring
STRUCTURE: Other: signal encoding and reconstruction
DATA_OBJECT: Sequence or time-series
INFERENCE: Deterministic or closed-form
PROBLEM_FORM: Optimization
DISTRIBUTION: none
COMPLEXITY: not stated
