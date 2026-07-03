MECHANISM: When multiple plausible causal models exist with different identifying assumptions, a weighted combination of effect estimates from each model is computed. Each model specifies a causal functional (e.g., an instrumental variable estimator, a regression adjustment estimator) and an identifying assumption set. A model validity measure is derived by testing whether the identifying assumptions hold using causal discovery criteria (e.g., d-separation). Data-driven weights are constructed from these validity measures. A triangulation functional is defined as a weighted average of the individual model estimates, with weights proportional to validity measures. Statistical inference is derived using semiparametric theory, yielding valid confidence intervals for the triangulated estimate. The framework avoids explicit model selection by maintaining a weighted combination of all candidates.
DOMAIN: causal inference and observational data
STRUCTURE: other: weighted ensemble
DATA_OBJECT: dense matrix or tensor
INFERENCE: frequentist point estimate
PROBLEM_FORM: estimation
DISTRIBUTION: none
COMPLEXITY: polynomial iterative
