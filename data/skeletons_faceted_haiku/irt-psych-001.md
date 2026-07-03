MECHANISM: The Rasch model estimates item parameters from binary user-item response data by modeling response probability as a logistic function of the difference between item difficulty and user ability. Random pairing MLE (RP-MLE) converts user-item comparisons into item-item comparisons by randomly pairing a user's responses to different items, forming independent item-pair comparisons. The item parameters are then estimated via maximum likelihood on these constructed pairs. A bootstrapped variant (MRP-MLE) aggregates results across multiple random pairings.
DOMAIN: psychometrics; item response theory
STRUCTURE: graphical models
DATA_OBJECT: set or table
INFERENCE: maximum likelihood estimation on constructed item-pair comparisons
PROBLEM_FORM: estimation
DISTRIBUTION: measured as binary user-item responses; estimator assumes logistic (sigmoid) response probability
COMPLEXITY: polynomial iterative
