MECHANISM: Item Response Theory estimates latent ability parameters of examinees and item characteristic parameters (difficulty, discrimination, guessing) from binary response data. The 2PL and 3PL models compute response probability as a logistic (or guessing-adjusted logistic) function of the difference between ability and item difficulty scaled by discrimination. Parameters are estimated via alternating optimization: fix item parameters and optimize ability via logistic regression, then switch roles. Coresets (subsampled weighted subsets) approximate the full data to achieve scalability via importance sampling on leverage scores.
DOMAIN: educational assessment; item response theory; psychometrics
STRUCTURE: graphical models
DATA_OBJECT: set or table
INFERENCE: maximum likelihood estimation; alternating optimization with logistic regression subproblems
PROBLEM_FORM: estimation
DISTRIBUTION: measured as binary correct/incorrect responses; estimator assumes logistic (sigmoid) response probability
COMPLEXITY: polynomial iterative
