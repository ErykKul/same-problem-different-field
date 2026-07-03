MECHANISM: Transform text messages through tokenization and contextual embedding using a pre-trained bidirectional transformer encoder that processes entire sequences to generate contextualized word representations. Fine-tune the encoder on the spam detection task and extract fixed-size vector representations. Apply multiple classification algorithms (logistic regression, naive Bayes, random forest, gradient boosting, support vector machine) to predict message class from embedded vectors.
DOMAIN: Text message classification and spam detection
STRUCTURE: other: deep-learning transformer
DATA_OBJECT: sequence or time-series
INFERENCE: frequentist point estimate
PROBLEM_FORM: classification
DISTRIBUTION: binary; binary
COMPLEXITY: polynomial iterative
