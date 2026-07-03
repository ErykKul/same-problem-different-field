MECHANISM: Binary outcomes on pairs drawn from two disjoint node types form a bipartite incidence matrix. Each node of both types is assigned a latent position in a shared low-dimensional continuous space, and the probability of a positive outcome for a pair is a monotone link applied to two additive baseline terms (one per node type) minus a scaled straight-line distance between the two positions. The key modeling choice is that the unsquared metric distance, rather than a squared dissimilarity, enters the link, which restores the triangle inequality and makes the embedding a proper metric space; the paper proves the squared and exponential alternatives violate it. Independent priors are placed on the baselines, the distance scale, and the latent positions, and the joint posterior factorizes as the product-Bernoulli likelihood times the priors. Because the conditionals are non-standard, parameters are drawn by a within-Gibbs Metropolis-Hastings sampler that updates each block sequentially, imputing missing pair outcomes from the current link each sweep. Rotational, reflective, and translational non-identifiability is removed by post-hoc alignment to principal axes. Recovered positions are used for distance-based clustering and separation scoring, predictive accuracy, and interpretation of one node type as anchors for the latent axes.
DOMAIN: legislative roll-call ideal-point estimation
STRUCTURE: graphical models
DATA_OBJECT: graph or network
INFERENCE: bayesian posterior
PROBLEM_FORM: estimation
DISTRIBUTION: binary; logistic
COMPLEXITY: polynomial iterative
