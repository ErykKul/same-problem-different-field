MECHANISM: This paper computes a robust graph fine-tuning method by formulating the problem as a min-max optimization. The inner maximization generates adversarial noise to degrade model performance, while the outer minimization learns prompts to counteract this noise. The adversarial noise is constrained to specific perturbation limits, and the prompts are optimized through alternating updates. The inner maximization uses a Joint Projected Gradient Descent algorithm to simultaneously attack node features and graph topology. The outer minimization employs a parameterized function to compute learnable prompts that are added to node features in each layer of the pre-trained GNN. The process iterates between generating adversarial noise and optimizing prompts until convergence. The method ensures robustness by explicitly modeling worst-case perturbations and training the model to minimize their impact. The optimization alternates between solving the inner maximization (adversarial noise generation) and outer minimization (prompt learning), with constraints applied to maintain perturbation feasibility. The final prompts are derived through a bottleneck function that processes node features and learns parameters to enhance robustness against both topological and feature-based attacks. The framework is general and can be integrated with various pre-trained GNN models.  
DOMAIN: graph neural networks  
STRUCTURE: other: alternating optimization  
DATA_OBJECT: graph or network  
INFERENCE: optimization only  
PROBLEM_FORM: optimization  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: public-benchmark-used  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
