MECHANISM: Reduce dataset bias by combining sample and feature weighting. Train a domain classifier to distinguish biased samples from representative ones, extract feature importances, and convert them to feature weights using softmin (downweighting important/biased features). Iteratively remove samples identified as non-representative by the classifier until it can no longer distinguish the two distributions (AUROC falls below 0.5). Return both sample and feature weights for reweighting the biased dataset for downstream tasks.
DOMAIN: Dataset debiasing, domain adaptation, tabular machine learning
STRUCTURE: other: iterative resampling with classifier-based sample selection
DATA_OBJECT: set or table
INFERENCE: frequentist point estimate
PROBLEM_FORM: decision or test
DISTRIBUTION: none
COMPLEXITY: polynomial iterative
