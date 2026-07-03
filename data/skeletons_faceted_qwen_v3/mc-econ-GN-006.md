MECHANISM: The paper computes a semiparametric model that jointly estimates Value-at-Risk (VaR) and Expected Shortfall (ES) by incorporating high-frequency realized measures into a dynamic factor structure. The model introduces a latent tail state variable to capture time-varying tail thickness and risk intensity, distinguishing between changes in risk location (governed by conditional quantile dynamics) and tail-generating mechanisms. Realized measures are transformed into high-frequency risk innovations through measurement equations, which are then aggregated via a dynamic factor model to extract common tail risk factors. These factors influence the latent tail state variable, which modulates the ES-VaR gap. The model avoids full parametric distributional assumptions by relying on recursive quantile dynamics (e.g., CAViaR) for VaR and a semiparametric specification for tail thickness. Joint estimation of VaR and ES is enabled through scoring rules that exploit their elicitability. The dynamic factor model reduces dimensionality by extracting a single latent risk factor from multiple correlated realized measures, mitigating collinearity and parameter instability. The framework is validated through out-of-sample forecasting and backtesting against benchmarks like quantile regression and GARCH-type models.  
DOMAIN: financial econometrics and risk management  
STRUCTURE: dynamic factor model  
DATA_OBJECT: point set  
INFERENCE: none  
PROBLEM_FORM: estimation  
DISTRIBUTION: continuous; semiparametric  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
