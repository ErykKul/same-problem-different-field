MECHANISM: The paper computes a discrete-time Markov chain model to analyze sequential price change transitions in limit orders. Consecutive price changes are categorized into nine discrete states based on magnitude and direction, forming a categorical time series. Transition probability matrices (TPMs) are estimated for each intraday interval and market capitalization tier, capturing the likelihood of moving between states. The G-test of independence is applied to verify short-range dependence in the data, confirming the validity of the Markov assumption. Key metrics derived from the TPMs include spectral gap (measuring convergence rate to stationary distribution), entropy rate (quantifying information content per transition), mixing rate (assessing convergence speed), and mean recurrence time (estimating expected return intervals for states). Stationary distributions are computed to characterize long-term behavior, and clustering techniques (hierarchical and DBSCAN) are used to identify temporal phases in the data. Jensen-Shannon divergence is applied to compare stationary distributions across intervals, revealing distinct temporal regimes. The analysis distinguishes bid and ask sides separately, capturing directional asymmetries in price revision dynamics. The methodology combines statistical hypothesis testing, matrix estimation, and dimensionality reduction (PCA and t-SNE) to summarize and compare intraday patterns across market capitalization tiers.  
DOMAIN: market microstructure  
STRUCTURE: spectral or transform  
DATA_OBJECT: sequence or time-series  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: simulation or generation  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: dataset-in-repository  
CODE_AVAILABILITY: public-repository  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
