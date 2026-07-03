MECHANISM: The paper computes a composite objective function called GT-Score to reduce overfitting in optimization problems. The function combines four components: (1) mean strategy return, (2) a logarithmic transformation of a Z-score measuring statistical significance of outperformance relative to a benchmark, (3) an R-squared value quantifying return consistency, and (4) a downside deviation term penalizing negative volatility. The Z-score is calculated as the difference between the strategy's mean return and the benchmark's mean return, divided by the standard error of the strategy's returns. The logarithm of the Z-score acts as a significance gate, compressing large values to prevent dominance by statistical significance alone. The R-squared term ensures consistency by penalizing erratic performance, while the downside deviation term specifically targets downside risk without penalizing upside volatility. The function is optimized using random search over parameter spaces of trading strategies, with a minimum trade threshold to avoid unstable estimates. The optimization process involves walk-forward validation and Monte Carlo trials to assess generalization. The method does not explicitly model uncertainty as a probability distribution but uses frequentist significance tests as heuristic filters.  
DOMAIN: quantitative finance  
STRUCTURE: other: composite objective function  
DATA_OBJECT: sequence or time-series  
INFERENCE: frequentist point estimate  
PROBLEM_FORM: optimization  
DISTRIBUTION: continuous; approximate Gaussian  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
