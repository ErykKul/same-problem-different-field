MECHANISM: The paper derives Kalman filters as the steady-state solution of gradient descent on variational free energy. It begins by formulating a probabilistic model of hidden variables in a dynamical system under linear Gauss-Markov assumptions. The variational free energy is defined as the negative log of the marginal likelihood of observed data, augmented by a variational approximation to the posterior distribution over hidden states. Gradient descent is applied to minimize this free energy, leading to iterative updates of the posterior mean and covariance of hidden variables. The derivation shows that the Kalman filter equations emerge as the fixed-point solution of this gradient descent process when the variational approximation matches the true posterior. The method leverages the equivalence between free energy minimization and maximum a posteriori estimation under Gaussian assumptions. The paper emphasizes that this derivation aligns with active inference frameworks, which model neural computation as gradient descent on variational free energy. The approach bridges probabilistic inference and neural dynamics by framing Kalman filtering as an optimization of a variational objective. The algorithm operates on continuous-time dynamical systems with Gaussian noise, and the solution is derived analytically without requiring sampling or Monte Carlo methods. The derivation is validated through theoretical consistency with existing Kalman filter formulations and their application in neuroscience and robotics. The paper does not introduce new computational steps beyond the standard Kalman filter but provides a novel theoretical justification rooted in variational inference.

DOMAIN: computational neuroscience and Bayesian inference

STRUCTURE: optimization

DATA_OBJECT: continuous function or field

INFERENCE: Bayesian posterior

PROBLEM_FORM: estimation

DISTRIBUTION: continuous; Gaussian

COMPLEXITY: not stated

DATA_AVAILABILITY: none

CODE_AVAILABILITY: none

PREREGISTRATION: none

EVIDENCE_BASIS: mathematical-proof
