MECHANISM: The paper computes a statistical model where the hazard rate function is expressed as a linear combination of covariates and time-dependent hazard factor functions. The model combines parametric and nonparametric components: some hazard factors are specified with parametric forms (e.g., linear, exponential), while others remain unspecified. Estimation involves two steps: first, parametric components are estimated by minimizing an integrated weighted quadratic form, which compares the parametric hazard functions to nonparametric estimates derived from the data. Second, nonparametric components are estimated using integrated weighted least squares, leveraging martingale-based methods to account for censoring and time-dependent covariates. The parametric estimation employs maximum likelihood, while the nonparametric part uses a plug-in approach, substituting estimated parametric components into the nonparametric estimator. Large-sample properties are derived, including asymptotic normality for both parametric and nonparametric estimators, and the paper constructs goodness-of-fit tests (e.g., chi-squared) to assess the adequacy of parametric assumptions. The method also quantifies precision gains from hybrid parametric-nonparametric modeling compared to fully nonparametric approaches. Simulations and real-data applications validate the method's performance.  
DOMAIN: survival analysis  
STRUCTURE: other: optimization and nonparametric estimation  
DATA_OBJECT: continuous function or field  
INFERENCE: frequentist point estimate  
PROBLEM_FORM: estimation  
DISTRIBUTION: continuous; nonnegative  
COMPLEXITY: consistency  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: simulation-study
