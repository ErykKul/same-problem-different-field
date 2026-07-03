MECHANISM: Successive changes of a scalar quantity are discretized into a small set of ordered categories, producing a categorical sequence stratified by side, time window, and group. A likelihood-ratio independence test on the consecutive-state contingency table first checks for short-range dependence, justifying a first-order memory assumption. Conditional on dependence, a row-stochastic transition matrix over the states is estimated by maximum likelihood (normalized transition counts) for each stratum. From each matrix several invariants are computed in closed form: the stationary left-eigenvector solving the balance equations, the spectral gap as one minus the second-largest eigenvalue magnitude (with relaxation and mixing-time reparameterizations), the per-transition entropy rate weighted by the stationary vector, and mean recurrence times as reciprocals of stationary probabilities. To compare whole matrices, each is flattened to a vector, projected to a few principal components, embedded into two dimensions by a neighbor-preserving map, and grouped by hierarchical and density-based clustering. Pairwise dissimilarity of stationary distributions across windows is quantified by a symmetric information divergence. Results are read off as systematic patterns across windows, groups, and sides.
DOMAIN: limit-order microstructure in finance
STRUCTURE: graphical models
DATA_OBJECT: sequence or time-series
INFERENCE: maximum likelihood
PROBLEM_FORM: estimation
DISTRIBUTION: ordinal; multinomial
COMPLEXITY: closed-form
