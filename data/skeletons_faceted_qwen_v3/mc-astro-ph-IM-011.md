MECHANISM: The paper computes a real-time detection and multi-mode frequency estimation system using a convolutional neural network (CNN) framework. The method processes time-series strain data through a pipeline involving robust power spectral density (PSD) estimation, frequency-domain whitening, and bandpass filtering to isolate the 2–4 kHz post-merger signal band. The data is transformed into time-frequency representations via short-time Fourier transforms (STFTs) with overlapping Hann windows. A shared convolutional encoder extracts features, followed by task-specific output heads for detection and frequency prediction. The detection head uses a binary classification architecture with sigmoid activation, while five parallel frequency heads predict normalized frequencies and aleatoric uncertainty. Training employs focal loss for class imbalance and mean squared error for frequency regression, with aggressive data augmentation simulating challenging noise conditions. An ensemble of five networks aggregates predictions via arithmetic mean, with epistemic uncertainty estimated from ensemble variance. The framework is validated on synthetic O4-characteristic noise with authentic glitch morphologies, achieving sub-millisecond latency and high detection accuracy.  
DOMAIN: gravitational wave detection  
STRUCTURE: other: convolutional neural network  
DATA_OBJECT: sequence or time-series  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: detection or test; estimation  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: public-benchmark-used  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-private-data
