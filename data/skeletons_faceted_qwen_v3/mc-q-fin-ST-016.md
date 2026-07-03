MECHANISM: The paper computes a statistical procedure to distinguish between multiscaling arising from distributional properties or temporal dependencies. It first establishes multiscaling by applying weighted least squares regression to quantify how moments of absolute returns scale with time aggregation, accounting for heteroscedastic errors. The regression estimates a generalized Hurst exponent $H(q)$ as a linear function of moment order $q$, with the slope $B$ serving as a multiscaling proxy. To isolate distributional effects, it generates shuffled surrogates that preserve return distributions while destroying temporal correlations using distance-based permutation tests. These surrogates are compared against the original data to assess whether multiscaling persists. The method is validated using synthetic processes with known multifractal properties, such as the Multifractal Random Walk (MRW) and Fractional Lévy Stable Motion (FLSM). The analysis involves normalizing and standardizing moment estimates to ensure robustness, particularly for heavy-tailed distributions. The procedure includes estimating tail exponents via maximum likelihood for stable distributions to determine valid ranges for moment orders $q$. The final comparison between original and surrogate data determines whether multiscaling is attributable to distributional features or temporal structure. The approach combines regression, permutation testing, and synthetic validation to address the problem of source attribution in multiscaling phenomena.  
DOMAIN: financial modeling  
STRUCTURE: other: statistical testing  
DATA_OBJECT: sequence or time-series  
INFERENCE: frequentist point estimate  
PROBLEM_FORM: estimation  
DISTRIBUTION: heavy-tailed; Gaussian  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: simulation-study
