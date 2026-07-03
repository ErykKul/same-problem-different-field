MECHANISM: ECG signals are preprocessed (bandpass filtering, R-peak detection) to extract Heart Rate Variability (HRV) metrics and Catch22 time-series descriptors from RR intervals. Parallel classification pipelines use classical ML (Random Forest, SVM, XGBoost) with hand-crafted features and deep learning (1D-CNN, BiLSTM, Transformer) on raw signals. For cross-modal fusion, Catch22 features extracted from ECG are used to train XGBoost classifiers to predict cognitive states; the learned model is applied to EEG-derived Catch22 features to achieve transfer learning across modalities. Evaluation uses standard metrics (accuracy, F1, ROC-AUC) on three classification tasks: memory load (5/9/13 digits), binary (baseline vs. memory), and four-class.
DOMAIN: Cognitive load assessment, physiological computing, heart-brain coupling
STRUCTURE: other: feature-based ML and deep learning on time series
DATA_OBJECT: sequence or time-series
INFERENCE: bootstrap or resampling
PROBLEM_FORM: prediction or classification
DISTRIBUTION: none
COMPLEXITY: not stated
