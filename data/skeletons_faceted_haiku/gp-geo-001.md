MECHANISM: Proposes transformed Gaussian Markov random fields (GMRFs) via probability integral transformation to create spatial random fields with non-Gaussian marginal distributions while preserving the underlying Markov dependency structure. Represents the spatial field as a graph where sparse precision matrix defines conditional independence. Applies inverse transform sampling to obtain fields with arbitrary margins (gamma, beta, etc.) given a Gaussian copula structure. Specifies spatial GLMMs using these fields as random effects and conducts Bayesian posterior inference.
DOMAIN: Geostatistics, spatial statistics, environmental modeling
STRUCTURE: graphical models
DATA_OBJECT: grid or lattice
INFERENCE: Bayesian posterior
PROBLEM_FORM: estimation
DISTRIBUTION: continuous; continuous
COMPLEXITY: polynomial iterative
