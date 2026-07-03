MECHANISM: A meta-learner (stacking ensemble) combines predictions from multiple base credit scoring models by treating their logit-transformed probability-of-default outputs as features. Base learners include behavioral scores and standardized credit risk data models. The meta-learner is trained via pointwise-consistent alignment of historical balance sheet dates with defaults occurring in the following year. Point-in-time consistency ensures that predictions at each decision point use data aligned with the reference period being modeled. The ensemble learns weights over the base predictions to produce calibrated probability-of-default estimates that improve prediction accuracy by leveraging multiple heterogeneous information sources.
DOMAIN: Credit risk and probability of default
STRUCTURE: other: stacking ensemble
DATA_OBJECT: set or table
INFERENCE: frequentist point estimate
PROBLEM_FORM: prediction or classification
DISTRIBUTION: binary
COMPLEXITY: polynomial iterative
