MECHANISM: Estimate a reweighting function that transforms source population data to match target population's covariate distribution. Use entropy balancing or model-based reweighting with calibration constraints to solve for weights that either align specific moments or satisfy estimated equations for density ratio modeling. Calculate weights from source-population individual data and target-population aggregate statistics (moments). Apply weights to source observations and compute target parameter estimates; propagate uncertainty from aggregate statistics through variance estimators derived from weighted combinations of source data.
DOMAIN: Causal inference and transportability across populations
STRUCTURE: optimization
DATA_OBJECT: table
INFERENCE: frequentist point estimate
PROBLEM_FORM: estimation
DISTRIBUTION: continuous; continuous
COMPLEXITY: polynomial iterative
