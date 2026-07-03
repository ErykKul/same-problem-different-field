MECHANISM: The paper computes treatment effect estimates using generalized pairwise comparisons (GPC) by comparing all possible pairs of individuals across treatment and control groups. For each pair, outcomes are ranked hierarchically according to clinical importance, and a comparison score (favorable, unfavorable, or neutral) is assigned. Aggregation of these scores yields win odds (WO), which quantify the treatment effect as the ratio of favorable to unfavorable pairs, adjusted for neutral pairs. To address clustering and temporal trends, hierarchical mixed-effects models are applied to cluster-period win odds, incorporating random slopes for cluster-specific treatment effects and fixed effects for time. Probabilistic index models (PIMs) are used to adjust for covariates by linking win odds to regression coefficients through a link function. The analysis includes stratification by cluster or period, inverse-variance weighting of stratum-specific estimates, and estimation of net treatment benefit (NTB) as a probability-scale measure. Simulation studies evaluate type I error control, power, and robustness under varying intraclass correlations, cluster autocorrelation, and time effects. The methods are implemented using mixed-effects models with random intercepts and slopes, and the win odds are estimated via log-linear aggregation of cluster-specific results.  
DOMAIN: clinical trial statistics  
STRUCTURE: other: mixed-effects modeling  
DATA_OBJECT: set or table  
INFERENCE: frequentist point estimate  
PROBLEM_FORM: estimation  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: simulation-study
