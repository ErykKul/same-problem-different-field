MECHANISM: Represent documents as feature-count vectors recording word/phrase occurrence frequencies. Train three classifiers: (1) Naive Bayes computing posterior class probability assuming conditional independence of features; (2) Maximum entropy finding exponential distribution maximizing entropy subject to empirical feature constraints; (3) Support vector machine finding maximum-margin linear separator in feature space. Apply to predict document class from feature vectors.
DOMAIN: Natural language sentiment classification and opinion detection
STRUCTURE: graphical models
DATA_OBJECT: set or table
INFERENCE: frequentist point estimate
PROBLEM_FORM: classification
DISTRIBUTION: binary; binary
COMPLEXITY: polynomial iterative
