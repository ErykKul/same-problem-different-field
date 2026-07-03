MECHANISM: The paper computes an estimator for item parameters in a probabilistic model by transforming user-item response data into item-item comparisons through random pairing. The process begins by randomly pairing responses from the same user to different items, forming synthetic item-item comparisons that preserve statistical independence. These comparisons are modeled as a Bradley-Terry-Luce (BTL) process, where the probability of one item "beating" another depends exponentially on their latent parameters. The transformed data is then used to compute a maximum likelihood estimator (MLE) for the item parameters. A bootstrapped variant (MRP-MLE) improves accuracy by repeating the pairing and estimation process with different random splits and averaging results. The method provides finite-sample guarantees on the $\ell_{\infty}$ error of the estimator, ensuring that individual parameter estimates are close to their true values. It also derives the asymptotic distribution of the estimator, enabling uncertainty quantification such as confidence intervals. The algorithm relies on sparse data structures and operates under assumptions about the sparsity and independence of observations. Theoretical analysis shows that the estimator achieves minimax optimal error rates and can recover top-$K$ items with minimal sample complexity. The method is distinct from prior approaches like spectral estimation or conditional MLE, as it explicitly leverages pairwise comparisons and avoids assumptions about user parameters.  
DOMAIN: psychometrics and item response theory  
STRUCTURE: other: item comparison transformation  
DATA_OBJECT: sparse matrix  
INFERENCE: frequentist point estimate  
PROBLEM_FORM: estimation  
DISTRIBUTION: none  
COMPLEXITY: finite-sample bound  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
