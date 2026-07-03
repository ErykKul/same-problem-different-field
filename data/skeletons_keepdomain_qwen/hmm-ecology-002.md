MECHANISM: The paper computes a Hidden Markov Movement Model (HMMM) to identify behavioral states from animal tracks with negligible measurement error. The model is based on the process equation of the first-Difference Correlated Random Walk with Switching (DCRWS), which defines the movement dynamics as a continuous-time stochastic process with switching between behavioral states. The HMMM uses a discrete-time hidden Markov framework where each state corresponds to a distinct behavioral mode, and transitions between states are governed by a Markov chain with time-homogeneous transition probabilities. Observations are modeled as noisy measurements of the true location, with the noise distribution assumed to be Gaussian. The model parameters include the transition matrix, the observation matrix, and the process noise covariance. Maximum likelihood estimation is performed using the R package TMB, which implements automatic differentiation and Laplace approximation for efficient parameter inference. The algorithm iteratively updates the posterior distribution of the hidden states and model parameters via the Expectation-Maximization (EM) algorithm, with the E-step computing the expected complete-data log-likelihood and the M-step optimizing the parameters. The model is compared to a modified DCRWS (DCRWS NOME) and a common HMM (moveHMM) using real and simulated data. The HMMM is validated by fitting it to tracks from grey seals, lake trout, and blue sharks, demonstrating its accuracy and applicability across species. The method is implemented in the R package swim for broader use.
DOMAIN: animal movement analysis
STRUCTURE: graphical models
DATA_OBJECT: sequence or time-series
INFERENCE: deterministic or closed-form
PROBLEM_FORM: estimation
DISTRIBUTION: none
COMPLEXITY: not stated
DATA_AVAILABILITY: none
CODE_AVAILABILITY: public-repository
PREREGISTRATION: none
EVIDENCE_BASIS: empirical-with-private-data
