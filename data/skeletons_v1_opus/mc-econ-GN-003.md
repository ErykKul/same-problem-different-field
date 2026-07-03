MECHANISM: Entities are randomly assigned to one of several treatment conditions or a control, with assignment balance across recorded covariates checked by group-difference comparisons. A required sample size is first derived in closed form from target error rates and a standardized effect size. A continuous response is recorded per entity before and after the intervention, and the per-entity change is taken as the outcome. The average causal effect of each condition is estimated by regressing this change on indicator variables for the conditions while including covariate indicators as controls, fitting coefficients by least squares; standard errors and significance of each coefficient are reported. Conditions are compared both in separate fits and in a single joint fit so that their coefficients share a common scale and can be ranked by magnitude. Effect heterogeneity is probed by adding an interaction between a condition indicator and a covariate. To link the continuous outcome to a binary switch, a second model regresses a binary change indicator on the continuous change via a logistic link, yielding an odds-ratio interpretation. Model adequacy is judged by a likelihood-ratio test, deviance reduction, pseudo variance-explained measures, and area under the receiver-operating curve.
DOMAIN: behavioral economics, technology adoption policy
STRUCTURE: dense linear algebra
DATA_OBJECT: set or table
INFERENCE: frequentist point estimate
PROBLEM_FORM: decision or test
DISTRIBUTION: continuous; gaussian
COMPLEXITY: closed-form
