MECHANISM: Train a gradient-boosted decision tree ensemble to predict an ordinal outcome (accident severity) from heterogeneous input features (environmental, temporal, spatial). Apply class weighting to address severe imbalance in outcome frequencies. Perform feature importance analysis to identify which input dimensions contribute most to predictions. Conduct cross-validation via random search over hyperparameters to optimize generalization.
DOMAIN: Traffic accident severity prediction using machine learning
STRUCTURE: map-reduce or embarrassingly-parallel
DATA_OBJECT: dense matrix or tensor
INFERENCE: frequentist point estimate
PROBLEM_FORM: prediction or classification
DISTRIBUTION: ordinal; ordinal
COMPLEXITY: polynomial iterative
