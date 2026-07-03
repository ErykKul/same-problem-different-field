MECHANISM: The paper proposes Z-score Linear Discriminant Analysis (Z-LDA), a modification of standard Linear Discriminant Analysis (LDA) for brain-computer interfaces (BCI). Traditional LDA assumes Gaussian-distributed data with equal covariance matrices across classes, but BCI data often exhibit heteroscedastic class distributions. Z-LDA addresses this by defining a decision boundary using z-scores of projected data, which incorporates both the mean and standard deviation of the projected features. The method projects data onto a discriminative subspace using class means and covariance matrices, then computes z-scores for each class's projected distribution. These z-scores are used to adjust the decision boundary, allowing it to adapt to varying class variances. The algorithm calculates the discriminant function as a weighted combination of the projected mean and standard deviation, with weights derived from the inverse covariance matrix. This approach avoids assuming equal covariance matrices and instead models class-specific variances explicitly. The decision boundary is defined as a threshold on the z-score, which scales the distance between class means relative to their standard deviations. The method is applied to both simulated and real EEG datasets, with classification accuracy evaluated using standard metrics. The paper demonstrates that Z-LDA outperforms conventional LDA in scenarios with heteroscedastic distributions by better capturing class-specific variability.  
DOMAIN: brain-computer interfaces  
STRUCTURE: dense linear algebra  
DATA_OBJECT: dense matrix  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: prediction or classification  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: public-benchmark-used  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
