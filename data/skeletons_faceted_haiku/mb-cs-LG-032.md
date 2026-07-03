MECHANISM: Neural operators replace classical relaxation smoothers in multigrid methods for solving ill-conditioned linear systems from integral equations. A hierarchical scheme solves linear systems across multiple grid levels. At each level, a trained neural operator (Fourier neural operator) performs a smoothing step that targets specific high-frequency error components corresponding to that grid level. Loss functions incorporate spectral filtering to ensure each operator focuses on its designated frequency band, leaving lower frequencies for coarser grids. The coarsest grid uses an exact solver. Neural smoothers are trained offline on synthetic data using level-wise loss functions with frequency masks, then applied during solve phase to different right-hand-side vectors without retraining.
DOMAIN: Numerical solvers for integral equations using neural operators
STRUCTURE: dense linear algebra
DATA_OBJECT: dense matrix or tensor
INFERENCE: deterministic or closed-form
PROBLEM_FORM: solving linear systems
DISTRIBUTION: none
COMPLEXITY: polynomial iterative
