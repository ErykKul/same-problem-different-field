MECHANISM: Two neural networks are trained: a structure-based teacher network using 3D protein complex descriptors (Moal, Dias, NIRP features) and a sequence-based student network using sequence-derived descriptors (k-mer, ProPy, PSSM, BLOSUM). Both perform regression on binding affinity. The student is trained with three loss components: supervised regression loss on ground-truth affinities, distillation loss matching teacher predictions, and feature-level distillation matching intermediate teacher representations. At inference, only the sequence-based student is used, requiring no structural information.
DOMAIN: Computational structural biology for protein-protein binding prediction
STRUCTURE: other: supervised knowledge distillation from teacher to student network
DATA_OBJECT: set or table
INFERENCE: optimization only
PROBLEM_FORM: prediction or classification
DISTRIBUTION: none
COMPLEXITY: not stated
