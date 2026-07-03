MECHANISM: The paper computes a variational Bayesian learning procedure for nonlinear state-space models using sparse Gaussian processes. The algorithm combines variational Bayes with sequential Monte Carlo to approximate the posterior distribution over the model's latent states and parameters. The method introduces a hybrid inference approach that alternates between variational updates to the approximate posterior and particle-based sampling to refine the approximation. Stochastic variational inference is applied to scale the method to long time series by using mini-batches of data. Online learning is implemented through incremental updates to the variational parameters as new data points arrive. The sparse Gaussian process is used to model the nonlinear dynamics, with inducing points selected to reduce computational complexity. The posterior over the model's parameters is tractable due to the variational approximation, which avoids the intractability of exact Bayesian inference. The algorithm maintains a balance between model capacity and computational cost by adjusting the number of inducing points and the variational approximation's precision. The method is evaluated through its ability to trade off accuracy and speed while avoiding overfitting compared to conventional parametric models. The core computation involves optimizing the variational lower bound using gradient-based methods, with the sequential Monte Carlo component providing uncertainty estimates for the latent states. The approach is designed to handle high-dimensional and nonlinear dynamics in time-series data without requiring explicit parametrization of the state transitions.

DOMAIN: nonlinear dynamical systems

STRUCTURE: other: hybrid variational-inference

DATA_OBJECT: continuous function or field

INFERENCE: variational

PROBLEM_FORM: estimation

DISTRIBUTION: none

COMPLEXITY: not stated

DATA_AVAILABILITY: none

CODE_AVAILABILITY: none

PREREGISTRATION: none

EVIDENCE_BASIS: mathematical-proof
