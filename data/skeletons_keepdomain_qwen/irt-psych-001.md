MECHANISM: The paper introduces two estimators for item parameters in the Rasch model: random pairing maximum likelihood estimator (RP-MLE) and its bootstrapped variant multiple random pairing MLE (MRP-MLE). The RP-MLE constructs item-item comparisons by randomly pairing user-item response pairs, reducing the problem size while preserving statistical independence. The method computes the maximum likelihood estimate of item parameters by optimizing the likelihood function over the paired comparisons. The MRP-MLE extends this by applying bootstrap resampling to the paired data, generating multiple estimates to quantify uncertainty in the item parameters. Both estimators are designed to handle sparse binary response data, where each response is a 0 or 1 indicating whether a user answered an item correctly. The optimization process involves solving a non-convex likelihood maximization problem, which is approximated using iterative numerical methods. The paper proves that the estimators achieve minimax optimality in finite sample $\ell_{\infty}$ error, ensuring robust parameter estimation even with sparse observations. The distributional characterization of the estimators allows for the construction of confidence intervals via asymptotic normality or bootstrap-based methods. The method is applied to both simulated datasets and real-world psychometric data to validate its performance. The computational steps include data pairing, likelihood computation, optimization, and uncertainty quantification through bootstrapping. The approach avoids explicit matrix inversion or decomposition, relying instead on stochastic pairing and iterative optimization.  
DOMAIN: psychometrics and item response theory  
STRUCTURE: optimization  
DATA_OBJECT: binary response matrix  
INFERENCE: frequentist point estimate  
PROBLEM_FORM: estimation  
DISTRIBUTION: binary; Rasch model  
COMPLEXITY: finite-sample bound  
DATA_AVAILABILITY: public-benchmark-used  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
