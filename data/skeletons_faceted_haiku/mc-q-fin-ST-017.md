MECHANISM: Fits parametric distributions (Gamma, Weibull, Lognormal) to compositional probability vectors via interval-censored maximum likelihood, comparing fits using cross-entropy minimization. Computes Wasserstein-1 distance between two observed distributions as a time series summary. Detects structural breaks in the divergence series using Bai-Perron partitioning minimization with HAC-robust inference. Applies generalized Pareto distribution fitting above thresholds to characterize tail behavior, using maximum likelihood with fallback to probability-weighted moments. Evaluates all fits using strictly proper scoring rules (CRPS and Kullback-Leibler divergence). Performs threshold stability diagnostics to assess GPD model appropriateness on bounded support.
DOMAIN: Distributional inference and statistical modeling in tourism revenue analytics
STRUCTURE: dense linear algebra
DATA_OBJECT: sequence or time-series
INFERENCE: frequentist point estimate
PROBLEM_FORM: estimation
DISTRIBUTION: continuous; continuous
COMPLEXITY: polynomial iterative
