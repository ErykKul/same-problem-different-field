MECHANISM: Apply bandpass filtering to time-series signals to suppress noise while preserving morphological features. Detect landmarks in the signal using an ensemble of complementary detection methods, then segment into fixed-length windows. Extract a large set of features spanning time-domain statistics, frequency-domain band powers, and morphological attributes via wavelet decomposition. Augment features by computing scalar summaries of inter-sample relationships (HRV, graph-theoretic centrality). Select and refine features using mutual information and recursive elimination, then train a linear classifier on the augmented feature matrix via convex optimization.
DOMAIN: Arrhythmia detection in electrocardiogram signals
STRUCTURE: spectral or transform
DATA_OBJECT: dense matrix or tensor
INFERENCE: deterministic or closed-form
PROBLEM_FORM: prediction or classification
DISTRIBUTION: ordinal; ordinal
COMPLEXITY: polynomial iterative
