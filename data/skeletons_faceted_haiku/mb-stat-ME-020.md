MECHANISM: Cluster predictors using correlation-based hierarchical clustering, then test each cluster (whether nested, singleton, or composite) via a hypothesis test against a null that the cluster contains no true effects. Develop a generalized linear step-up procedure that ranks p-values and rejects a closure-respecting set of null hypotheses by comparing each p-value against a scaled threshold, with a weighting scheme that counts partial discoveries fractionally (e.g., selecting a set of k items as one unit counts as 1/k discoveries rather than k). Control false discovery rate by defining discoveries as the weighted sum of minimal rejected hypotheses only, avoiding double-counting when one hypothesis implies another.
DOMAIN: Statistical hypothesis testing and false discovery rate control
STRUCTURE: graph traversal
DATA_OBJECT: graph or network
INFERENCE: frequentist point estimate
PROBLEM_FORM: decision or test
DISTRIBUTION: none
COMPLEXITY: not stated
