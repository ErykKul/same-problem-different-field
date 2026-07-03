MECHANISM: Item Response Theory (IRT) estimates learner ability from test scores. The Generalized Partial Credit Model (GPCM) computes the probability of observing a score as a logistic function of learner ability, item difficulty, discrimination, and step parameters. Missing scores are imputed using automated scoring models trained on subsets of manually scored responses or zero-shot LLM predictions. The complete dataset is then used to estimate ability by maximizing the IRT likelihood, with missing scores excluded during estimation.
DOMAIN: educational assessment; item response theory
STRUCTURE: graphical models
DATA_OBJECT: set or table
INFERENCE: maximum likelihood estimation; Bayesian posterior estimation
PROBLEM_FORM: estimation
DISTRIBUTION: measured as ordinal polytomous scores (multi-category); estimator assumes logistic (sigmoid-based) probability via GPCM
COMPLEXITY: polynomial iterative
