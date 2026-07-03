MECHANISM: Represent each sequence as a frequency vector counting overlapping k-length substrings. Fit multiple generative classifiers (multinomial Bayes, Markov chain) that model class-conditional probability distributions over these count vectors, using either maximum likelihood or Bayesian smoothing parameter estimation. Fit discriminative classifiers (logistic regression, linear support vector machine) that directly model posterior class probabilities or define discriminant functions. Systematically evaluate performance across variations in classifier type, parameter smoothing, regularization penalty, k-mer length, and sequence completeness.
DOMAIN: Viral genome classification and phylogenetic typing
STRUCTURE: dense linear algebra
DATA_OBJECT: sparse matrix
INFERENCE: frequentist point estimate
PROBLEM_FORM: classification
DISTRIBUTION: count; multinomial
COMPLEXITY: polynomial iterative
