MECHANISM: Formulates a composite objective function (GT-Score) combining mean strategy return, statistical significance (z-score of outperformance), consistency (R-squared of returns), and downside deviation via multiplicative structure; applies random search optimization over trading strategy parameters; compares against three baseline objectives (simple profit, Sharpe Ratio, Sortino Ratio) using identical evaluation budgets; evaluates via walk-forward validation with sequential train/validation splits and embargo periods; performs Monte Carlo analysis with multiple random seeds; computes generalization ratio as validation return divided by training return; reports Diebold-Mariano tests and backtesting Sharpe ratios.
DOMAIN: Quantitative trading strategy selection and overfitting reduction
STRUCTURE: combinational logic
DATA_OBJECT: sequence or time-series
INFERENCE: frequentist point estimate
PROBLEM_FORM: optimization
DISTRIBUTION: continuous; continuous
COMPLEXITY: not stated
