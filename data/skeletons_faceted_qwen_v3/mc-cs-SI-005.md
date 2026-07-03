MECHANISM: The paper computes a voting mechanism that optimizes social welfare while ensuring anonymity and neutrality. It transforms voter preference profiles into a bipartite graph, where voters and candidates are nodes connected by edges representing preference scores. A permutation-equivariant graph neural network (GEVN) processes this graph to output a probability distribution over candidates, representing the probabilistic social choice function (PSCF). The GEVN is trained using a welfare-maximizing loss function that directly optimizes the expected social welfare, defined as the weighted sum of candidate utilities under the distribution. To enforce monotonicity, a monotonicity loss is introduced, penalizing decreases in candidate selection probabilities when preference scores increase. A separate adversarial module (GESN) generates strategic preference profiles by optimizing a rational loss that maximizes individual voter utility under the PSCF. The GESN and GEVN are jointly trained in an adversarial manner, with the GEVN's parameters frozen during GESN gradient updates to prevent interference. The method generalizes to arbitrary numbers of voters and candidates by leveraging permutation-equivariant operations, ensuring anonymity and neutrality without explicit constraints. The final PSCF is converted to a deterministic voting rule via argmax over probabilities, and the model is evaluated on synthetic and real-world datasets to validate resilience against strategic voting.  
DOMAIN: voting mechanisms and elections  
STRUCTURE: graph traversal  
DATA_OBJECT: graph or network  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: optimization  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: public-benchmark-used  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
