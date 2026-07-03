MECHANISM: The paper computes an adaptive learning rate for federated post-deployment adaptation under non-stationary distribution shifts. It estimates two signals: uncertainty dynamics, which measures changes in predictive uncertainty via cosine distance between consecutive softmax output vectors averaged over data batches, and representation dynamics, which measures embedding-level drift via cosine distance between normalized batch-mean feature representations. These signals are combined into a per-client, per-timestep adaptive learning rate scaled between minimum and maximum bounds. The learning rate is applied in a federated setting where clients update shared and personalized model layers using an unsupervised risk estimator derived from pseudo-labels corrected via a confusion matrix. The method includes theoretical guarantees showing that the dynamics signals approximate true distribution shifts and achieve dynamic regret bounds with convergence under non-stationary conditions. The algorithm alternates between local gradient updates with adaptive learning rates and global aggregation of shared model parameters.  
DOMAIN: federated learning with distribution shifts  
STRUCTURE: dynamic programming  
DATA_OBJECT: graph or network  
INFERENCE: optimization only  
PROBLEM_FORM: optimization  
DISTRIBUTION: none  
COMPLEXITY: convergence rate  
DATA_AVAILABILITY: dataset-with-DOI-or-handle  
CODE_AVAILABILITY: public-repository  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
