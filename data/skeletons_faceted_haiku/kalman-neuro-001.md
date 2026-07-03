MECHANISM: Derive the Kalman filter as the steady-state solution of gradient descent on variational free energy. Represent a dynamical system with latent states and observations using a linear Gaussian generative model. Formulate variational free energy as an upper bound on prediction error, minimized over the posterior distribution. Compute gradient descent dynamics with respect to the posterior mean and covariance: the mean-update gradient yields the Kalman gain multiplied by the measurement residual; the covariance-update gradient yields the posterior error covariance. At steady-state, these gradient equations recover the standard Kalman filter prediction and correction steps.
DOMAIN: Neuroscience and Bayesian brain hypothesis.
STRUCTURE: dynamic programming
DATA_OBJECT: sequence or time-series
INFERENCE: Bayesian posterior
PROBLEM_FORM: estimation
DISTRIBUTION: continuous; continuous
COMPLEXITY: polynomial iterative
