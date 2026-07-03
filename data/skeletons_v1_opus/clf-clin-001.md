MECHANISM: Each entity is represented as a vector of nonnegative integer counts over a fixed vocabulary of discrete features. A generative probabilistic model assumes each of two classes generates feature counts according to a class-specific categorical distribution over the vocabulary, with features assumed conditionally independent given the class. For a given entity, the likelihood of its observed counts under a class is the product of per-feature probabilities raised to their observed counts, scaled by a multinomial coefficient. Model parameters are the per-class per-feature probabilities, estimated from labeled training data by relative frequency of each feature within each class. A prior probability is assigned to each class. Classification proceeds by computing, for each class, the log of the product of the prior and the class-conditional likelihood, and assigning the entity to the class with the larger posterior log-score; for two classes this reduces to a log-likelihood-ratio plus log-prior-ratio threshold rule. Performance is estimated by partitioning the labeled set into equal folds and averaging held-out scores across rotations. Two feature representations and their union are compared by precision, recall, and their harmonic mean.
DOMAIN: clinical text classification, biomedical informatics
STRUCTURE: graphical models
DATA_OBJECT: set or table
INFERENCE: maximum likelihood
PROBLEM_FORM: prediction or classification
DISTRIBUTION: count; multinomial
COMPLEXITY: closed-form
