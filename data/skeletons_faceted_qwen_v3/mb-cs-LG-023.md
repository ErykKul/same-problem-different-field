MECHANISM: The paper computes a method to adjust sample weights in a dataset by incorporating feature weights derived from a domain classifier. The algorithm begins by training a classifier to distinguish between representative and non-representative samples. Feature importances are extracted from this classifier, with highly biased features (those that strongly differentiate the two classes) assigned lower weights. These feature weights are transformed using a softmin function with a temperature parameter, which scales the influence of each feature. The algorithm then iteratively removes samples from the non-representative dataset based on their combined sample and feature weights, prioritizing the removal of samples most confidently identified as non-representative. This process continues until the classifier can no longer differentiate between the datasets, at which point the adjusted sample weights align the distributions. The method ensures that highly biased features have reduced influence on the sample weighting process, preserving more instances for downstream tasks. The temperature parameter controls the sharpness of the feature weight distribution, with lower values emphasizing differences in feature importance. The algorithm uses cross-validation to optimize hyperparameters and evaluates performance using metrics like AUROC and maximum mean discrepancy (MMD). The final output includes both sample and feature weights, which can be applied to reweight the dataset for subsequent analysis. The method is validated empirically on multiple datasets, demonstrating its effectiveness in reducing bias while maintaining predictive performance.  
DOMAIN: social sciences  
STRUCTURE: other: iterative optimization  
DATA_OBJECT: set or table  
INFERENCE: frequentist point estimate  
PROBLEM_FORM: estimation  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: public-benchmark-used  
CODE_AVAILABILITY: public-repository  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
