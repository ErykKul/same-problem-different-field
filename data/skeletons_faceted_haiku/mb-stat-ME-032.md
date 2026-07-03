MECHANISM: Extends semiparametric linear hazard regression to allow three choices per covariate: time-varying (nonparametric) effect, constant (parametric) effect, or exclusion, yielding 3^q candidate models. Focused information criterion ranks models by minimizing estimated mean squared error for a chosen estimand (e.g., survival probability). Variance and squared bias components are estimated from data; variance stems from martingale-based least-squares estimators, bias from the difference to the full model. Weighted versions (wFIC) allow heterogeneous importance across estimands or covariate regions. Model averaging constructs weighted combinations of top-ranking candidates.
DOMAIN: Survival analysis, semiparametric model selection
STRUCTURE: other: focused estimation with variance-bias decomposition
DATA_OBJECT: sequence or time-series (censored event times with covariates)
INFERENCE: frequentist point estimate
PROBLEM_FORM: decision or test
DISTRIBUTION: survival or time-to-event; estimator assumes no specific parametric form for the cumulative hazard
COMPLEXITY: not stated
