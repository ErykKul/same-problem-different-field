MECHANISM: The paper computes a preference-based optimization objective that aligns language models with thermodynamic stability by incorporating energy gaps between candidate sequences. The method begins by defining a physical energy oracle that evaluates the stability of a sequence. A preference pair is formed by contrasting a stable sequence (winner) with an unstable or pathological decoy (loser). The energy gap between these sequences is calculated using a ReLU function applied to the difference in their energy values. This gap is then mapped to an optimization intensity via a sigmoid function, which scales the magnitude of gradient updates. The objective function integrates this energy-weighted term into a modified DPO formulation, where the log-likelihood of preferred responses is multiplied by the energy gap scaling factor. The gradient of the objective is decomposed into a standard DPO error term and a physics-informed gain term, which amplifies updates for sequences with large energy violations while suppressing updates for ambiguous pairs. The method also introduces a hard negative mining strategy to generate adversarial decoys that are linguistically plausible but structurally invalid, ensuring the model learns fine-grained biophysical distinctions. Theoretical analysis shows that the energy-weighted objective reduces gradient variance and aligns with optimizing a Boltzmann distribution over energy differences. The framework maintains a reference model to preserve diversity while focusing optimization on resolving critical stability barriers.  
DOMAIN: protein design and thermodynamics  
STRUCTURE: other: preference-based optimization  
DATA_OBJECT: sequence or time-series  
INFERENCE: optimization only  
PROBLEM_FORM: optimization  
DISTRIBUTION: continuous; Boltzmann  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
