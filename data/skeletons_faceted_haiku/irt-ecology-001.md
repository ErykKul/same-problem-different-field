MECHANISM: An occupancy model estimates true presence-absence of a species at spatial locations using imperfect detection data. The true occupancy state follows a Bernoulli distribution with probability modeled as a logistic function of covariates. Spatially-varying coefficients are introduced: each covariate effect becomes a spatial surface modeled via a Nearest Neighbor Gaussian Process (NNGP). A hierarchical Bayesian framework with Pólya-Gamma data augmentation yields efficient Gibbs sampling. For multiple species, factor models decompose species-specific spatial effects into low-rank latent factors plus species loadings, sharing spatial information across species.
DOMAIN: ecology; species distribution modeling; conservation
STRUCTURE: graphical models
DATA_OBJECT: set or table
INFERENCE: Bayesian posterior via MCMC with Pólya-Gamma data augmentation; Nearest Neighbor Gaussian Processes for spatial effects
PROBLEM_FORM: estimation; prediction
DISTRIBUTION: measured as binary occupancy (presence/absence); estimator assumes logistic (sigmoid) occupancy probability given covariates and latent spatial effects
COMPLEXITY: polynomial iterative
