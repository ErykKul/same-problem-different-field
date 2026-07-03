MECHANISM: The paper computes a hypothesis test for the direct treatment effect on recurrent events while accounting for terminal events. It decomposes the treatment into two components: one affecting recurrent events directly and another influencing survival. The method defines counterfactual outcomes for each treatment component, estimates survival functions using a discrete Kaplan-Meier estimator, and applies inverse probability weighting to adjust for confounding. A proportional rate marginal structural model (PR-MSM) is used to model the counterfactual mean number of recurrent events as a function of treatment, with the rate parameter estimated via an optimization-based score test. The test statistic is formed by standardizing the score function against its estimated variance, derived from cumulative hazard estimates. The approach explicitly separates direct and indirect effects by fixing one treatment component while varying the other, ensuring causal interpretability even under time-varying event rates and differential survival. The method is validated through simulation studies and applied to a real-world dataset to compare treatment effects on gastrointestinal bleeding recurrence.  
DOMAIN: causal inference for recurrent and terminal events  
STRUCTURE: graphical models  
DATA_OBJECT: sequence or time-series  
INFERENCE: optimization only  
PROBLEM_FORM: decision or test  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: public-benchmark-used  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
