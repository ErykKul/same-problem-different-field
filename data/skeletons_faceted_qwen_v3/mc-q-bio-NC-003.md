MECHANISM: The paper computes a classification framework using time-series features extracted from ECG and EEG signals to infer cognitive load. It begins by preprocessing raw physiological signals through bandpass filtering and artifact correction to obtain clean time-series data. From these, it extracts two types of features: traditional HRV metrics (e.g., SDNN, RMSSD) and a standardized set of 22 non-linear time-series descriptors (Catch22). These features are then used to train machine learning models (XGBoost, SVM, Random Forest) and deep learning architectures (1D-CNN, BiLSTM, Transformer) for classification tasks. The framework includes cross-modal transfer learning, where features from one modality (ECG or EEG) are projected onto the feature space of the other modality to enable fusion. The models are evaluated on three classification tasks: distinguishing memory load levels (low, medium, high), binary classification (baseline vs. memory), and four-class classification (including baseline). The method relies on feature importance analysis and confusion matrices to assess model performance and interpretability. It does not involve probabilistic inference or optimization beyond model training. The core computation is feature extraction, model training, and cross-modal projection using deterministic algorithms.  
DOMAIN: cognitive neuroscience and physiological computing  
STRUCTURE: other: machine learning pipelines  
DATA_OBJECT: sequence or time-series; set or table  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: classification  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: dataset-with-DOI-or-handle  
CODE_AVAILABILITY: public-repository  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
