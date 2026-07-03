MECHANISM: The paper computes a probabilistic clustering of data points into Gaussian-distributed clusters using a mixture model. The algorithm begins by assuming a parameter space where each data point is represented as a vector. The model posits that the data distribution is a weighted sum of multivariate Gaussian distributions, each characterized by a mean vector and covariance matrix. Parameters are estimated using the Expectation-Maximization (EM) algorithm, which iteratively computes the likelihood of data points belonging to each cluster (E-step) and updates the cluster parameters (M-step) to maximize the overall likelihood. Once the model is trained, the association of any new data point with the clusters is determined by comparing the likelihood of the point under each cluster. A subset of clusters is defined, and the Neyman-Pearson test is applied to compute a likelihood ratio, which is compared to a threshold to classify the point into the subset or its complement. The method is applied to two problems: first, to model the distribution of pulsars in a parameter space defined by period and period derivative, and second, to rank the likelihood of unidentified gamma-ray sources being pulsars. The clustering is validated using a multi-dimensional Kolmogorov-Smirnov test to avoid overfitting, and the final classification thresholds are derived empirically from the cluster parameters.  
DOMAIN: pulsar astronomy  
STRUCTURE: graphical models  
DATA_OBJECT: point set  
INFERENCE: Bayesian posterior  
PROBLEM_FORM: classification  
DISTRIBUTION: binary; continuous  
COMPLEXITY: not stated  
DATA_AVAILABILITY: public-benchmark-used  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
