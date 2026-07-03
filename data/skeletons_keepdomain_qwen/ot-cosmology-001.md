MECHANISM: The paper computes a reconstruction of the early Universe's density fluctuations by formulating the problem as an optimization task with constraints derived from observed galaxy distributions. The method defines a cost function that measures the discrepancy between simulated and observed density fields, incorporating a regularization term to enforce physical plausibility. The optimization is performed using gradient-based numerical methods, iteratively adjusting the initial density field to minimize the cost function. The algorithm enforces mass conservation through a constraint that the total mass of the reconstructed field matches the observed distribution. The solution is validated by comparing the reconstructed initial conditions to those from N-body simulations, quantifying agreement through statistical metrics. The method does not assume a specific cosmological model, instead relying on the observed galaxy distribution as the sole input. The optimization is constrained by the observed velocity field of galaxies, which is treated as a fixed parameter. The algorithm's performance is evaluated using metrics such as mean squared error between reconstructed and true initial conditions. The computational steps involve discretizing the density field into a grid, applying a variational approach to derive the optimization problem, and solving it using iterative numerical techniques. The method is tested on synthetic data generated from N-body simulations to assess its accuracy and robustness. The reconstruction process is deterministic, with no explicit probabilistic modeling of uncertainties. The final output is a high-resolution map of the initial density field that serves as input for cosmological simulations.

DOMAIN: cosmology, early universe reconstruction

STRUCTURE: other: optimization-based

DATA_OBJECT: continuous function or field

INFERENCE: deterministic or closed-form

PROBLEM_FORM: estimation

DISTRIBUTION: none

COMPLEXITY: not stated

DATA_AVAILABILITY: public-benchmark-used

CODE_AVAILABILITY: none

PREREGISTRATION: none

EVIDENCE_BASIS: simulation-study
