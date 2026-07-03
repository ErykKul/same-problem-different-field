MECHANISM: An atomic-level graph representation of molecular structure is constructed from 3D coordinates using k-nearest neighbor connectivity with 5 Angstrom distance cutoff. Node features include element type, residue type, atom type, DSSP secondary structure, and relative solvent accessibility. Edge features encode Euclidean distances and unit direction vectors. Graph Attention Network layers with edge-aware attention coefficients propagate information over 4 layers, maintaining both scalar and tensor states. Atomic-level predictions are aggregated to residues via attention-based pooling with learnable query vectors, then decoded to multi-label binding probabilities.
DOMAIN: Structural bioinformatics for protein-ligand interaction prediction
STRUCTURE: graph traversal
DATA_OBJECT: point set
INFERENCE: optimization only
PROBLEM_FORM: prediction or classification
DISTRIBUTION: none
COMPLEXITY: not stated
