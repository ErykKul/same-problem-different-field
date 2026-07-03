MECHANISM: Trains five base models (SVM, Random Forest, XGBoost, CNN, LSTM) to predict time-series values; generates prediction distributions via normal approximations; measures diversity between models using rank-score characteristic functions and computes cognitive diversity as Euclidean distance between RSC curves; combines multiple models using score averaging, rank averaging, or weighted combinations with diversity-based weights; selects final output by choosing highest-probability value from combined distribution; evaluates performance with mean squared error and mean absolute percentage error.
DOMAIN: Bitcoin price prediction via ensemble machine learning
STRUCTURE: other: ensemble learning with model fusion
DATA_OBJECT: sequence or time-series
INFERENCE: frequentist point estimate
PROBLEM_FORM: prediction or classification
DISTRIBUTION: continuous; continuous
COMPLEXITY: polynomial iterative
