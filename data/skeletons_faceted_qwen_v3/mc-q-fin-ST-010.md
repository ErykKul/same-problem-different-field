MECHANISM: The paper computes a two-step risk assessment framework that integrates static and dynamic models through stacking. First, a static model estimates annual probabilities of default (PDs) using balance-sheet data anchored to fixed reference dates. This model combines standardized logit-transformed PDs from complementary sources with turnover class indicators via logistic regression. Second, a dynamic model captures monthly PD evolution by applying exponentially weighted moving averages (EWMA) to behavioral data, adjusting for temporal shifts. The dynamic model reuses the same logistic regression structure as the static model but incorporates time-weighted behavioral scores. A meta-learner then aggregates outputs from both models using logistic regression, treating their predictions as learned representations of distinct risk perspectives. This stacking approach allows integration of new features without retraining base models by encoding non-linear relationships in financial and behavioral indicators. Temporal consistency is enforced through exponential interpolation between anchor points, reflecting accelerating risk deterioration near distress. Size-specific delta shifts adjust PDs for calibration across company segments. The framework explicitly models the gap between data reference dates and evaluation dates, avoiding biases from stale or incomplete information. The final output is a unified predictive model that maintains interpretability through coefficient-based feature attribution and marginal effects analysis.  
DOMAIN: credit risk management  
STRUCTURE: other: stacking-based ensemble  
DATA_OBJECT: set or table  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: prediction or classification  
DISTRIBUTION: continuous; logistic  
COMPLEXITY: not stated  
DATA_AVAILABILITY: data-on-request  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-private-data
