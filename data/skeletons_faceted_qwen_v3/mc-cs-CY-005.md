MECHANISM: The paper computes a classification model to predict the likelihood of case resolution within six months using structured features derived from administrative case data. Features include static case attributes, dynamic event counts over time windows, temporal gaps, investigation milestones, lawyer activity metrics, unit-level performance indicators, and crime-type aggregates. The model is trained on historical data from 2014 to 2024, using a rolling temporal cross-validation strategy to avoid future data leakage. Predictions are evaluated using precision-focused metrics (Precision@300) aligned with institutional constraints. The system also applies legal rules to compute statutory prescription periods for cases, flagging those exceeding time thresholds based on crime category-specific penalties. The classifier generates weekly ranked lists of 300 cases for prioritization and 1000 cases for statutory oversight. The model uses an ensemble approach (Random Forests) combining multiple decision trees, with feature importance derived from historical patterns of case progression. The system emphasizes interpretability and operational feasibility, avoiding automation of decisions while supporting institutional workflows. Legal prescription thresholds are calculated using arithmetic means of statutory periods defined by the Código Penal para el Estado de Zacatecas. The methodology includes validation against random baselines and historical closure probabilities to assess model performance.  
DOMAIN: criminal justice and AI governance  
STRUCTURE: other: classification model  
DATA_OBJECT: set or table  
INFERENCE: frequentist point estimate  
PROBLEM_FORM: prediction or classification  
DISTRIBUTION: binary; binary  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-private-data
