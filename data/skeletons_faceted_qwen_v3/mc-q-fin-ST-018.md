MECHANISM: The paper computes a fusion of multiple model outputs to predict a quantity. It begins by generating score and rank functions from each model's predictions, where scores are normalized real numbers and ranks are derived from sorted scores. Cognitive diversity between models is quantified as the Euclidean distance between their rank-score characteristic functions. Models are then combined using three strategies: average combination (equal weighting), weighted combination by diversity strength (higher weight for models with greater diversity), and weighted combination by performance (higher weight for models with better individual metrics). For each combination, scores and ranks are aggregated using weighted averages, with weights determined by diversity or performance metrics. The final prediction is derived by selecting the value with the highest probability across all combinations, using normal distributions centered on model predictions with standard deviations from the test set. Truncation at two standard deviations ensures bounded ranges, and the final prediction is the value with the highest probability within the combined range.  
DOMAIN: financial forecasting  
STRUCTURE: map-reduce or embarrassingly-parallel  
DATA_OBJECT: set or table  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: prediction or classification  
DISTRIBUTION: continuous; normal  
COMPLEXITY: not stated  
DATA_AVAILABILITY: public-benchmark-used  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
