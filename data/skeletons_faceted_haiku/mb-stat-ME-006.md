MECHANISM: A survival analysis framework decomposes total mortality into four components: cancer deaths, baseline health differences, treatment-induced other-cause deaths, and general population other-cause mortality. The Pohar Perme estimator is a reweighting method that estimates net survival by removing general population mortality from observed total mortality using inverse probability weights. The weights are constructed from the probability of survival in the general population matched by age and other covariates. This produces an estimate of survival conditional on the cancer patient living under general population mortality only. The method is analyzed theoretically to determine what estimand it actually targets, revealing discrepancies when cancer patients have elevated other-cause mortality relative to the general population.
DOMAIN: survival analysis and competing risks
STRUCTURE: other: inverse probability weighting
DATA_OBJECT: sequence or time-series
INFERENCE: frequentist point estimate
PROBLEM_FORM: estimation
DISTRIBUTION: survival or time-to-event
COMPLEXITY: not stated
