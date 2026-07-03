MECHANISM: A linear regression model with unknown parameters is solved using a hybrid dynamical system that alternates between continuous gradient flows and discrete jumps. Two coupled parameter estimators evolve continuously under scaled gradient dynamics during flows. At predetermined time intervals, a discrete reset combines the two estimators using a functional that depends on the state-transition matrix computed from the gradient trajectories. The combination is designed such that after the first reset, both estimators equal the true parameters. The method works by exploiting the difference in convergence rates of two differently-scaled gradient flows to achieve finite-time parameter recovery without persistent excitation.
DOMAIN: parameter estimation and identification
STRUCTURE: finite-state machine
DATA_OBJECT: dense matrix or tensor
INFERENCE: deterministic or closed-form
PROBLEM_FORM: estimation
DISTRIBUTION: none
COMPLEXITY: not stated
