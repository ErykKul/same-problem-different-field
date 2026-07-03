MECHANISM: A semiparametric framework jointly models Value-at-Risk (VaR) and Expected Shortfall (ES) by decomposing tail risk into two layers: VaR dynamics governed by conditional quantile equations (following CAViaR), and tail thickness governed by a latent tail state variable. Multiple realized measures (jump-robust continuous variance, bipower variation) are aggregated via a dynamic factor model to extract common high-frequency tail risk factors. These factors drive the tail severity gap (ES minus VaR) rather than the quantile level itself. The model uses joint elicitability framework to enable consistent estimation and backtesting without fully specifying the conditional distribution. Measurement equations transform realized measures into risk innovations; factor dynamics capture their common evolution; the tail-generating mechanism characterizes conditional loss severity beyond the quantile.
DOMAIN: Financial econometrics and tail risk forecasting
STRUCTURE: other: factor model with recursive quantile equations
DATA_OBJECT: time-series or sequence
INFERENCE: variational
PROBLEM_FORM: prediction or classification
DISTRIBUTION: continuous and heavy-tailed
COMPLEXITY: polynomial iterative
