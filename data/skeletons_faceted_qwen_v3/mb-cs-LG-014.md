MECHANISM: The paper computes the effect of two margin application strategies (saturating similarity clamping and post-log-probability subtraction) on training variance in a supervised contrastive loss framework. It defines a closed-form supervised contrastive loss with explicit margin variants, computes gradient contributions through forward and backward passes, and analyzes variance using sample variance calculations and F-tests. The method involves modifying similarities with a margin, applying temperature scaling, shifting logits for numerical stability, computing per-anchor log-probabilities via softmax, and aggregating losses using mean-over-positives reduction. Gradient truncation effects are evaluated through clamp activation rates and layerwise gradient norms. The analysis compares variance between margin types across multiple datasets, identifies dataset-dependent factors (positive-pair density and task difficulty), and validates gradient-neutrality of the subtraction baseline via mathematical proof. Diagnostic metrics include variance ratios, clamp activation rates, and gradient norms to isolate saturation-driven variance inflation. The computational steps are applied layerwise in a Vision Transformer architecture with stop-gradient operations to enforce local updates.  
DOMAIN: machine learning, contrastive learning, training stability  
STRUCTURE: other: loss function analysis  
DATA_OBJECT: test accuracy  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: estimation  
DISTRIBUTION: continuous; normal  
COMPLEXITY: not stated  
DATA_AVAILABILITY: public-benchmark-used  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
