MECHANISM: Dataset distillation creates synthetic datasets by optimizing a subset of samples to match the training dynamics of real datasets. The attack has three sequential stages. In architecture inference, loss trajectories recorded during training on synthetic data are used to train a classifier that identifies which distillation algorithm and model architecture generated the synthetic data. This transforms a black-box scenario to white-box access. In membership inference, a secondary attack model is trained on hidden layer activations from the reconstructed model to determine whether individual samples were in the original dataset. In model inversion, a dual-network diffusion framework with reconstruction, classification, and trajectory-matching losses generates samples from the target distribution that reproduce the victim model's loss trajectory.
DOMAIN: Privacy attacks on dataset distillation methods
STRUCTURE: other: multi-stage adversarial model reconstruction and inversion
DATA_OBJECT: dense matrix or tensor
INFERENCE: optimization only
PROBLEM_FORM: decision or test
DISTRIBUTION: continuous
COMPLEXITY: polynomial iterative
