MECHANISM: The paper computes a Bayesian calibration framework that integrates high- and low-fidelity data sources to optimize system parameters under uncertainty. It models the relationship between low-fidelity outputs and high-fidelity outputs via a Gaussian Process (GP) structure, where high-fidelity outputs are expressed as a scaled version of low-fidelity outputs plus a systematic discrepancy term. The framework estimates calibration parameters and discrepancy hyperparameters using maximum likelihood estimation, iteratively refining predictions through posterior inference. It constructs a joint GP model for both low- and high-fidelity data, incorporating covariance functions to capture input correlations. The posterior predictive distribution is derived to approximate the true system output at new input locations, enabling uncertainty quantification. Decision analysis is performed by sampling from the posterior predictive distribution, evaluating the objective function across candidate inputs, and identifying optimal settings that minimize the objective while accounting for parameter uncertainty. The workflow includes data collection, model calibration, prediction, and decision-making, with emphasis on handling discrepancies between model predictions and physical measurements. The method assumes Gaussian process priors for both low- and high-fidelity outputs, with separable power exponential covariance functions to model spatial dependencies. Parameter estimation involves maximizing the marginal likelihood of the discrepancy process, and uncertainty in calibration parameters is approximated via leave-one-out cross-validation. The final decision is based on the distribution of optimal inputs derived from the posterior predictive model, ensuring robustness to model uncertainty and computational constraints.
DOMAIN: manufacturing process optimization
STRUCTURE: other: Gaussian process-based multi-fidelity modeling
DATA_OBJECT: continuous function or field
INFERENCE: Bayesian posterior
PROBLEM_FORM: optimization
DISTRIBUTION: continuous; Gaussian
COMPLEXITY: not stated
DATA_AVAILABILITY: none
CODE_AVAILABILITY: none
PREREGISTRATION: none
EVIDENCE_BASIS: empirical-with-released-data
