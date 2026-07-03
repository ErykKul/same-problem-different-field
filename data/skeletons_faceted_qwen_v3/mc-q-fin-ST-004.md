MECHANISM: The paper computes regime-dependent predictive relationships between time-series variables using a two-step process. First, it estimates latent regimes via a Student-t Hidden Markov Model (HMM), which partitions the data into distinct states based on multivariate Student-t emission distributions. Second, within each regime, it performs Granger causality tests to determine if lagged values of one variable improve prediction of another, conditional on the target's own history. The algorithm iteratively fits the HMM to identify regime boundaries, then applies autoregressive models with lagged variables to assess predictive precedence. The method explicitly avoids inferring structural causality, instead focusing on temporal dependencies. It uses a Bayesian Information Criterion to select the optimal number of regimes, estimates transition probabilities via EM algorithm, and applies Bonferroni-corrected significance tests across factor pairs. The computational core involves both probabilistic state estimation and statistical hypothesis testing on time-series data.  
DOMAIN: financial econometrics  
STRUCTURE: graphical models  
DATA_OBJECT: sequence or time-series  
INFERENCE: frequentist point estimate  
PROBLEM_FORM: prediction or classification  
DISTRIBUTION: continuous; student-t  
COMPLEXITY: not stated  
DATA_AVAILABILITY: public-benchmark-used  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
