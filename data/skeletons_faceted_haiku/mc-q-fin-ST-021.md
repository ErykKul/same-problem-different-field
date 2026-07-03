MECHANISM: Constructs supervised binary classification task with rolling window; engineers features from three complementary classes: intrinsic OHLC prices, historical volatility indicators (Donchian Channel, Bollinger Bands, Keltner Channel computed over 20-day window), and nowcasting ratios (log-ratios of intraday prices relative to open); trains eight diverse classifiers (Decision Tree, Naive Bayes, k-NN, Logistic Regression, XGBoost, MLP, CatBoost, ExtraTreesClassifier) on 80% train split and evaluates on 20% test split; computes per-feature importance via Shapley values for explainability.
DOMAIN: Healthcare sector index price movement prediction and feature analysis
STRUCTURE: combinational logic
DATA_OBJECT: sequence or time-series
INFERENCE: frequentist point estimate
PROBLEM_FORM: prediction or classification
DISTRIBUTION: binary; binary
COMPLEXITY: polynomial iterative
