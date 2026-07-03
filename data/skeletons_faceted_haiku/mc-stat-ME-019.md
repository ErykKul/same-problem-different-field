MECHANISM: An ensemble of decision trees is grown on outcome and covariate data using a splitting rule that targets treatment-effect heterogeneity. Each tree recursively partitions the feature space to maximize differences in response to treatment between subgroups. Multiple trees are aggregated to identify patient profiles with differential treatment benefit. The method does not require pre-specified outcome labels but discovers structure from the outcome distribution.
DOMAIN: Survival analysis, precision medicine, machine learning
STRUCTURE: graph traversal
DATA_OBJECT: tree or hierarchy
INFERENCE: frequentist point estimate
PROBLEM_FORM: prediction or classification
DISTRIBUTION: survival or time-to-event measured distribution, none assumed
COMPLEXITY: not stated
