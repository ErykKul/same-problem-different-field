MECHANISM: The paper computes a joint prediction of structural and energetic properties for molecular complexes. It begins by encoding an input graph representing a molecular complex using a backbone module, which extracts features from nodes and edges. A structure refinement module then iteratively refines an initial estimate of the mutant structure through multiple cycles, using a masked mutation modeling task that reconstructs corrupted wild-type structures. This refinement process involves applying a probabilistic model to represent atomic positions as Gaussian distributions, capturing uncertainty in molecular configurations. The refined structure is re-encoded, and features from both the wild-type and mutant structures are pooled to generate a final representation. A predictor module then estimates the change in free energy (ΔΔG) based on these representations. The refinement is guided by a loss function that combines structural reconstruction (using Huber loss) and ΔΔG prediction. The PDC-Net, a geometric graph neural network, models atomic positions as probability density clouds, computing mean and variance updates through message passing that incorporates geometric features derived from distributions of distances and angles. This allows the model to capture dynamic variations and encode uncertainty in molecular interactions. The method integrates both structural refinement and ΔΔG prediction into a unified training objective, avoiding reliance on external software for structure sampling.  
DOMAIN: protein-protein interaction modeling  
STRUCTURE: graphical models  
DATA_OBJECT: graph or network  
INFERENCE: none  
PROBLEM_FORM: estimation  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: dataset-with-DOI-or-handle  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
