MECHANISM: Limit order price changes are categorized into nine discrete states based on percentage deviation from the previous price, and modeled using a discrete-time Markov chain to capture temporal dependencies in state transitions. The transition probability matrix is estimated from consecutive price changes for fixed quote sides and intraday intervals. Statistical testing (G-test) validates that price changes exhibit first-order Markov dependence rather than independence. The model predicts subsequent state transitions given the current state, conditioned on firm size (market capitalization tier). The framework applies separately to buy and sell sides across different times of day and across asset size categories to study how limit order dynamics vary systematically across the cross-section.
DOMAIN: Market microstructure and intraday price dynamics
STRUCTURE: finite-state machine
DATA_OBJECT: sequence or time-series
INFERENCE: frequentist point estimate
PROBLEM_FORM: prediction or classification
DISTRIBUTION: ordinal
COMPLEXITY: polynomial iterative
