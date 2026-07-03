MECHANISM: The paper computes a statistical emulator for an optimization problem under uncertainty. It begins by reducing the dimensionality of a high-dimensional random field using a spectral decomposition technique, projecting the field onto a set of orthonormal basis functions. This reduces the input space to a lower-dimensional latent variable representation. Next, a Gaussian process is constructed as a surrogate model, where the mean and covariance functions are defined using hyperparameters estimated via maximum likelihood. The process involves sampling input points using a stratified sampling strategy to ensure coverage of the input space. For each sampled input, the original optimization problem is solved to obtain corresponding outputs. These input-output pairs are used to train the Gaussian process emulator, which approximates the relationship between inputs and outputs. The emulator is then used to evaluate the optimization problem at new input points with negligible computational cost. The uncertainty in the output is quantified by the posterior predictive distribution of the Gaussian process, which provides mean and variance estimates. The method is applied to a stochastic optimization problem where the objective function depends on a random variable, and the goal is to estimate statistical moments of the solution. The approach replaces expensive Monte Carlo sampling with a reduced-order model that maintains accuracy while significantly reducing computational time.
DOMAIN: power systems and uncertainty quantification
STRUCTURE: graphical models
DATA_OBJECT: set or table
INFERENCE: Bayesian posterior
PROBLEM_FORM: estimation
DISTRIBUTION: continuous; Gaussian
COMPLEXITY: not stated
DATA_AVAILABILITY: public-benchmark-used
CODE_AVAILABILITY: none
PREREGISTRATION: none
EVIDENCE_BASIS: simulation-study
