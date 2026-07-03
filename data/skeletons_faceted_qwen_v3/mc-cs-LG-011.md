MECHANISM: The paper computes a hybrid feature space by transforming raw time-series data through wavelet-based time-frequency decompositions, then encoding structural relationships via graph-theoretic metrics. First, the input is filtered using a bandpass Butterworth filter to isolate clinically relevant frequency components. Next, R-peak detection is performed using an ensemble of differentiation, wavelet energy maximization, and adaptive thresholding, with peaks merged within a physiological refractory period. Segmentation is optimized via an adaptive windowing technique minimizing a composite loss function involving entropy, signal-to-noise ratio, and energy ratios. Feature extraction generates a multidimensional vector combining time-domain statistics, frequency-domain band powers, and morphological attributes derived from continuous wavelet transforms. Temporal dynamics are modeled through heart rate variability metrics in both time and frequency domains, while graph augmentation constructs a directed graph with edges weighted by cosine similarity of feature vectors and exponential decay in temporal proximity. Graph-theoretic features like PageRank centrality and clustering coefficients are extracted to quantify structural topology. Feature redundancy is reduced using mutual information thresholding and recursive elimination, followed by principal component analysis to enhance global variance. Class imbalance is addressed via SMOTE-ENN synthesis, and final classification is performed using linear models trained via regularized empirical risk minimization with class-weighted loss functions.  
DOMAIN: biomedical signal processing  
STRUCTURE: other: hybrid feature engineering  
DATA_OBJECT: sequence or time-series  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: classification  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: public-benchmark-used  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
