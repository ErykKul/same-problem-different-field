MECHANISM: The paper computes a Gaussian-process-based surrogate model to approximate the output of a stochastic economic dispatch solver under wind power uncertainty. First, wind power generation is represented as a random process with a covariance structure defined by the Karhunen-Loève expansion, which reduces the dimensionality of the uncertainty space. Next, a set of sample points is generated in the reduced-dimensional space by sampling the principal components of the expansion. At each sample point, the economic dispatch solver is evaluated to produce a set of output values (e.g., generator dispatch levels, expected costs). These outputs are then used to train a Gaussian process emulator, which maps inputs (wind power scenarios) to outputs (dispatch results) by learning a probabilistic relationship between them. The emulator's predictive distribution quantifies uncertainty in the dispatch outcomes by propagating the input uncertainty through the model. The method avoids the computational burden of Monte Carlo sampling by replacing the expensive solver evaluations with the fast, interpolated predictions of the Gaussian process. The accuracy of the emulator is validated by comparing its predictions to direct solver evaluations on the IEEE 118-bus test case. The approach is specifically tailored to power systems optimization with renewable energy uncertainty, maintaining domain-specific terminology throughout.
DOMAIN: power systems and uncertainty quantification
STRUCTURE: other: Gaussian process emulation
DATA_OBJECT: continuous function or field
INFERENCE: Bayesian posterior
PROBLEM_FORM: estimation
DISTRIBUTION: continuous; Gaussian
COMPLEXITY: not stated
DATA_AVAILABILITY: public-benchmark-used
CODE_AVAILABILITY: none
PREREGISTRATION: none
EVIDENCE_BASIS: simulation-study
