MECHANISM: Estimate the parameters of a pairwise maximum-entropy graphical model over many categorical variables from aligned observations. Fit single-variable field parameters and pairwise coupling parameters by maximizing a sum of per-variable conditional likelihoods with a quadratic regularizer, an asymptotically consistent surrogate that avoids the intractable normalizing constant. Each conditional treats one variable as the response and the remaining variables as predictors, giving a tractable convex objective. The fitted pairwise couplings are reduced to a single interaction score per pair, corrected for background heterogeneity. Pairs are ranked by score to separate variables that interact directly from those correlated only through intermediaries.
DOMAIN: structural biology
STRUCTURE: graphical models
DATA_OBJECT: graph or network
INFERENCE: frequentist point estimate
PROBLEM_FORM: estimation
DISTRIBUTION: categorical; pairwise maximum-entropy
COMPLEXITY: polynomial iterative
DATA_AVAILABILITY: public-benchmark-used
CODE_AVAILABILITY: public-repository
PREREGISTRATION: none
EVIDENCE_BASIS: empirical-with-released-data
