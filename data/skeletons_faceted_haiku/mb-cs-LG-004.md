MECHANISM: A foundation model backbone is pretrained with self-supervised objectives on 500,000 unlabeled molecules to learn a shared embedding from multiple modalities (SMILES sequences via Transformer, 2D graphs via graph convolutional networks, 3D conformers via continuous-filter convolutions). Bidirectional cross-modal attention between modalities and gated fusion combine representations. Auxiliary encoders process experimental conditions and molecular descriptors. The unified embedding is refined through condition-aware modules parametrized separately per property. Per-property prediction heads implement domain-informed equations with learned coefficients, selected from tournaments of candidate thermophysical models via validation performance. Multi-task training with uncertainty weighting and explicit cross-property physical coupling constraints enforce thermodynamic consistency during training.
DOMAIN: molecular property prediction, computational chemistry, machine learning
STRUCTURE: dense linear algebra
DATA_OBJECT: graph or network
INFERENCE: optimization only
PROBLEM_FORM: estimation
DISTRIBUTION: continuous; continuous
COMPLEXITY: not stated
