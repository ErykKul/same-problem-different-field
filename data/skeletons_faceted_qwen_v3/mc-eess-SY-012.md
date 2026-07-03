MECHANISM: The paper computes a set of functions that satisfy specific stability conditions for a system governed by switching rules. It constructs candidate functions using neural networks, where each function corresponds to a system mode. The functions must satisfy two properties: (1) they decrease along the system's dynamics within their mode, and (2) they decrease when switching between modes. To enforce these properties, the method defines loss functions that penalize violations of these conditions. For the first property, the loss ensures that the function's derivative (in continuous time) or its value difference (in discrete time) is negative, while also ensuring the function remains positive. For the second property, the loss ensures that the function value in the target mode is lower than in the source mode within switching regions. These losses are minimized using gradient descent, but the training is augmented with a verification step. An SMT solver checks whether the candidate functions satisfy all required properties over a domain excluding a neighborhood around the equilibrium. If violations are found, counterexamples are added to the training data, and the process repeats. The method combines neural network training with formal verification to ensure the functions rigorously satisfy stability conditions. The overall process iterates between training to minimize losses and verification to eliminate violations, ensuring the final functions meet both mode-wise and switching decrease requirements.  
DOMAIN: control theory  
STRUCTURE: other: neural network training with verification  
DATA_OBJECT: continuous function or field  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: proof or characterization  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: simulation-study
